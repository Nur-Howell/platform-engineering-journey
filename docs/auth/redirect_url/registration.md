# Redirect URL Registration
The OAuth authorization flow relies heavily on the redirect URL, which acts as the critical bridge returning a user to an application post-approval. Because this URL often carries sensitive tokens or authorization codes, treating it as a dynamic, unconstrained variable introduces systemic vulnerabilities (like Open Redirects or token leakage).

To stabilize this feedback loop and secure the boundary, the system must enforce a strict constraint: **pre-registration of allowed redirect URIs**.

By requiring developers to define the exact destination boundaries during application setup, the authorization server can mathematically validate any incoming redirect request against an immutable list. This transforms a potentially volatile input into a predictable, binary outcome (Match/No Match), ensuring the system only routes sensitive data to verified nodes. This constraint must be applied across all client types, with specific adaptations required for the unique routing challenges of mobile environments.

## Redirect URL Registration

## 1. System Vulnerabilities & Surface Area
Allowing dynamic or arbitrary redirection targets transforms the authorization server into an **open redirector**. This expands the attack surface, allowing external actors to manipulate the OAuth loop, intercept sensitive authorization codes/tokens, or exploit the authorization node for non-OAuth redirect attacks.

## 2. Boundary Controls & Input Validation
To stabilize system boundaries, destination points must be explicitly defined during client onboarding and rigorously validated:
* **Strict Whitelisting**: The authorization server must exclusively redirect to explicitly pre-registered URLs.
* **Structural Constraints**: Redirect URLs may contain query parameters but **must reject fragment identifiers** to prevent client-side script injection and state leakage.
* **Cross-Platform Adaptability**: The validation engine must support custom application URI schemes (e.g., `myapp://`) to safely extend boundary enforcement to native and mobile execution environments.

## 3. Decoupling Routing from Dynamic State
Attempting to dynamically modify redirect URLs per request introduces entropy and bypasses route validation. The system resolves this by separating concerns:
* **Routing Determinism**: Redirect URLs require exact-match validation against registered entries for every request.
* **State Isolation**: Dynamic runtime context must be completely offloaded to the dedicated `state` parameter (encoded payload or session ID reference), preserving deterministic routing while supporting transactional fluidity.