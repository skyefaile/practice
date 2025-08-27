# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and the end"""

    return(f"{decoration * 3} {statement} {decoration * 3}")

def string_check(question, valid_answers=['yes', 'no'],
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def instructions():
    print(make_statement("Instructions", "-"))

    print('''

You can order up to 5 pizzas. Each pizza can have extra toppings. You can also order sides.

If using a card, a surcharge of 5% will be applied.

if you want your pizza to be delivered there will be an extra $5. You will also need to enter your address.

    ''')


# Ask user if they want to see the instructions
# Display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()