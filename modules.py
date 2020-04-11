
def print_pause(text, length=1):
    """Print a string and wait a certain amount of time. 1s default."""
    print(text)
    time.sleep(length)


def valid_input(prompt, options, tryagain):
    """Validate user input."""
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause(f"{tryagain}", 1)


def replay():
    """Prompt player to play again."""
    choice = valid_input("\nWould you like to play again? y/n\n", ["y", "n"])
    yes_list = ["Yeehaw!", "Oh no not again!", "Lets do this!",
                "One more turn!", "Why does this keep happening to me?"]
    if choice == "y":
        print_pause(random.choice(yes_list), 3)
        play_game()
    elif choice == "n":
        print_pause("Get me out of here!", 1)
        print_pause("Thanks for playing!", 1)
        sys.exit()
