"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False

    password_count=len([letter for letter in password])
    count_lower = len([letter for letter in password if letter.islower()])
    count_upper = len([letter for letter in password if letter.isupper()])
    count_digit = len([letter for letter in password if letter.isdigit()])
    count_special = len([char for char in password if char in SPECIAL_CHARACTERS])
    if password_count > MAX_LENGTH or password_count < MIN_LENGTH  or count_lower < 1 or count_upper <1 or count_digit <1 or count_special <1:
        return False
    else:
        return True
        # TODO: count each kind of character (use str methods like isdigit)
        pass

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True

main()
