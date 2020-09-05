# type: ignore[attr-defined]

import random
from enum import Enum
from typing import Optional

import typer
from rich.console import Console

from test_template import __version__
from test_template.example import bye, hello


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


class Greeting(str, Enum):
    hello = "hello"
    bye = "bye"


app = typer.Typer(
    name="test-template",
    help="Awesome `test-template` is a Python cli/package created with https://github.com/TezRomacH/python-package-template",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(
            f"[yellow]test-template[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Name of person to greet."),
    greeting: str = typer.Option(
        ..., case_sensitive=False, help="Type of Greeting"
    ),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for name. If not specified then choice will be random.",
    ),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the test-template package.",
    ),
):
    """Prints a greeting for a giving name."""
    if color is None:
        # If no color specified use random value from `Color` class
        color = random.choice(list(Color.__members__.values()))
    if greeting == "hello":
        greeting: str = hello(name)
    else:
        greeting: str = bye(name)
    console.print(f"[bold {color}]{greeting}[/]")
