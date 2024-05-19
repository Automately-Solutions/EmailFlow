import csv
from datetime import datetime

class EmailListManager:
    def __init__(self, filename='email_list.csv'):
        self.filename = filename
        self.email_list = []
        self.load_email_list()

    def load_email_list(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.email_list = list(reader)
        except FileNotFoundError:
            pass

    def get_email_list(self):
        return self.email_list

    def add_email(self, email, name):
        entry = {
            "Email address": email,
            "Prospect / Customer Name": name,
            "User added": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Emails sent": 0
        }
        self.email_list.append(entry)
        self.save_email_list()

    def import_email_list(self, emails):
        for email, name in emails:
            self.add_email(email, name)

    def save_email_list(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ["Email address", "Prospect / Customer Name", "User added", "Emails sent"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.email_list)
    
    def increment_email_count(self, email_address):
        for email in self.email_list:
            if email["Email address"] == email_address:
                old_count = email["Emails sent"]
                email["Emails sent"] = str(int(email["Emails sent"]) + 1)
                new_count = email["Emails sent"]
                print(f"Updated email count for {email_address}: {old_count} -> {new_count}")  # Debug print
                break
