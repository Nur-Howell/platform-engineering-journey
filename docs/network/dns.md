# DNS
Translation of IP addresses into readable domains that the computer can use to communicate.
- name to address resolution
- cache (lowers lookup time)
## Working
- User input
- Load local cache
- DNS resolver query
- Root server query
- TLD server response
- Authoritative server response
- Final response
## Structure of DNS
1. Root
- Represented by a dot (.) at the end of a domain name
Acts as the starting point of domain resolution
2. TLD
- Includes extensions like .com, .org, .net, .edu
Helps categorize domains by purpose or region
3. SLD
- Appears before the TLD (e.g., "example" in example.com)
Uniquely identifies a domain under a TLD
4. Subdomains
- Examples: www, mail, blog
Helps structure different parts of a website
5. Hostnames
- Examples: web1, mailserver, ftp
Maps to actual IP addresses using DNS records
- ![DNS TUT](https://www.geeksforgeeks.org/computer-networks/domain-name-system-dns-in-application-layer/)
- ![Debian WIKI](https://wiki.debian.org/dnsmasq)
