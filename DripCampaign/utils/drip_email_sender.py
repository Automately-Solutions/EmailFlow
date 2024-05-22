import os
from mailjet_rest import Client
from rich.console import Console
from rich.panel import Panel
from rich import box

class EmailSender:
    def __init__(self):
        self.api_key = 'MAILJET_API_KEY'
        self.api_secret = 'MAILJET_SECRET_KEY'
        self.mailjet_client = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        self.console = Console()

    def send_email(self, recipient_email, recipient_name, campaign_type):
        # Example email contents for different campaigns
        campaigns = {
            "Win-back Campaign": {
                "Subject": "We Miss You!",
                "TextPart": f"Dear {recipient_name}, we noticed you unsubscribed. We miss you! Here’s a special offer to welcome you back.",
                "HTMLPart": f"<h3>Dear {recipient_name},</h3><p>We noticed you unsubscribed. We miss you! Here’s a special offer to welcome you back.</p>"
            },
            "Cross-Selling Campaign": {
                "Subject": "Check Out These Offers!",
                "TextPart": f"Dear {recipient_name}, based on your recent purchase, we thought you might like these additional products.",
                "HTMLPart": f"<h3>Dear {recipient_name},</h3><p>Based on your recent purchase, we thought you might like these additional products.</p>"
            },
            "Cart Abandonment Campaign": {
                "Subject": "Complete Your Purchase",
                "TextPart": f"Dear {recipient_name}, it looks like you left something in your cart. Complete your purchase now!",
                "HTMLPart": f"<h3>Dear {recipient_name},</h3><p>It looks like you left something in your cart. Complete your purchase now!</p>"
            },
            "Welcome Drip Campaign": {
                "Subject": "Welcome to The Network!",
                "TextPart": f"Dear {recipient_name}, welcome to The Network! We’re excited to have you on board.",
                "HTMLPart": f"<h3>Dear {recipient_name},</h3><p>Welcome to The Network! We’re excited to have you on board.</p>"
            }
        }

        if campaign_type not in campaigns:
            return "Error: Unknown campaign type."

        campaign = campaigns[campaign_type]
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "raoabdulhadi952@gmail.com",
                        "Name": "The Network"
                    },
                    "To": [
                        {
                            "Email": recipient_email,
                            "Name": recipient_name
                        }
                    ],
                    "Subject": campaign["Subject"],
                    "TextPart": campaign["TextPart"],
                    "HTMLPart": campaign["HTMLPart"],
                    "CustomID": campaign_type
                }
            ]
        }
        result = self.mailjet_client.send.create(data=data)
        if result.status_code == 200:
            self.console.print(Panel.fit(f"Email successfully sent to {recipient_email}", border_style="bold green", box=box.SQUARE))
            return "Success"
        else:
            self.console.print(Panel.fit(f"Failed to send email to {recipient_email}. Error: {result.json()}", border_style="bold red", box=box.SQUARE))
            return "Failed"

