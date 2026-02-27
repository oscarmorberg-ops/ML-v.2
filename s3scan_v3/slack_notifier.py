import os
from slack_sdk import WebhookClient
from dotenv import load_dotenv

load_dotenv()

class SlackNotifier:
    def __init__(self, webhook_url=None):
        self.webhook = WebhookClient(webhook_url or os.getenv('SLACK_WEBHOOK'))
    
    def send_iam_alert(self, vulns):
        message = f"""
🚨 s3scan v3 IAM ALERT!
Found {len(vulns)} public IAM policies:
{chr(10).join([f"• {v}" for v in vulns[:5]])}

Multiverse demo-ready scanner!
        """
response = self.webhook.send(text=message)

        print(f"✅ Slack alert sent: {response['status']}")

# Test
if __name__ == "__main__":
    notifier = SlackNotifier()
    test_vulns = ["arn:aws:iam::123:policy/PublicRead"]
    notifier.send_iam_alert(test_vulns)
