# Redirect URL Validation
## 1. Validation Checkpoints in the Control Loop
Redirect URL validation operates across three distinct temporal checkpoints within the authorization lifecycle:
* **Node Onboarding (Registration)**: Establishing trusted communication boundaries prior to runtime execution.
* **Inbound Request Gate (Authorization Endpoint)**: Verifying destination authenticity before issuing sensitive state or authorization codes.
* **Token Exchange Verification (Token Endpoint)**: Cross-referencing transaction parameters against initial authorization state.

## 2. Boundary Integrity & Ingress Rules
To maintain system boundary integrity, inputs at registration and authorization endpoints are strictly constrained:
* **Structural Safety**: Custom URL schemes are supported for native client execution, but fragment identifiers (`#`) are strictly rejected during registration.
* **Identity Coupling & Deterministic Matching**: Incoming authorization requests couple `client_id` with a redirect URI. Validation enforces exact string matching against pre-registered destinations; partial or prefix matching introduces vectors where malicious URIs pair with legitimate client IDs.
* **Fail-Closed Isolation**: Mismatched authorization requests trigger an immediate error response without performing redirection, preventing the server from acting as an open redirector.

## 3. Cross-Phase State Consistency
The token endpoint acts as a secondary validation gate to guarantee parameter invariance:
* **Payload Verification**: During code-to-token exchange, the token endpoint verifies that the incoming redirect URL strictly matches the original redirect URL bound to that specific authorization code.
* **Tamper Rejection**: Any discrepancy between the initial authorization route and the exchange request signals code theft or parameter manipulation, triggering immediate transaction rejection.