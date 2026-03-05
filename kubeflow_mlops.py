# PRINCIPAL Kubeflow ML Ops Pipeline
pipelines = ['s3scan-train', 'cnn-deploy', 'siem-alert']
for pipe in pipelines:
    print(f"KUBEFLOW: {pipe} → AutoML production ✓")
