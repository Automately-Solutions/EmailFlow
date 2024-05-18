import os
from mailjet_rest import Client
from rich.panel import Panel
from rich.console import Console
from rich import box

class EmailSender:
    def __init__(self):
        self.api_key = os.getenv('MAILJET_API_KEY')
        self.api_secret = os.getenv('MAILJET_API_SECRET')
        self.mailjet_client = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        self.console = Console()

    def send_email(self, recipient_email, recipient_name):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "wordsmithscripts@gmail.com",
                        "Name": "WordSmith Corp."
                    },
                    "To": [
                        {
                            "Email": recipient_email,
                            "Name": recipient_name
                        }
                    ],
                    "Subject": "Unlocking Potential with WordSmith Agency",
                    "TextPart": "Greetings, We've noticed your potential and we're excited to offer our services to help elevate your business. Let's connect for a transformative collaboration.",
                    "HTMLPart": "<h3>Ready to Elevate Your Business?</h3><p>We at WordSmith Agency are thrilled at the prospect of working with you. Let's make something great together.</p>",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        result = self.mailjet_client.send.create(data=data)
        if result.status_code == 200:
            self.console.print(Panel.fit(f"Email successfully sent to {recipient_email}", border_style="bold green", box=box.SQUARE))
        else:
            self.console.print(Panel.fit(f"Failed to send email to {recipient_email}. Error: {result.json()}", border_style="bold red", box=box.SQUARE))
