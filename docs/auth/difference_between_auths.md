# Differences between OAuth 1.0 & OAuth 2.0
## Terminology Mapping

| OAuth 1.0 Term | OAuth 2.0 Term | System Role |
| --- | --- | --- |
| User | Resource Owner | The entity granting permission. |
| Consumer | Client | The application seeking access. |
| Service Provider | Resource Server + Authorization Server | Decoupled in 2.0 into separate API and token-minting entities. |
| 2-Legged / 3-Legged | Grant Types (e.g., Auth Code, Client Credentials) | Explicit protocol flows tailored to specific threat models. |

## Bearer Tokens

- **OAuth 1.0 (Asymmetric HMAC/Crypto Signing):**
Uses a dual-key pair (public token + private secret). The client cryptographically signs every individual HTTP request payload locally. The private secret never touches the wire, eliminating reliance on encrypted transport, but placing heavy signature-verification overhead on both client and server.

- **OAuth 2.0 (Bearer Tokens + TLS Transport Security):**
Uses a single, opaque/signed string as a possession-based credential. Anyone holding the token gets access ("proof-of-possession" is omitted at the application layer). Security is offloaded entirely to the transport layer (TLS/HTTPS), simplifying client code while making encrypted pipes mandatory.

### Trade-off Analysis

| Metric / Dimension | OAuth 1.0 (Signed Requests) | OAuth 2.0 (Bearer Tokens) |
| --- | --- | --- |
| Trust Model | Cryptographic proof per request | Possession + Transport Layer Encryption (TLS) |
| Network Security Requirement | Works over HTTP (payload signed) | Strictly requires HTTPS (plaintext token in transit) |
| Implementation Complexity | High (Requires custom crypto libraries) | Extremely Low (`Authorization: Bearer <token>`) |
| Replay Attack Vulnerability | Low (Signed nonces & timestamps prevent replay) | High (Intercepted tokens can be replayed immediately) |
| System Blast Radius | Isolated to token compromise | Higher; requires rapid token revocation / short lifetimes |

### Security Trade-off Mitigations

1. Short lifetimes
2. Strict TLS Enforcement
3. Sender-Constrained Tokens

## Seperation of Roles

### Architectural Decoupling: AS vs. RS

* **Authorization Server (Identity Control Plane):** Manages high-friction operations like user authentication, consent prompts, client metadata (`client_id`, `client_secret`), and token issuance.
* **Resource Server (Data/Value Plane):** Focuses exclusively on low-latency domain logic and payload delivery. It validates incoming access tokens and fulfills API requests without needing user credentials or app registry data.

---

### Systemic Benefits & Architectural Trade-offs

| System Dimension | Monolithic Auth (OAuth 1.0 style) | Separated Auth Architecture (OAuth 2.0) |
| :--- | :--- | :--- |
| **Data Store Coupling** | Shared DB required for credentials & sessions | Fully decoupled; RS does not need access to AS user/client DBs |
| **Scalability & Routing** | Bound to same infrastructure / domain | AS (`accounts.google.com`) and RS (`googleapis.com`) scale independently |
| **Security Surface Area** | Secrets (`client_secret`) exposed across all servers | Secrets restricted strictly to the AS boundary; RS only sees tokens |
| **Organizational Velocity** | Monolithic codebase; coupled deployments | Autonomous domain teams operating on independent release cycles |

---

### Key Takeaway for Platform Engineers

Separating the Control Plane (AS) from the Data Plane (RS) allows you to scale stateless API gateways across hundreds of microservices, subdomains, or regions while keeping your sensitive authentication infrastructure isolated and highly secured.