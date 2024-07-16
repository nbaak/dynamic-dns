# Simple DNS Server

This is a simple DNS server implemented in Python using the `socket` library. It currently supports basic A record (IPv4 address) queries.

## Features

- Handles basic A record queries
- Simple and easy to understand
- Configurable DNS records

## Requirements

- Python 3.x

## Usage No Docker

1. **Clone the repository or download the script**:
Create VENV and install dependencies:

```sh
python3 -m venv ddns
. ddns/bin/actkivate
python3 -m pip -r requirements.txt
```

IF you want to run it on Port 53 (default DNS port, you have to install the packages as root! NOT RECOMMENDED).

```sh
sudo python3 -m pip -r requirements.txt
```

2. **Run the DNS server**

```sh
sudo python3 dnsserver.py -p 53
```

Note: Binding to port 53 requires administrative privileges. Use sudo if necessary.

3. **Test the DNS server**
Set a custom handler:

```sh
curl localhost:5000/nic/update/test/0.8.1.5
```

You can test the DNS server using the dig command or any DNS query tool:

```sh
dig @localhost test.localhost.lan
```

## Usage Docker

**TODO**
Compose Stack is not ready yet.

```sh
docker compose up -d
```