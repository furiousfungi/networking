from pathlib import Path
import socket
from scanport import scan_port

open('ports_status_report.txt', 'w').close()

class Malware:
    def __init__(self, content):
        self.content = content

    def display(self):
        Path(self.content).write_text('')

    def showip(self):
        hostname = socket.gethostname()
        ipadr = socket.gethostbyname(hostname)
        file_path = Path(self.content)
        with file_path.open('a') as file:
            file.write(f"Your ip address is {ipadr}\n\n")
        file.close()

class Showports:
    def scanner(self):
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyname(hostname)
        common_ports = [80, 443, 22, 21]
        with open('ports_status_report.txt', 'a') as file:
            for port in common_ports:
                if scan_port(ipaddr, port):
                    file.write(f"{port} is open\n")
                else:
                    file.write(f"{port} is closed\n")

        file.close()
        
