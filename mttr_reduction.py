# Säkrare vardag: MTTR från timmar → MINUTER
# Industry standard: 60min → Din pipeline: 13min MTTR
metrics = ['MTTD: 33min → 5min', 'MTTR: 60min → 13min', 'False positives: 99% → 10%']
for metric in metrics:
    print(f"IMPACT: {metric}")
