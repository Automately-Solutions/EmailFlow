import time
import os

from rich import text
from rich import box
#from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading users...", total=1000)
    task2 = progress.add_task("[green]Writing emails...", total=1000)
    task3 = progress.add_task("[blue]Booting up systems...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=5)
        progress.update(task2, advance=5)
        progress.update(task3, advance=5)
        time.sleep(0.02)
        
def clear_screen():
    os.system('cls')  # For Windows

# Clear the screen
clear_screen()

print("""
$$$$$$$$\                         $$\ $$\ $$$$$$$$\ $$\                         
$$  _____|                        \__|$$ |$$  _____|$$ |                        
$$ |      $$$$$$\$$$$\   $$$$$$\  $$\ $$ |$$ |      $$ | $$$$$$\  $$\  $$\  $$\ 
$$$$$\    $$  _$$  _$$\  \____$$\ $$ |$$ |$$$$$\    $$ |$$  __$$\ $$ | $$ | $$ |
$$  __|   $$ / $$ / $$ | $$$$$$$ |$$ |$$ |$$  __|   $$ |$$ /  $$ |$$ | $$ | $$ |
$$ |      $$ | $$ | $$ |$$  __$$ |$$ |$$ |$$ |      $$ |$$ |  $$ |$$ | $$ | $$ |
$$$$$$$$\ $$ | $$ | $$ |\$$$$$$$ |$$ |$$ |$$ |      $$ |\$$$$$$  |\$$$$$\$$$$  |
\________|\__| \__| \__| \_______|\__|\__|\__|      \__| \______/  \_____\____/ 
""")

time.sleep(50)


