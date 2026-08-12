# Verify or install Netcat on Ubuntu [1, 2]
sudo apt update && sudo apt install netcat-openbsd

# Backup current network configuration settings [3]
sudo sysctl -a | grep "^net\." > /tmp/network-sysctl-backup.conf

# View current socket buffer configuration [3]
sysctl net.ipv4.tcp_rmem
sysctl net.ipv4.tcp_wmem
sysctl net.core.rmem_max
sysctl net.core.wmem_max

# Temporarily modify network socket read/write limits [3, 4]
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216

# Configure persistent high-performance network buffers and TCP options [5]
sudo tee /etc/sysctl.d/99-network-tuning.conf << 'EOF'
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216
net.core.rmem_default = 1048576
net.core.wmem_default = 1048576
net.ipv4.tcp_rmem = 4096 131072 16777216
net.ipv4.tcp_wmem = 4096 131072 16777216
net.ipv4.tcp_mem = 786432 1048576 1572864
net.ipv4.tcp_window_scaling = 1
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_sack = 1
EOF

# Apply newly defined persistent sysctl configurations [3, 6]
sudo sysctl --system

# Start an interactive TCP listener (Server) on port 8080 [7, 8]
nc -lk 8080

# Connect to the active TCP server socket (Client) [7, 8]
nc 127.0.0.1 8080

# Start an interactive UDP listener (Server) on port 8080 [8, 9]
nc -ul 8080

# Connect to the active UDP server socket (Client) [8, 9]
nc -u 127.0.0.1 8080

# Monitor active TCP connection states (LISTEN, ESTABLISHED, etc.) [10]
ss -atn

# Monitor active UDP socket assignments [10]
ss -aun

# Identify owning process names and PIDs for active sockets [10]
sudo ss -atnp

# Display a high-level summary of active sockets across the OS [10, 11]
ss -s

# Capture and analyze the TCP 3-way handshake on port 8080 [12]
sudo tcpdump -i any -n tcp port 8080 -v

# Inspect independent UDP datagram payloads on port 8080 in hex/ASCII [12]
sudo tcpdump -i any -n udp port 8080 -X