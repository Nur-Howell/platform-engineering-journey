# Work-Ready Docker Roadmap for Platform Engineers

This guide outlines the essential production-grade Docker concepts required for platform engineering, ordered sequentially for systematic learning.

---

## Step 1: Dockerfile Optimization & Security

Platform engineers design standard container templates for development teams. Enterprise containers must be secure, minimal, and non-root.

### Key Concepts & Instructions

1. **Multi-Stage Builds**:
   * Separate the compilation environment (containing heavy compilers and dependencies) from the runtime environment.
   * Drastically reduces final image size and eliminates unnecessary build tools from production.

2. **Non-Root Execution**:
   * By default, Docker containers run as `root`. If a container is compromised, the attacker has elevated host access.
   * Explicitly create and switch to a non-privileged system user (`USER`).

3. **Layer Caching Optimization**:
   * Order Dockerfile steps from least frequently changed to most frequently changed.
   * Copy dependency files (`package.json`, `go.mod`, `requirements.txt`) and install libraries *before* copying application code.

### Reference Production Dockerfile (Go Example)

```dockerfile
# --- Stage 1: Build Stage ---
FROM golang:1.22-alpine AS builder

WORKDIR /app

# Download dependencies first (leverages layer caching)
COPY go.mod go.sum ./
RUN go mod download

# Copy source code and compile
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-w -s" -o server .

# --- Stage 2: Runtime Stage ---
FROM alpine:3.19

WORKDIR /app

# Create a non-root system user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy compiled binary from builder stage
COPY --from=builder /app/server /app/server

# Change ownership of binary
RUN chown appuser:appgroup /app/server

# Switch to non-root user
USER appuser

EXPOSE 8080

CMD ["/app/server"]
```

---

## Step 2: Storage & State Persistence

Containers are ephemeral by default; destroying a container deletes all modified data inside it. Platform engineers must choose the right storage strategy depending on the workload.

### Storage Paradigms

1. **Named Volumes**:
   * Managed directly by Docker (stored under `/var/lib/docker/volumes/` on Linux).
   * Best for databases, stateful services, and production workloads.
   * Fully decoupled from host file system structures.

2. **Bind Mounts**:
   * Links a specific host directory directly to a container directory (e.g., `-v $(pwd):/app`).
   * Primary use case: Local development with live-reloading.

### Essential Commands

```bash
# Create a named volume for a database
docker volume create postgres_data

# Inspect volume location and metadata
docker volume inspect postgres_data

# Run PostgreSQL using the named volume
docker run -d \
  --name production-db \
  -e POSTGRES_PASSWORD=securepassword \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:16-alpine

# List volumes
docker volume ls
```

---

## Step 3: Networking & Service Discovery

Production container setups do not expose all service ports directly to the public internet. Platform engineers isolate backend services on private virtual networks.

### Networking Paradigms

1. **Default Bridge**:
   * Default network assigned to containers unless specified otherwise.
   * Lacks built-in DNS resolution; containers can only communicate using direct IP addresses.
   * Avoid using in production environments.

2. **User-Defined Bridge Networks**:
   * Custom isolated networks that provide automatic internal DNS resolution between containers using container or service names.

### Practical Implementation

```bash
# Create an isolated network
docker network create platform-net

# Run database on the network (do NOT publish port to host)
docker run -d \
  --name database \
  --network platform-net \
  -e POSTGRES_PASSWORD=secret \
  postgres:16-alpine

# Run API application on the same network
docker run -d \
  --name api-service \
  --network platform-net \
  -p 8080:8080 \
  -e DB_HOST=database \
  my-api-image:latest
```

*Note: `api-service` connects to `database` using the DNS hostname `database:5432` automatically.*

---

## Step 4: Runtime Operations, Healthchecks & Hardening

Once containers run in production, platform engineers ensure they stay healthy and do not exhaust system resources.

### 1. Healthchecks
Allows the Docker Engine or Orchestrator to monitor if an app is internally operational (not just running as a process).

```dockerfile
# Add directly to a Dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1
```

### 2. Resource Limits
Prevents a single container with a memory leak or CPU spike from crashing the underlying server host.

```bash
docker run -d \
  --name restricted-service \
  --memory="512m" \
  --cpus="1.5" \
  my-app:v1
```

### 3. Log Rotation
Prevents `/var/log` or Docker logs from filling up the server disk.

```bash
docker run -d \
  --name app-with-logging \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  my-app:v1
```

---

## Step 5: Multi-Container Orchestration (Docker Compose)

Docker Compose aggregates networks, volumes, resource constraints, and healthchecks into a single declarative configuration file.

### Production-Grade `docker-compose.yml`

```yaml
version: '3.8'

networks:
  app-network:
    driver: bridge

volumes:
  postgres_data:

services:
  database:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppassword
      POSTGRES_DB: maindb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser -d maindb"]
      interval: 5s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M

  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    environment:
      DB_HOST: database
      DB_PORT: 5432
      DB_USER: appuser
      DB_PASSWORD: apppassword
      DB_NAME: maindb
    networks:
      - app-network
    depends_on:
      database:
        condition: service_healthy
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
```

### Management Commands

```bash
# Validate compose syntax
docker compose config

# Start services in detached mode
docker compose up -d

# View consolidated container logs
docker compose logs -f api

# Shut down stack and keep volume data
docker compose down

# Shut down stack and wipe volumes
docker compose down -v
```