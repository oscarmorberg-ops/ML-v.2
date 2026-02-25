#!/usr/bin/env python3
import socket
from sklearn.ensemble import IsolationForest  
import numpy as np

class MLPortScanner:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.patterns = []
    
    def scan_port(self, target, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        self.patterns.append([port, result])
        return result == 0

if __name__ == "__main__":
    scanner = MLPortScanner()
    target = "scanme.nmap.org"
    for port in [22, 80, 443]:
        if scanner.scan_port(target, port):
            print(f"Port {port} OPEN")

