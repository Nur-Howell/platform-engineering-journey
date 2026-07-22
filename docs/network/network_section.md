# Platform Engineering Roadmap – Networking

## 🟢 Tier 1 — Fast Wins (1–2 Days Each)

These concepts are relatively quick to understand and can be reinforced with a small lab.

### 1. HTTP vs HTTPS
**Learn**
- How HTTP communication works.
- The difference between HTTP and HTTPS.
- Why HTTPS provides encryption.

**Build**
- Host a simple webpage using Nginx over HTTP.
- Later transition the same site to HTTPS.

---

### 2. DNS
**Learn**
- How DNS resolves domain names to IP addresses.
- DNS records (A, CNAME, etc.).

**Build**
- Configure local DNS using `/etc/hosts`.
- Create local DNS records (e.g., AdGuard DNS).
- Point a hostname to your web server.

---

### 3. SSL/TLS Certificate Management
**Learn**
- SSL/TLS fundamentals.
- Certificates, Certificate Authorities (CAs), public/private keys.
- Certificate lifecycle and trust.

**Build**
- Generate a self-signed certificate using OpenSSL.
- Configure HTTPS with Nginx using the certificate.

---

### 4. Web Servers (Nginx Basics)
**Learn**
- What a web server does.
- Virtual hosts/server blocks.
- Static content hosting.

**Build**
- Install Nginx.
- Serve a basic HTML page.
- Configure a virtual host.

---

# 🟡 Tier 2 — Moderate

Requires a little more networking knowledge but still straightforward to implement.

### 5. TCP vs UDP
**Learn**
- Connection-oriented vs connectionless communication.
- Reliability, ordering, and performance differences.

**Build**
- Experiment using `netcat (nc)`.
- Compare protocols used by SSH (TCP) and DNS (UDP).

---

### 6. DHCP
**Learn**
- Dynamic IP address assignment.
- DHCP lease process.

**Build**
- Configure a DHCP server within an isolated virtual network.
- Observe clients automatically receiving IP addresses.

---

### 7. Load Balancing
**Learn**
- Purpose of load balancing.
- High availability concepts.
- Reverse proxy fundamentals.

**Build**
- Deploy two web servers.
- Configure Nginx or HAProxy as a load balancer.

---

# 🟠 Tier 3 — More Involved

Requires stronger networking knowledge and multiple concepts working together.

### 8. Firewalls
**Learn**
- Packet filtering.
- Ports.
- Inbound vs outbound traffic.
- Security policies.

**Build**
- Configure `ufw`.
- Allow SSH and HTTP.
- Block unnecessary ports.

---

### 9. VPN
**Learn**
- Secure remote access.
- Encryption.
- Authentication.
- Tunneling.

**Build**
- Deploy a WireGuard VPN.
- Connect remotely to your homelab.

---

### 10. NAT Gateways
**Learn**
- Private vs public addressing.
- Network Address Translation.
- Routing.

**Build**
- Configure NAT between virtual networks.
- Observe address translation in practice.

---

# 🔴 Tier 4 — Continuous Learning

These topics develop naturally as you progress through your platform engineering journey.

### 11. Security
**Topics**
- SSH hardening.
- TLS best practices.
- Firewalls.
- Least privilege.
- Authentication.
- Secrets management.
- Updates.
- Monitoring.
- Logging.

---

# Suggested Learning Order

1. ✅ SSH *(Completed)*
2. HTTP vs HTTPS
3. Nginx (Web Server)
4. DNS
5. SSL/TLS Certificate Management
6. Firewalls (`ufw`)
7. TCP vs UDP
8. Load Balancing
9. DHCP
10. VPN
11. NAT Gateways
12. Continue improving security throughout the journey

---

## Learning Philosophy

- Learn enough theory to understand the concept.
- Build a small project immediately after.
- Document everything.
- Move on once the concept is understood and working.
- Revisit topics later as your infrastructure becomes more advanced.
