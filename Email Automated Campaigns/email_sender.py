from mailjet_rest import Client
from rich.panel import Panel
from rich.console import Console
from rich import box

class EmailSender:
    def __init__(self):
        self.api_key = "55567d679bb914cb2db0bd74f246dd5d"  # Default API key
        self.api_secret = "e1114507687414ec0414f895ca890bed"  # Default API secret
        self.sender_email = "raoabdulhadi952@gmail.com"  # Default sender email
        self.mailjet_client = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        self.console = Console()

    def send_email(self, recipient_email, recipient_name):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": self.sender_email,
                        "Name": "EmailFlow Inc."
                    },
                    "To": [
                        {
                            "Email": recipient_email,
                            "Name": recipient_name
                        }
                    ],
                    "Subject": "Test Email campaign - EmailFlow",
                    "TextPart": "EmailFlow Development Campaign",
                    "HTMLPart": "<h3>EmailFlow Test Campaigns</h3><p>Ignore this email.</p>",
                    "CustomID": "AppGettingStartedTest"
                }
            ]
        }
        result = self.mailjet_client.send.create(data=data)
        if result.status_code == 200:
            self.console.print(Panel.fit(f"Email successfully sent to {recipient_email}", border_style="bold green", box=box.SQUARE))
        else:
            self.console.print(Panel.fit(f"Failed to send email to {recipient_email}. Error: {result.json()}", border_style="bold red", box=box.SQUARE))

if __name__ == "__main__":
    sender = EmailSender()
    sender.send_email("test@example.com", "Test Recipient")
