def main():
    payloads = [
        "' OR 1=1 --",
        "' OR '1'='1' --",
        '" OR "1"="1" --',
    ]
    for payload in payloads:
        print(f"[SQLi] Testing payload: {payload}")
        # din test‑logik här

if __name__ == "__main__":
    main()
