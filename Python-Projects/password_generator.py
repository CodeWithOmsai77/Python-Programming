"""Generate a password with Python's secure random module."""

import secrets
import string


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer y or n.")


def main():
    try:
        length = int(input("Password length (8-128): "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if not 8 <= length <= 128:
        print("Choose a length from 8 to 128.")
        return

    pools = [string.ascii_lowercase, string.ascii_uppercase]
    if ask_yes_no("Include digits?"):
        pools.append(string.digits)
    if ask_yes_no("Include symbols?"):
        pools.append(string.punctuation)

    if length < len(pools):
        print("Password length is too short for the selected character groups.")
        return

    # Choose at least one character from each selected group.
    password_chars = [secrets.choice(pool) for pool in pools]
    all_characters = "".join(pools)

    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password_chars)
    print("\nGenerated password:")
    print("".join(password_chars))


if __name__ == "__main__":
    main()
