from pathlib import Path
import socket
from scanport import scan_port


common_file = Path("ports_status_report.txt")


class SystemInfo:
    def __init__(self, filepath: Path):
        self.filepath = filepath

    def create_file(self):
        self.filepath.touch(exist_ok=True)

    def show_ip(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            with self.filepath.open("a") as file:
                file.write(f"\nYour IP address is {ip_address}\n\n")
        except socket.error as e:
            print(f"Error getting IP address: {e}")


class ShowPorts:
    def scan(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            common_ports = [80, 443, 22, 21]

            with common_file.open('a') as file:
                for port in common_ports:
                    status = "open" if scan_port(ip_address, port) else "closed"
                    file.write(f"Port {port} is {status}\n")

        except socket.error as e:
            print(f"Network error: {e}")


def main():
    system_info = SystemInfo(common_file)
    system_info.create_file()
    system_info.show_ip()


    port_scanner = ShowPorts()
    port_scanner.scan()


if __name__ == "__main__":
    main()