import os
import time
from datetime import datetime

from rich import box
from rich import text
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout

from rich.traceback import install
install(show_locals=True)

layout = Layout()

layout.split_column(
    Layout(name="header", size=3),
    Layout(name="body"),
    Layout(name="footer", size=3)
)

layout["body"].split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

layout["upper"].split_row(
    Layout(name="left_upper"),
    Layout(name="right_upper")
)

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand = True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")

        grid.add_row("📩", "[b]EmailFlow[/]", datetime.now().ctime().replace(":", "[blink]:[/]"))

        return Panel(grid, style = "Bold white on Black")

class Footer:
    def __rich__(self) -> Panel:
        f_grid = Table.grid(expand=True)
        f_grid.add_column(justify="left")
        f_grid.add_column(justify="center")
        f_grid.add_column(justify="right")

        f_grid.add_row("🧠", "[b]Email Marketing Campaign Automation Software", "📑")

        return Panel(f_grid, style = "Bold white on black")

layout["header"].update(Header())
layout["footer"].update(Footer())

print(layout)