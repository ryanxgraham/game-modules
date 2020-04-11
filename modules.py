"""Some useful functions methods for making text-based games."""

import os
import time
import random
import termios
import sys

class colors:
    """Colors class."""

    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    flash='\033[05m'
    reverse='\033[07m'
    invisible='\033[08m'
    strikethrough='\033[09m'

    class fg:
        """Foreground color class."""

        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        """Background color class."""

        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def print_pause(text, color=colors.reset, length=1,):
    """
    Print a string of a certtain color and wait a certain amount of time.

    Default wait time 1 second.
    Too print bold red use: colors.fg.red + colors.bold.
    """
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)
    os.system("stty echo")
    print(f"{color}" + text + colors.reset)
    os.system("stty -echo")
    time.sleep(length)


def valid_input(prompt, options, tryagain):
    """
    Validate user input.

    Requires a promt, a list of valid options, and a message for invalid
    """
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause(f"{tryagain}",colors.fg.red, 1)


def replay():
    """Prompt player to play again."""
    choice = valid_input("\nWould you like to play again? y/n\n", ["y", "n"], "Please select 'y' or 'n'")
    yes_list = ["Yeehaw!", "Oh no not again!", "Lets do this!",
                "One more!", "Why does this keep happening to me?"]
    if choice == "y":
        print_pause(random.choice(yes_list), colors.fg.blue, 3)
        play_game()
    elif choice == "n":
        print_pause("Get me out of here!", colors.fg.red, 1)
        print_pause("Thanks for playing!", colors.fg.green, 1)
        sys.exit()

class Zone:
    """Parent class for Zones."""

    def __init__(self, name, description, weather, directions, destinations,
    inventory):
        """Initialize Zone Class."""
        self.name = name
        self.description = description
        self.weather = weather
        self.directions = directions
        self.destinations = destinations
        self.inventory = inventory

    def choose_direction(directions, destinations, inventory):
        """Print inventory and choose a diriection to go."""
        print_pause("\nInventory:", 0)
        print_pause(inventory, colors.bg.black + colors.fg.yellow, .5)
        response = valid_input("\nWhich way would you "
                               "like to go? N/S/E/W:  ", directions,
                               "Please N,S,E, or W").lower()
        if response == "n":
            return destinations[0](inventory)
        elif response == "s":
            return destinations[1](inventory)
        elif response == "e":
            return destinations[2](inventory)
        elif response == "w":
            return destinations[3](inventory)
