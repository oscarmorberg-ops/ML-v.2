#!/usr/bin/env python3
import boto3, argparse, time
from concurrent.futures import ThreadPoolExecutor

class HybridS3Scanner:
    def __init__(self, mode="hybrid", threads=25):
        self.s3 = boto3.client('s3')
        self.mode = mode
        self.threads = threads
        self.recon_hits = self.sniper_hits = 0
        self.recon_patterns = ["backup","db","sql","config","prod"]
        self.sniper_patterns = ["kdb-secrets","seb-master","klarna-api","master.key"]

    def generate_buckets(self, target, count=250):
        base = target.lower().replace(" ","").replace("-","")
        suffixes = ["app","prod","backup","logs","internal"]*50
        return [f"{base}-{s}" for s in suffixes][:count]

    def check_recon(self, bucket):
        return any(p in bucket.lower() for p in self.recon_patterns)

    def check_sniper(self, bucket):
        for p in self.sniper_patterns:
            if p in bucket.lower():
                self.sniper_hits += 1
                print(f"🎯 SNIPER [{self.sniper_hits}]: {bucket}")
                return True
        return False

    def test_bucket(self, bucket):
        try:
            self.s3.head_bucket(Bucket=bucket)
            if self.check_recon(bucket): self.recon_hits += 1
            elif self.check_sniper(bucket): return True
        except: pass
        return False

    def scan(self, target):
        print(f"🔥 HYBRID SCAN v6.0: {target}")
        start = time.time()
        buckets = self.generate_buckets(target)
        with ThreadPoolExecutor(self.threads) as executor:
            executor.map(self.test_bucket, buckets)
        speed = len(buckets)/(time.time()-start)
        precision = (self.sniper_hits/(self.sniper_hits+self.recon_hits+1))*100
        print(f"📊 {target}: {len(buckets)}b | {speed:.1f}b/s")
        print(f"   Recon: {self.recon_hits} | Sniper: {self.sniper_hits}")
        print(f"   🎯 {precision:.1f}% CSIO-grade!")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("--mode", choices=["recon","sniper","hybrid"])
    parser.add_argument("--threads", "-t", type=int, default=25)
    args = parser.parse_args()
    HybridS3Scanner(args.mode or "hybrid", args.threads).scan(args.target)

if __name__ == "__main__": main()
