# Functions go here

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


# Main Routine goes here

while True:
    print()

    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")