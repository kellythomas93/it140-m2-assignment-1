"""TODO: Replace with a one-line summary of the program's purpose (<73 chars).

Input:
      import datetime


def main():
    name = input("What is your name? ")
    age_input = input("How old are you? ")

    age = int(age_input)
    current_year = datetime.datetime.now().year

Process:
    birth_year = current_year - age

Output:
print(f"\nHello {name}! You were born in {birth_year}.")

Typical usage example:
    TODO: Replace with the input prompt and original name-input example.
    TODO: Replace with the input prompt and original age-input example.
    TODO: Replace with the resulting output from those inputs.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    name = input("What is your name?")
    age_input = input("How old are you?")P

    age = int(age_input)
    current_year = date.datetime.noe().year
    birth_year = current_year - age
    print(f"\nHellp {name}! You were boen in {birth_year}.")




# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
