# DHCP Learning & Implementation Guide: Kea DHCPv4 on Ubuntu Server

## Executive Summary
This document serves as a reference manual detailing the fundamental concepts of the Dynamic Host Configuration Protocol (DHCP), hands-on deployment of **Kea DHCPv4** on Ubuntu Server, configuration structures, and management procedures.

---

## 1. Fundamentals of DHCP

### 1.1 What is DHCP?
Dynamic Host Configuration Protocol (DHCP) is a network management protocol used on Internet Protocol (IP) networks to automatically assign IP addresses and other communication parameters (such as subnet mask, default gateway, and DNS servers) to devices, enabling them to communicate on network interfaces.

### 1.2 The DORA Process
The IP address assignment follows a four-step handshake known as **DORA**:

```
+----------------+                    +----------------+
|  DHCP Client   |                    |  DHCP Server   |
+----------------+                    +----------------+
        |                                     |
        | ------ 1. DHCPDISCOVER (BCAST) ---> |
        | <----- 2. DHCPOFFER   (UCAST) ----  |
        | ------ 3. DHCPREQUEST (BCAST) ---> |
        | <----- 4. DHCPACK     (UCAST) ----  |
        |                                     |
```

1. **Discover (DHCPDISCOVER)**: The client broadcasts a request searching for available DHCP servers on the subnet (`255.255.255.255`, UDP port 67).
2. **Offer (DHCPOFFER)**: The DHCP server responds with an available IP address offer, network parameters, and lease time (`UDP port 68`).
3. **Request (DHCPREQUEST)**: The client broadcasts an acceptance of the offered address, notifying all DHCP servers on the local network.
4. **Acknowledge (DHCPACK)**: The server confirms the lease and finalizes the configuration parameters.

### 1.3 Key Network Parameters Provided by DHCP
- **IP Address & Subnet Mask**: Defines host identity and local subnet boundaries.
- **Default Gateway (Router)**: Directs outbound traffic beyond the local subnet.
- **Domain Name System (DNS) Servers**: Enables hostname-to-IP resolution.
- **Lease Duration**: Specifies how long the host holds the IP address before renewal (`DHCPREQUEST` at 50% lease time renewal threshold).

---

## 2. Implementing Kea DHCP Server on Ubuntu Server

ISC Kea is a modern, high-performance, modular DHCP server developed by Internet Systems Consortium (ISC) to replace the legacy `isc-dhcp-server`.

### 2.1 Installation
On modern Ubuntu releases (20.04/22.04/24.04 LTS), Kea is available from standard repositories:

```bash
# Update package index
sudo apt update

# Install Kea DHCPv4 service
sudo apt install -y kea-dhcp4-server
```

### 2.2 Managing the Kea Service

| Action | Command |
| :--- | :--- |
| **Start Service** | `sudo systemctl start kea-dhcp4-server` |
| **Stop Service** | `sudo systemctl stop kea-dhcp4-server` |
| **Restart Service** | `sudo systemctl restart kea-dhcp4-server` |
| **Check Status** | `sudo systemctl status kea-dhcp4-server` |
| **Enable on Boot** | `sudo systemctl enable kea-dhcp4-server` |
| **Test Syntax** | `sudo kea-dhcp4 -t /etc/kea/kea-dhcp4.conf` |

---

## 3. Detailed Kea DHCPv4 Configuration (`kea-dhcp4.conf`)

Kea utilizes structured **JSON** format for configuration. The primary configuration file is located at `/etc/kea/kea-dhcp4.conf`.

### 3.1 Annotated Master Configuration Example

```json
{
  "Dhcp4": {
    // 1. Network Interfaces Selection
    "interfaces-config": {
      "interfaces": [ "eth0" ],
      "dhcp-socket-type": "raw"
    },

    // 2. Control Agent Integration (REST API / Management)
    "control-socket": {
      "socket-type": "unix",
      "socket-name": "/run/kea/kea4-ctrl-socket"
    },

    // 3. Lease Storage Engine (In-Memory Memfile)
    "lease-database": {
      "type": "memfile",
      "persist": true,
      "name": "/var/lib/kea/kea-leases4.csv"
    },

    // 4. Lease Timers (In Seconds)
    "valid-lifetime": 4000,
    "renew-timer": 1000,
    "rebind-timer": 2000,

    // 5. Global Options (Fallback if not overridden in subnets)
    "option-data": [
      {
        "name": "domain-name-servers",
        "data": "1.1.1.1, 8.8.8.8"
      },
      {
        "name": "domain-name",
        "data": "lab.internal"
      }
    ],

    // 6. Subnet & IP Pool Definitions
    "subnet4": [
      {
        "id": 1,
        "subnet": "192.168.1.0/24",
        "pools": [
          {
            "pool": "192.168.1.100 - 192.168.1.200"
          }
        ],
        "option-data": [
          {
            "name": "routers",
            "data": "192.168.1.1"
          }
        ],

        // 7. Static IP Reservations (MAC Binding)
        "reservations": [
          {
            "hw-address": "00:11:22:33:44:55",
            "ip-address": "192.168.1.50",
            "hostname": "printer-office"
          }
        ]
      }
    ]
  }
}
```

---

## 4. Key Configuration Parameters Quick Reference

| JSON Key | Purpose | Description / Example |
| :--- | :--- | :--- |
| `interfaces-config.interfaces` | Interface Selection | Network card(s) Kea listens on (`["eth0", "eth1"]` or `["*"]`). |
| `lease-database` | Lease Storage | Configures database backend (`memfile`, `mysql`, `postgresql`). |
| `valid-lifetime` | Default Lease Time | Total duration (seconds) an assigned IP remains valid. |
| `renew-timer` | Renewal Interval | Time before client attempts to extend lease with current server (`T1`). |
| `rebind-timer` | Rebind Interval | Time before client broadcasts to find *any* server if primary fails (`T2`). |
| `subnet4` | Subnet Array | Contains subnet blocks, address ranges, and subnet-specific options. |
| `pools` | Dynamic Address Ranges | Ranges of IP addresses reserved for dynamic assignment. |
| `option-data` | DHCP Options | Options array such as `routers` (Option 3) and `domain-name-servers` (Option 6). |
| `reservations` | Static Leases | Maps physical MAC addresses (`hw-address`) to explicit IP addresses. |

---

## 5. Operations & Troubleshooting

### 5.1 Verification & Log Inspection
Check service logs for initialization errors, lease transactions, or syntax mismatches:

```bash
# View real-time logs via Systemd journal
sudo journalctl -u kea-dhcp4-server -f -n 50

# Inspect active DHCP leases
sudo cat /var/lib/kea/kea-leases4.csv
```

### 5.2 Firewall Configuration (`UFW`)
Ensure firewall rules permit inbound DHCP broadcast/unicast traffic:

```bash
# Allow UDP Ports 67 & 68
sudo ufw allow 67/udp
sudo ufw allow 68/udp
sudo ufw reload
```

### 5.3 Client-Side Testing & Verification
On a Linux client machine:

```bash
# Release current DHCP lease
sudo dhclient -r

# Obtain new DHCP lease with verbose output
sudo dhclient -v
```

---

## 6. Summary of Key Learnings
- Learned the 4-way **DORA** handshake mechanism powering host auto-configuration.
- Migrated focus to **Kea DHCP**, the modern, JSON-configured standard replacing `isc-dhcp-server`.
- Configured declarative subnet pools, global/subnet-specific options, and static MAC-to-IP reservations on Ubuntu Server.
- Developed practical troubleshooting routines using `journalctl`, lease file inspection, and configuration validation options (`kea-dhcp4 -t`).
