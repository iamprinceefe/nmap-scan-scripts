#!/usr/bin/python3

import socket
import dns.resolver
import sys

# Adjust path for custom module
sys.path.append('/home/kali/Downloads/')
import common_ports 

def get_open_ports(target, port_range, verbose=False):
    # Function to check if a port is open
    def is_port_open(ip, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            try:
                s.connect((ip, port))
                return True
            except (socket.timeout, socket.error):
                return False

    # Resolve hostname to IP address
    def resolve_hostname(hostname):
        try:
            result = dns.resolver.resolve(hostname, 'A')
            return result[0].to_text()
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return None

    # Validate IP address
    def validate_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False

    # Get the IP address from the target
    if validate_ip(target):
        ip_address = target
    else:
        ip_address = resolve_hostname(target)
        if not ip_address:
            return "Error: Invalid hostname"

    if not validate_ip(ip_address):
        return "Error: Invalid IP address"

    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        if is_port_open(ip_address, port):
            open_ports.append(port)

    if verbose:
        result = [f"Open ports for {target} ({ip_address})"]
        result.append("PORT       SERVICE")
        for port in open_ports:
            service = common_ports.get(port, "unknown")
            result.append(f"{port:<7} {service}")
        return "\n".join(result)

    return open_ports
