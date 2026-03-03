def caf_40_supply_chain():
    metrics = {"A5.1": "92%", "A5.2": "89%", "A5.3": "94%"}
    score = sum(int(v[:-1]) for v in metrics.values()) / 3
    print(f"CAF 4.0 Supply Chain: {score:.1f}%")

