# ssh
Access for a user to another PC romotely over a network.
* Port: 22 (TCP)
## ssh access syntax
`ssh [username]@[hostname or IP address]`
## ssh apt
`sudo apt install openssh-client openssh-server`
## systemctl start/enable sshd
```
sudo systemctl start ssh
sudo systemctl enable ssh
```
## key generation ssh (authentication)
`ssh-keygen`
> [!Note]
> Copy public key to the remote server. This allows for login without the need of a password.
> `ssh-copy-id username@server_ip`
## requirements
To successfully connect to a remote Linux machine using SSH, ensure the following:

   - The server must be switched on and connected to a network.
   - You should have valid login credentials
   - The OpenSSH server must be installed and active.
   - Port 22 (or the configured custom port) should be open on your firewall.
## ssh secure communication
SSH uses multiple layers of cryptography:

   - Symmetric Encryption: Uses one shared key for encrypting and decrypting the session.
   - Asymmetric Encryption: Uses a public/private key pair for authentication and key exchange.
   - Hashing: Ensures message integrity - any tampering is immediately detected.
