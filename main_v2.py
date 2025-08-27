# Importing packages
import pandas

import numpy as np


# Pizza Price List
ONE_PRICE = 7.50
TWO_PRICE = 7.50
THREE_PRICE = 7.50
FOUR_PRICE = 7.50
FIVE_PRICE = 7.50
SIX_PRICE = 7.50
SEVEN_PRICE = 7.50
EIGHT_PRICE = 7.50
NINE_PRICE = 7.50
TEN_PRICE = 7.50


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and the end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def int_check(question, low, high):
    """Checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def pizza_selection(user_choice):
    # Output error message / success message
    if pizza_choice == 1:
        user_selection = "Classic Cheese"
        pizza_cost = ONE_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 2:
        user_selection = "Pepperoni"
        pizza_cost = TWO_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 3:
        user_selection = "Vegetarian"
        pizza_cost = THREE_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 4:
        user_selection = "Meat Lovers"
        pizza_cost = FOUR_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 5:
        user_selection = "Hawaiian"
        pizza_cost = FIVE_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 6:
        user_selection = "BBQ Chicken"
        pizza_cost = SIX_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 7:
        user_selection = "Ham and Cheese"
        pizza_cost = SEVEN_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 8:
        user_selection = "Buffalo Chicken"
        pizza_cost = EIGHT_PRICE
        return user_selection, pizza_cost
    elif pizza_choice == 9:
        user_selection = "Supreme"
        pizza_cost = NINE_PRICE
        return user_selection, pizza_cost
    else:
        pizza_cost = TEN_PRICE
        print(f"You chose Pesto")


def topping_selection(user_choice):
    # Output error message / success message
    if topping_choice == 1:
        user_selection = "Extra Cheese"
        return user_selection
    elif topping_choice == 2:
        user_selection = "Bacon"
        return user_selection
    elif topping_choice == 3:
        user_selection = "Chicken"
        return user_selection
    elif topping_choice == 4:
        user_selection = "Mushrooms"
        return user_selection
    elif topping_choice == 5:
        user_selection = "BBQ Sauce"
        return user_selection
    elif topping_choice == 6:
        user_selection = "Capsicum"
        return user_selection
    elif topping_choice == 7:
        user_selection = "Ham"
        return user_selection
    elif topping_choice == 8:
        user_selection = "Basil"
        return user_selection
    elif topping_choice == 9:
        user_selection = "Chilli"
        return user_selection
    else:
        return "Pineapple"


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine goes here

# Initialise ticket numbers
MAX_PIZZAS = 5
pizzas_sold = 0

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_pizza_selected = []
all_pizza_price = []
all_surcharges = []

pizza_order_dict = {
    'Pizza Choice': all_pizza_selected,
    'Pizza Price': all_pizza_price,
    'Surcharge': all_surcharges
}

# Program main heading
make_statement("Welcome to The Pizza Place!", "🍕")

# Ask user if they want to see the instructions
# Display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# ask user for their name (and check it's not blank)
name = not_blank("Name: ")


# loop to order pizza
while pizzas_sold < MAX_PIZZAS:

    # display menu
    # Creating menu
    all_pizza_options = ["Classic Cheese", "Pepperoni", "Vegetarian", "Meat Lovers", "Hawaiian",
                         "BBQ Chicken", "Ham and Cheese", "Buffalo Chicken", "Supreme", "Pesto"]
    all_pizza_price = [7.50, 8.00, 7.00, 8.00, 8.00, 9.50, 8.00, 9.50, 10.50, 7.50]

    pizza_place_dict = {
        'Pizza Options': all_pizza_options,
        'Price': all_pizza_price,
    }

    # create dataframe / table from dictionary
    pizza_place_frame = pandas.DataFrame(pizza_place_dict)

    # Rearranging index
    pizza_place_frame.index = np.arange(1, len(pizza_place_frame) + 1)

    print("MENU")
    print(pizza_place_frame)
    print()

    # pizza selection
    # ask user for an integer
    pizza_choice = int_check("Choose a pizza from the menu (1-10): ", 1, 10)

    pizza_selected, pizza_price = pizza_selection(pizza_choice)

    print(f"You chose {pizza_selected} cost: ${pizza_price}")

    # Creating menu
    all_topping_options = ["Extra Cheese", "Bacon", "Chicken", "Mushrooms", "BBQ Sauce",
                           "Capsicum", "Ham", "Basil", "Chilli", "Pineapple"]
    all_topping_price = [7.50, 8.00, 7.00, 8.00, 8.00, 9.50, 8.00, 9.50, 10.50, 7.50]

    topping_dict = {
        'Toppings': all_topping_options,
        'Price': all_topping_price,
    }

    # create dataframe / table from dictionary
    topping_frame = pandas.DataFrame(topping_dict)

    # Rearranging index
    topping_frame.index = np.arange(1, len(topping_frame) + 1)

    # Ask user if they want toppings

    print()
    want_toppings = string_check("Do you want toppings? ")

    if want_toppings == "yes":
        print(topping_frame)

        topping_choice = int_check("Choose a topping from the menu (1-10): ", 1, 10)

        topping_selected = topping_selection(topping_choice)

        print(f"You chose {topping_selected}")

    print()

    pizzas_sold += 1

    # loop details
    if pizzas_sold == 5:
        break

    want_pizza = string_check("Would you like to order another pizza? ")
    if want_pizza == "yes":
        continue
    else:
        break