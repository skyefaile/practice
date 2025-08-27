# Functions go here
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


def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


# Main Routine goes here

# loop for testing purposes...
while True:
    print()

    want_toppings = yes_no("Do you want a topping? ")

    # ask user for an integer
    topping_choice = int_check("Choose a topping from the menu (1-10): ", 1, 10)

    topping_selected = topping_selection(topping_choice)

    print(f"You chose {topping_selected}")
