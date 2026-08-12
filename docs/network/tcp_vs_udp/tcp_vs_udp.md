Summary of Key Learnings
1. Transport Protocol Characteristics

    * TCP (Transmission Control Protocol) is connection-oriented. It relies on a formal three-way handshake (SYN, SYN-ACK, ACK) to establish a stateful session before transferring data. It guarantees reliable, in-order packet delivery through acknowledgements (ACKs) and automatic retransmission of lost packets.
    * UDP (User Datagram Protocol) is connectionless and lightweight. It bypasses connection handshakes and provides no guarantees of delivery, ordering, or retransmission.
    * Control Mechanisms: TCP actively prevents network congestion and receiver overload using dynamic flow control and congestion control. UDP lacks these mechanisms, transmitting data as fast as the system allows.
    * Data Models & Transmission: TCP abstracts application messages into a continuous byte stream, supporting only point-to-point (unicast) channels. UDP preserves message boundaries by treating data as independent, discrete messages, and natively supports broadcasting and multicasting.
    Header Overhead: TCP headers are variable in size (20 to 60 bytes) to support control flags and window options. UDP headers are fixed at a lightweight 8 bytes.

2. Practical Systems Behaviors on Ubuntu

   *  The UDP Feedback Void: Because UDP is connectionless, it has no handshake or delivery confirmation. Sending UDP packets to a closed port will succeed silently on the client side without returning a "Connection refused" error, forcing administrators to use raw packet capture (tcpdump) to diagnose delivery failures.
  *  Privileged Ports Constraint: Ubuntu blocks regular (non-root) processes from binding to system ports under 1024 for security; custom network tests must use unprivileged ports like 8080.
   * Kernel Socket Visibility: Modern Ubuntu VMs deprecate netstat in favour of the faster ss (Socket Statistics) utility, which reads directly from kernel memory. Stateful TCP sockets are tracked under explicit transitions (such as LISTEN or ESTABLISHED), whereas stateless UDP sockets appear with generic placeholders (such as UNCONN).
   * Cleartext Security Risks: Standard Netcat (nc) transmits all data in unencrypted cleartext with no authentication. Exposing these listeners on untrusted networks exposes raw data and files to trivial capture.