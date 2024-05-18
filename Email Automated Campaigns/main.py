import time
import os

from rich import box
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.progress import Progress
from rich.traceback import install

from email_list_manager import EmailListManager
from campaign_manager import Campaign

install(show_locals=True)

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading users...", total=1000)
    task2 = progress.add_task("[green]Writing emails...", total=1000)
    task3 = progress.add_task("[blue]Booting up systems...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=9)
        progress.update(task2, advance=5)
        progress.update(task3, advance=7)
        time.sleep(0.02)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    console = Console()
    console.print("""
    $$$$$$$$\                         $$\ $$\ $$$$$$$$\ $$\                         
    $$  _____|                        \__|$$ |$$  _____|$$ |                        
    $$ |      $$$$$$\$$$$\   $$$$$$\  $$\ $$ |$$ |      $$ | $$$$$$\  $$\  $$\  $$\ 
    $$$$$\    $$  _$$  _$$\  \____$$\ $$ |$$ |$$$$$\    $$ |$$  __$$\ $$ | $$ | $$ |
    $$  __|   $$ / $$ / $$ | $$$$$$$ |$$ |$$ |$$  __|   $$ |$$ /  $$ |$$ | $$ | $$ |
    $$ |      $$ | $$ | $$ |$$  __$$ |$$ |$$ |$$ |      $$ |$$ |  $$ |$$ | $$ | $$ |
    $$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |$$ |$$ |$$ |      $$ |\$$$$$$  |\$$$$$\$$$$  |
    \________|\__| \__| \__| \_______|\__|\__|\__|      \__| \______/  \_____\____/ 
    """)

    console.print("\n[bold]Welcome to EmailFlow! Please select an option:[/bold]\n")
    console.print("1. View Email List")
    console.print("2. Add New Email")
    console.print("3. Import Email List")
    console.print("4. Create Email Campaign")
    console.print("5. Schedule Campaign")
    console.print("6. View Email Log")
    console.print("7. Exit")

    choice = input("\nEnter your choice: ")
    return choice

def view_email_list(manager):
    email_list = manager.get_email_list()
    if email_list:
        print("Current Email List:")
        for email in email_list:
            print(email)
    else:
        print("Email list is empty.")
    input("\nPress Enter to return to the main menu.")

def add_new_email(manager):
    email = input("Enter the new email address: ")
    name = input("Enter the name of the prospect/customer: ")
    manager.add_email(email, name)
    print(f"{email} added to the email list.")
    input("\nPress Enter to return to the main menu.")

def import_email_list(manager):
    emails = ['example1@example.com', 'example2@example.com']
    manager.import_email_list(emails)
    print("Emails imported.")
    input("\nPress Enter to return to the main menu.")

def create_email_campaign(campaign_manager):
    name = input("Enter campaign name: ")
    subject = input("Enter campaign subject: ")
    from_email = input("Enter from email address: ")
    template_id = input("Enter email template ID: ")
    campaign = campaign_manager.create_campaign(name, subject, from_email, template_id)
    print(f"Campaign '{name}' created.")
    input("\nPress Enter to return to the main menu.")

def schedule_campaign(campaign_manager, manager):
    email_list = manager.get_email_list()
    if not email_list:
        print("Email list is empty. Cannot schedule campaign.")
    else:
        campaign_manager.schedule_campaign(campaign_manager.create_campaign(
            name='Scheduled Campaign',
            subject='Your Subject Here',
            from_email='your-email@example.com',
            template_id='your-template-id'
        ), email_list)
        print("Campaign scheduled.")
    input("\nPress Enter to return to the main menu.")

def emails_log():
    print("Sent Emails Log:")
    print("No logs available.")
    input("\nPress Enter to return to the main menu.")

email_list_manager = EmailListManager()
campaign_manager = Campaign('config.yaml')

while True:
    choice = main_menu()
    clear_screen()

    if choice == '1':
        view_email_list(email_list_manager)
    elif choice == '2':
        add_new_email(email_list_manager)
    elif choice == '3':
        import_email_list(email_list_manager)
    elif choice == '4':
        create_email_campaign(campaign_manager)
    elif choice == '5':
        schedule_campaign(campaign_manager, email_list_manager)
    elif choice == '6':
        emails_log()
    elif choice == '7':
        print("Exiting EmailFlow. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to return to the main menu.")
    clear_screen()
