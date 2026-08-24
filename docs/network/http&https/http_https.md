# HTTP vs HTTPS
- HTTP with encryption.
- HTTPS uses TLS (SSL).
## HyperText Transfer Protocol
- Protocol for transferring hypertext over the web.
- Data transfer.
- Plain text exchanged which is less secure.
- Stateless (ends after transaction).
## Pros
- Reduction of CPU and memory utilization.
- Pipeline
- Less network congestion.
## Cons
- P2P connection.
- Non-mobile friendly.
- No trustworthy exchane.
# HTTPS
End-to-end encryption and authentication by leveraging TLS/SSL.
- HTTPS is used for secure communication as Hypertext Transfer Protocol (HTTP) doesn't.
- Data can be transferred using this protocol in an encrypted format.
- The HTTPS protocol is mostly utilized in situations when entering login credentials is necessary. Modern browsers like Chrome distinguish between the HTTP and HTTPS protocols based on distinct markings.

![HTTPS](tcp_connection.webp)
## Pros
- Provides in-transit data security.
- Shields your website from data breaches, phishing, and MITM attacks.
- Increases the visitors' trust to your website.
## Cons
- While switching to HTTPS SSL certificate needs to be bought.
- Encrypting and decrypting data across HTTPS connections requires a lot of computation.
- There will be issues with caching some information over HTTPS. Public caching of those that previously took place won't happen again. 
## Ports
- `HTTP = 80`
- `HTTPS = 443`
