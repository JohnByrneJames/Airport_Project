from string import ascii_letters, digits

username = input("NAME ")
try:
    if 0 < len(username) < 3 or len(username) > 5:  # User has left blank and submitted or put less than 3 characters
        raise ValueError("⚠ You cannot leave the field blank/ username is always longer than 3 characters ⚠ ")
except ValueError as e:
    exit("Exiting, please retry from the main menu.")