# Registering a new application

From a systems engineering viewpoint, Client Registration is the initial handshake that establishes identity and trust constraints between a third-party client application and the Authorization Server (AS).

Before any user tokens can be generated or API boundaries crossed, the AS must track who is requesting access, where tokens are allowed to be sent, and what environmental constraints govern the requesting system. Without pre-registration, an Authorization Server cannot enforce access control boundaries or prevent unauthorized redirects.

## Architectural Summary: Client Registration Mechanics

```
    [ Client Developer ]
             │
   (Provide App Metadata)
             ▼
┌──────────────────────────┐
│   Authorization Server   │ ──► Enforces Platform Constraints (Grant Types)
│  (Client Registry DB)    │ ──► Issues Identity Pair (`client_id` + optional `client_secret`)
└──────────────────────────┘ ──► Binds Allowed Target Endpoints (`redirect_uri`)
```

- **Identity Allocation (client_id & client_secret):** The AS assigns a unique, public `client_id` to recognize the app. Confidential clients (like backend servers) receive a sensitive `client_secret` to authenticate themselves during token exchanges. Public clients (like SPAs or mobile apps) are restricted from using secrets since they cannot safely store them.
- **Security Boundary Enforcement (redirect_uri Validation):** The developer must register exact callback URLs. During live authorization flows, the AS strictly checks incoming redirect requests against this registered list to block authorization code interception and open-redirect vulnerabilities.
- **Client Profiling & Capability Assignment:** Platform type selection (Native, SPA, Web Server, Microservice) dictates which OAuth 2.0 grant types are enabled by default (e.g., automatically forcing PKCE for SPAs, issuing secrets only for confidential backends, or disabling unsafe legacy grants like Implicit).
- **Consent & Metadata Binding:** UI-facing metadata (app name, icon, privacy policy link) is stored by the AS to present a clear context to the end-user during the authorization prompt.

---

### Client Registration in OAuth 2.0

Client Registration is the foundational configuration step that registers a third-party application with the Authorization Server (AS) to establish trust, profile system capabilities, and define redirect boundaries.

#### Key Component Functions

* **Credential Provisioning:** Assigns a public `client_id` for tracking and an optional `client_secret` for confidential server-side authentication.
* **Redirect URI Binding:** Restricts authorization response callbacks strictly to pre-validated endpoints to prevent token theft.
* **Client Profiling & Grant Scoping:** Determines whether the app is *Public* or *Confidential* based on its deployment platform (SPA, Web, Native, Service), automatically enforcing relevant security policies (e.g., PKCE, disabling legacy Implicit flows).
* **Metadata Registration:** Stores application identifiers (name, description, privacy)