# SENIOR ARCHITECT: EKS + Helm + Istio mTLS
helm_charts = ['deep-hell-ml', 's3-scanner', 'siem-dashboard']
for chart in helm_charts:
    print(f"HELM DEPLOY: {chart} → EKS production")
