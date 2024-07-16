from dnslib import DNSRecord, RR, A, RCODE
import socket
from flask import Flask, jsonify, request
import threading

# Sample DNS records
DNS_RECORDS = {
    "example": "1.2.3.4",
    "test": "4.3.2.1",
}

app = Flask(__name__)


def handle_dns_query(data, addr, server_socket):
    request = DNSRecord.parse(data)
    query_name = str(request.q.qname)
    query_name = query_name.rstrip('.')
    
    handle = ""
    try:
        split_query = query_name.split('.')
        if len(split_query) == 3:
            handle = split_query[0]
        
    except:
        pass
    
    reply = request.reply()
    
    if handle:
        if handle in DNS_RECORDS:
            ip_address = DNS_RECORDS[handle]
            reply.add_answer(RR(query_name, rtype=1, rclass=1, ttl=60, rdata=A(ip_address)))
        else:
            reply.header.rcode = RCODE.NXDOMAIN  # Set NXDOMAIN error code for non-existent domain
    else:
        reply.header.rcode = RCODE.NXDOMAIN

    server_socket.sendto(reply.pack(), addr)


@app.route('/nic/update/<handle>', defaults={'ip': None}, methods=['GET'])
@app.route('/nic/update/<handle>/<ip>', methods=['GET'])
def update_dns_record(handle, ip=None):
    if ip is None:
        ip = request.remote_addr  # Get IP address of the sender
    DNS_RECORDS[handle] = ip
    return jsonify({"message": f"DNS record updated for {handle} with IP {ip}"}), 200


def start_dns_server(addr:str="127.0.0.1", port:int=53):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((addr, port))

        print(f"DNS server is running on {addr}:{port}...")

        while True:
            data, addr = server_socket.recvfrom(512)
            handle_dns_query(data, addr, server_socket)
    except Exception as e:
        print(f"Error starting DNS server: {e}")


def main():
    # Start DNS server in a separate thread
    dns_thread = threading.Thread(target=start_dns_server, args=("0.0.0.0", 5300))
    dns_thread.start()

    # Run Flask app
    app.run(debug=True)


if __name__ == "__main__":
    main()
