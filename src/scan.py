#!/usr/bin/env python3
"""
Host-Scan: A concurrent port scanner with basic evasion techniques.
This project is for educational and ethical cybersecurity purposes only.
"""

import concurrent.futures
import os
import signal
import socket
import struct
import subprocess
import sys
from typing import List, Tuple

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # Fallback if colorama is not installed
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = WHITE = LIGHTCYAN_EX = LIGHTMAGENTA_EX = LIGHTGREEN_EX = ""
    class Style:
        DIM = BRIGHT = NORMAL = ""


class PortScanner:
    def __init__(self, host: str, timeout: float = 0.1):
        self.host = host
        self.timeout = timeout
        self.tcp_ports: List[int] = []
        self.udp_ports: List[int] = []

    def scan_tcp(self, port: int) -> bool:
        """Attempts a TCP connection to the specified port."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                result = s.connect_ex((self.host, port))
                if result == 0:
                    self.tcp_ports.append(port)
                    return True
        except Exception:
            pass
        return False

    def scan_udp(self, port: int) -> bool:
        """Attempts to identify an open UDP port by sending a payload."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(self.timeout)
                if port == 53:
                    # DNS Query for www.example.com
                    data = struct.pack("!HHHHHH", 1, 0, 1, 0, 0, 0)
                    data += b"\x03www\x07example\x03com\x00"
                    data += struct.pack("!HH", 1, 1)
                else:
                    data = b""
                
                s.sendto(data, (self.host, port))
                try:
                    s.recvfrom(1024)
                    self.udp_ports.append(port)
                    return True
                except (socket.timeout, socket.error):
                    pass
        except Exception:
            pass
        return False

    def run_scan(self, port_range: range = range(1, 1025), max_workers: int = 500):
        """Runs the concurrent scan for both TCP and UDP."""
        print(f"{Fore.CYAN}[*] Starting scan on {self.host}...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # TCP Scan
            list(executor.map(self.scan_tcp, port_range))
            # UDP Scan
            list(executor.map(self.scan_udp, port_range))


def setup_environment():
    """Initial environment setup (ulimit, screen clear)."""
    if sys.platform.startswith('linux'):
        try:
            subprocess.run(["ulimit", "-n", "5100"], check=False)
        except Exception:
            pass


def handle_sigint(sig, frame):
    print(f"\n{Fore.RED}[!] Scan interrupted by user. Exiting...")
    sys.exit(0)


def copy_to_clipboard(data: str):
    """Utility to copy data to clipboard using xclip."""
    try:
        subprocess.run(["xclip", "-sel", "clip"], input=data.encode(), check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def main():
    signal.signal(signal.SIGINT, handle_sigint)
    
    # Header
    try:
        subprocess.run("clear", shell=True)  # nosec B602
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Host Scan - Professional Network Scanner")
    except Exception:
        pass

    target = input(f"{Fore.WHITE}Introduce the target IP/Host: ").strip()
    if not target:
        print(f"{Fore.RED}Error: Target cannot be empty.")
        return

    setup_environment()
    
    scanner = PortScanner(target)
    # Scanning first 1024 ports by default for speed, but configurable
    scanner.run_scan(port_range=range(1, 1025))

    print(f"\n{Fore.GREEN}[+] Scan complete!")
    print(f"{Fore.BLUE}[+] Open TCP Ports: {', '.join(map(str, sorted(scanner.tcp_ports))) or 'None'}")
    print(f"{Fore.YELLOW}[+] Open UDP Ports: {', '.join(map(str, sorted(scanner.udp_ports))) or 'None'}")

    if scanner.tcp_ports:
        choice = input(f"\n{Fore.WHITE}Copy TCP ports to clipboard? (y/n): ").lower()
        if choice == 'y':
            if copy_to_clipboard(",".join(map(str, sorted(scanner.tcp_ports)))):
                print(f"{Fore.GREEN}[*] TCP ports copied!")
            else:
                print(f"{Fore.RED}[!] Could not copy. Is xclip installed?")

    if scanner.udp_ports:
        choice = input(f"{Fore.WHITE}Copy UDP ports to clipboard? (y/n): ").lower()
        if choice == 'y':
            if copy_to_clipboard(",".join(map(str, sorted(scanner.udp_ports)))):
                print(f"{Fore.GREEN}[*] UDP ports copied!")
            else:
                print(f"{Fore.RED}[!] Could not copy. Is xclip installed?")


if __name__ == "__main__":
    main()
