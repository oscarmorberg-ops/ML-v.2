# 🚀 CyberSec S3 Pipeline (Rust)
Production AWS S3 + GuardDuty Security Scanner

[![Rust](https://img.shields.io/badge/rust-1.81-success)](https://rust-lang.org)
[![Async](https://img.shields.io/badge/tokio-async-blue)](https://tokio.rs)

## Features
- 🔴 **S3 Scanner**: Public ACLs, encryption, versioning  
- 🛡️ **GuardDuty**: CRITICAL findings (Backdoor, DataExfil)
- ⚡ **Async**: tokio::join! parallel scanning
- 📊 **CLI**: Production-grade output + summary

## Quick Start
```bash
git clone https://github.com/oscarmorberg-ops/ML-v.2.git
cd cybersec-s3-pipeline
cargo run

S3 Security Issues:   3
GuardDuty Findings:   2
TOTAL CRITICAL:       5
✅ Scan complete!

Tech Stack
Rust 1.81 + Tokio (async)

Chrono (timestamps)

402 commits • Part of oscarmorberg-ops AWS suite
