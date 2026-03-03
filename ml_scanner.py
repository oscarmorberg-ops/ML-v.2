#!/usr/bin/env python3
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from sklearn.ensemble import IsolationForest
import numpy as np

class MLPortScanner:
    def __init__(self, max_workers=50):
        self.model = IsolationForest(contamination=0.1)
        self.open_ports = []
        self.lock = threading.Lock()
        self.max_workers = max_workers
    
    def scan_port(self, target_port):
        target, port = target_port
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            sock.close()
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    print(f"✅ Port {port} OPEN")
        except:
            pass
    
    def scan(self, target, ports):
        print(f"🔥 Scanning {target} med {self.max_workers} threads...")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.scan_port, [(target, port) for port in ports])
        
        # 🔥 ML ANOMALY DETECTION
        if len(self.open_ports) > 0:
            patterns = np.array([[p, 1 if p in self.open_ports else 0] 
                               for p in ports[:100]])
            self.model.fit(patterns)
            anomalies = self.model.predict(patterns)
            print(f"🤖 ML anomalies: {np.sum(anomalies == -1)}/{len(anomalies)}")
        
        print(f"🎯 {len(self.open_ports)} öppna portar: {sorted(self.open_ports)}")

if __name__ == "__main__":
    scanner = MLPortScanner()
    target = "scanme.nmap.org"
    common_ports = list(range(1, 1001))  # 1-1000
    scanner.scan(target, common_ports)
