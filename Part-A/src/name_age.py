"""TODO: Replace with a one-line summary of the program's purpose (<73 chars).

Input:
    
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))

Process:
    current_year = datetime.datetime.now().year
  birth_year = current_year - user_age

Output:
    print(f"\nHello {user_name}! You were born in {birth_year}.")

Typical usage example:
  What is your name? Alex
How old are you?24
    Hello Alex! You were born in 2001.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))
 current_year = datetime.datetime.now().year
  birth_year = current_year - user_age
 print(f"\nHello {user_name}! You were born in {birth_year}.")



# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

