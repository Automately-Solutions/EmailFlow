import csv
import random
from utils.email_sender import EmailSender

email_list_file = 'data/email_list.csv'
campaign_logs_file = 'data/campaign_logs.csv'

def load_email_list(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def save_campaign_log(file_path, logs):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Campaign_Type", "Status"])
        for log in logs:
            writer.writerow(log)

def send_drip_campaign(email_list, campaign_type, email_sender):
    logs = []
    for entry in email_list:
        email = entry["Email"]
        name = entry["Name"]
        status = email_sender.send_email(email, name, campaign_type)
        logs.append([email, campaign_type, status])
    save_campaign_log(campaign_logs_file, logs)

def main():
    email_sender = EmailSender()
    email_list = load_email_list(email_list_file)

    print("Choose a Drip Campaign to Send:")
    print("1. Win-back Campaign")
    print("2. Cross-Selling Campaign")
    print("3. Cart Abandonment Campaign")
    print("4. Welcome Drip Campaign")

    choice = input("Enter the number of the campaign you want to send: ")

    if choice == '1':
        campaign_type = "Win-back Campaign"
        filtered_email_list = [entry for entry in email_list if entry["Status"] == "Unsubscribed"]
    elif choice == '2':
        campaign_type = "Cross-Selling Campaign"
        filtered_email_list = [entry for entry in email_list if entry["Status"] == "Active"]
    elif choice == '3':
        campaign_type = "Cart Abandonment Campaign"
        filtered_email_list = [entry for entry in email_list if entry["Status"] == "Cart Abandoned"]
    elif choice == '4':
        campaign_type = "Welcome Drip Campaign"
        filtered_email_list = [entry for entry in email_list if entry["Status"] == "New"]
    else:
        print("Invalid choice.")
        return

    if not filtered_email_list:
        print(f"No recipients found for {campaign_type}.")
        return

    send_drip_campaign(filtered_email_list, campaign_type, email_sender)
    print(f"{campaign_type} emails have been sent.")

if __name__ == "__main__":
    main()
