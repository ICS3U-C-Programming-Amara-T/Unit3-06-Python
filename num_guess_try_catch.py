#!/usr/bin/env python3

# Created By: Amara Tie

# Date: March 27, 2025

# This program is a game to guess a number


def main():
    # Ask User for a number
    number_as_string = input("Enter a number:")
    print("")

    # Check if the number_as_string is a number
    try:
        number_as_number = int(number_as_string)
        print("You entered the right number!")
    except Exception:
        print("This is not a number")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
