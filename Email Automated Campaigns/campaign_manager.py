import csv
from datetime import datetime
from rich.table import Table
from rich.console import Console

class CampaignManager:
    def __init__(self):
        self.campaigns = []
        self.load_campaign_log()

    def create_campaign(self, name, subject, from_email, template_id, description):
        campaign = {
            "Name": name,
            "Subject": subject,
            "From Email": from_email,
            "Template ID": template_id,
            "Description": description,
            "Start Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.campaigns.append(campaign)
        self.save_campaign_log()  # Save the campaign log after creating a new campaign
        return campaign

    def save_campaign_log(self):
        with open('campaign_log.csv', mode='w', newline='') as file:
            fieldnames = ["Name", "Subject", "From Email", "Template ID", "Description", "Start Date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for campaign in self.campaigns:
                writer.writerow(campaign)

    def load_campaign_log(self):
        try:
            with open('campaign_log.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.campaigns.append(row)
        except FileNotFoundError:
            pass  # No existing log file, initialize with an empty list

    def view_campaigns(self):
        if self.campaigns:
            table = Table(title="Campaign Log")
            table.add_column("Name", justify="left")
            table.add_column("Subject", justify="left")
            table.add_column("From Email", justify="left")
            table.add_column("Template ID", justify="left")
            table.add_column("Description", justify="left")
            table.add_column("Start Date", justify="left")
            for campaign in self.campaigns:
                table.add_row(
                    campaign["Name"],
                    campaign["Subject"],
                    campaign["From Email"],
                    campaign["Template ID"],
                    campaign["Description"],
                    campaign["Start Date"]
                )
            console = Console()
            console.print(table)
        else:
            print("No campaigns found in the log.")

    def get_campaign(self, name):
        for campaign in self.campaigns:
            if campaign["Name"] == name:
                return campaign
        return None