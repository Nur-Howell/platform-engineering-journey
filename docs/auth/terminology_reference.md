# Terminology Reference
## Roles
- Resource owner (the user)
- Resource server (the API)
- Authorization server (can be the same server as the API)
- Client (the application)

### Explanation

- **Resource Owner (User / Intent Governor)**: The state-holder who owns data/services and defines access boundaries. Acts as the ultimate authority that injects consent into the system.

- **Resource Server (API / Value Gateway)**: The boundary controller hosting protected data. Accepts requests, validates access tokens (tokens as bearer credentials), and enforces state transitions without needing application-level context.

- **Authorization Server (Token Mint / Identity Broker)**: The central trust authority. Interfaces directly with the Resource Owner to establish consent, evaluates access rules, and mints cryptographically verifiable tokens for authorized entities.

- **Client (Application / Proxy Actor)**: The third-party actor seeking bounded access. Obtains permission from the Authorization Server (via direct assertion or owner redirect) to execute operations on the Resource Server on behalf of the owner.

### Others

- **Access Token (Short-Lived Bearer Credential)**: The transient authorization proof presented to the Resource Server. To the Client, it is an opaque handle or signed payload; to the Resource Server, it represents explicit permission constraints (lifetime, scopes, subject) required to process a request.

- **Refresh Token (Long-Lived Revocation Key)**: A persistent credential stored securely by the Client. Its sole purpose is to request new Access Tokens from the Authorization Server without forcing the Resource Owner to re-authenticate, enabling zero-downtime sessions while minimizing the exposure window of active Access Tokens.

- **Authorization Code (Single-Use Handshake Token)**: A short-lived, ephemeral bridge used during front-channel redirects. It proves that the Resource Owner approved access, allowing the Client to safely exchange it over a secure back-channel for real tokens without exposing token payloads to user-agent/browser history.