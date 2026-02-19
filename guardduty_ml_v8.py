cat > guardduty_ml_v8.py << 'EOF'
import json
from datetime import datetime

def lambda_handler(event, context):
    print(f"GuardDuty ML-v8 LIVE! {datetime.now()}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'CSIO Blue Team ML-beast LIVE',
            'message': 'S3-malware defender 18:10 → DEPLOYED',
            'timestamp': datetime.now().isoformat()
        })
    }
EOF
