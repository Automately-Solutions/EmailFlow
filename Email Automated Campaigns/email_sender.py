import os
from mailjet_rest import Client
from rich.panel import Panel
from rich.console import Console
from rich import box

class EmailSender:
    def __init__(self):
        self.api_key = 'MAILJET_API_KEY'
        self.api_secret = 'MAILJET_SECRET_KEY'
        self.mailjet_client = Client(auth=(self.api_key, self.api_secret), version='v3.1')
        self.console = Console()

    def send_email(self, recipient_email, recipient_name, campaign):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": campaign["From Email"],
                        "Name": "EmailFlow Inc."
                    },
                    "To": [
                        {
                            "Email": recipient_email,
                            "Name": recipient_name
                        }
                    ],
                    "Subject": campaign["Subject"],
                    "TextPart": f"{campaign['Description']}\n\n{campaign['Subject']}",
                    "HTMLPart": f"<h3>{campaign['Subject']}</h3><p>{campaign['Description']}</p>",
                    "CustomID": campaign["Name"]
                }
            ]
        }
        result = self.mailjet_client.send.create(data=data)
        if result.status_code == 200:
            self.console.print(Panel.fit(f"Email successfully sent to {recipient_email}", border_style="bold green", box=box.SQUARE))
        else:
            self.console.print(Panel.fit(f"Failed to send email to {recipient_email}. Error: {result.json()}", border_style="bold red", box=box.SQUARE))
