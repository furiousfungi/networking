import socket
from pathlib import Path

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(ip, port)
        sock.close()
        return result == 0
    except:
        return False

hostname = socket.gethostname()

ipaddr = socket.gethostbyname(hostname)
common_ports = [80,443, 22, 21]
with open('ports_status_report.txt', 'w') as file:
    for port in common_ports:
        if scan_port(ipaddr, port):
            file.write(f"{port} is open\n")
        else:
            file.write(f"{port} is closed\n")

file.close()






