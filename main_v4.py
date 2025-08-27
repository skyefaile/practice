# Importing packages
import pandas

import numpy as np

# Pizza Price List
ONE_PRICE = 7.50
TWO_PRICE = 8.00
THREE_PRICE = 7.00
FOUR_PRICE = 8.00
FIVE_PRICE = 8.00
SIX_PRICE = 9.50
SEVEN_PRICE = 8.00
EIGHT_PRICE = 9.50
NINE_PRICE = 10.50
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

    error = f"Oops - please enter an integer from {low} and {high}."

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
        pizza_choice == 10
        user_selection = "Pesto"
        pizza_cost = TEN_PRICE
        return user_selection, pizza_cost

def topping_selection(user_choice):
    # Output error message / success message
    if topping_choice == 1:
        user_selection = "Extra Cheese"
        topping_cost = 2.00
        return user_selection, topping_cost
    elif topping_choice == 2:
        user_selection = "Bacon"
        topping_cost = 3.00
        return user_selection, topping_cost
    elif topping_choice == 3:
        user_selection = "Chicken"
        topping_cost = 3.00
        return user_selection, topping_cost
    elif topping_choice == 4:
        user_selection = "Mushrooms"
        topping_cost = 2.00
        return user_selection, topping_cost
    elif topping_choice == 5:
        user_selection = "BBQ Sauce"
        topping_cost = 1.00
        return user_selection, topping_cost
    elif topping_choice == 6:
        user_selection = "Capsicum"
        topping_cost = 2.00
        return user_selection, topping_cost
    elif topping_choice == 7:
        user_selection = "Ham"
        topping_cost = 3.00
        return user_selection, topping_cost
    elif topping_choice == 8:
        user_selection = "Basil"
        topping_cost = 0.50
        return user_selection, topping_cost
    elif topping_choice == 9:
        user_selection = "Chilli"
        topping_cost = 0.50
        return user_selection, topping_cost
    else:
        user_selection = "Pineapple"
        topping_cost = 2.00
        return user_selection, topping_cost


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine goes here

# Initialise ticket numbers
MAX_PIZZAS = 5
pizzas_sold = 0

total = 0

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')
confirmation_ans = ('confirm', 'cancel')

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold pizza order details
all_pizza_selected = []
all_pizza_selected_price = []
all_topping_selected = []
all_topping_selected_price = []
all_surcharges = []

pizza_order_dict = {
    'Pizza Choice': all_pizza_selected,
    'Pizza Price': all_pizza_selected_price,
    'Topping Choice': all_topping_selected,
    'Topping Price': all_topping_selected_price
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
    all_topping_price = [2.00, 3.00, 3.00, 2.00, 1.00, 2.00, 3.00, 0.50, 0.50, 2.00]

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

        topping_selected, topping_price = topping_selection(topping_choice)

        print(f"You chose {topping_selected} ${topping_price}")

        all_topping_selected.append(topping_selected)
        all_topping_selected_price.append(topping_price)
    else:
        all_topping_selected.append('No topping')
        all_topping_selected_price.append(0)

    print()

    # add pizza, pizza price, topping & topping price to lists
    all_pizza_selected.append(pizza_selected)
    all_pizza_selected_price.append(pizza_price)

    pizzas_sold += 1

    # loop details
    if pizzas_sold == 5:
        break

    want_pizza = string_check("Would you like to order another pizza? ")
    if want_pizza == "yes":
        continue
    else:
        break


# create dataframe / table from dictionary
pizza_order_frame = pandas.DataFrame(pizza_order_dict)
# Rearranging index
pizza_order_frame.index = np.arange(1, len(pizza_order_frame) + 1)
print(pizza_order_frame)

# calculating total
total = pizza_order_frame['Pizza Price'].sum() + pizza_order_frame['Topping Price'].sum()

print(f"Total: ${total}")


# ask user for payment method (cash / credit / ca / cr)
pay_method = string_check("Payment method: ", payment_ans, 2)
if pay_method == "cash":
    surcharge = 0
    end_total = total
    print("You chose cash")
    print(f"Total cost: ${total}")

# if paying by credit, calculate surcharge
else:
    surcharge = total * CREDIT_SURCHARGE
    end_total = surcharge + total
    print("You chose credit")
    print(f"Surcharge: ${surcharge}")
    print(f"Total cost: ${end_total}")


# confirm order
print(pizza_order_frame)
print(f"Total cost: ${end_total}")

confirmation = string_check("Would you like to confirm or cancel your order? ", confirmation_ans, 2)
if confirmation == 'cancel':
    cancel_ans = string_check("Are you sure? ")
    if cancel_ans == 'yes':
        exit()
