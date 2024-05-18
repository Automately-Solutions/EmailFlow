import csv
from datetime import datetime

class EmailListManager:
    def __init__(self, csv_file='email_list.csv'):
        self.csv_file = csv_file
        self.email_list = self.load_email_list()

    def load_email_list(self):
        email_list = []
        try:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    email_list.append(row)
        except FileNotFoundError:
            pass  # If the file does not exist, start with an empty list
        return email_list

    def save_email_list(self):
        with open(self.csv_file, mode='w', newline='') as file:
            fieldnames = ["Email address", "Prospect / Customer Name", "User Added", "Emails Sent"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for email_entry in self.email_list:
                writer.writerow(email_entry)

    def add_email(self, email, name):
        new_email = {
            "Email address": email,
            "Prospect / Customer Name": name,
            "User Added": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Emails Sent": 0
        }
        self.email_list.append(new_email)
        self.save_email_list()

    def import_email_list(self, emails):
        for email, name in emails:
            self.add_email(email, name)
        self.save_email_list()

    def get_email_list(self):
        return self.email_list
