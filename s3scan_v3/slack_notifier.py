import os
import json
import logging
from typing import Dict, Any

import requests


class SlackNotifier:
    def __init__(self, webhook_url: str | None = None) -> None:
        self.webhook_url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")
        if not self.webhook_url:
            raise ValueError("SLACK_WEBHOOK_URL is not set")

    def _build_payload(self, title: str, message: str, severity: str) -> Dict[str, Any]:
        color = {
            "INFO": "#36a64f",
            "LOW": "#36a64f",
            "MEDIUM": "#ffae42",
            "HIGH": "#ff0000",
            "CRITICAL": "#8B0000",
        }.get(severity.upper(), "#36a64f")

        return {
            "attachments": [
                {
                    "fallback": f"{title}: {message}",
                    "color": color,
                    "title": title,
                    "text": message,
                    "mrkdwn_in": ["text", "pretext"],
                }
            ]
        }

    def send_alert(self, title: str, message: str, severity: str = "INFO") -> Dict[str, Any]:
        payload = self._build_payload(title, message, severity)
        try:
            resp = requests.post(
                self.webhook_url,
                data=json.dumps(payload),
                headers={"Content-Type": "application/json"},
                timeout=5,
            )
            resp.raise_for_status()
            logging.info("Slack alert sent: %s", resp.status_code)
            print(f"✅ Slack alert sent: {resp.status_code}")
            return {"status": "ok", "code": resp.status_code}
        except Exception as exc:
            logging.error("Failed to send Slack alert: %s", exc)
            print(f"❌ Failed to send Slack alert: {exc}")
            return {"status": "error", "error": str(exc)}
