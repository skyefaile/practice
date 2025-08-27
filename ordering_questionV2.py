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


def pizza_selection(user_choice):
    # Output error message / success message
    if pizza_choice == 1:
        user_selection = "Classic Cheese"
        return user_selection
    elif pizza_choice == 2:
        user_selection = "Pepperoni"
        return user_selection
    elif pizza_choice == 3:
        user_selection = "Vegetarian"
        return user_selection
    elif pizza_choice == 4:
        user_selection = "Meat Lovers"
        return user_selection
    elif pizza_choice == 5:
        user_selection = "Hawaiian"
        return user_selection
    elif pizza_choice == 6:
        user_selection = "BBQ Chicken"
        return user_selection
    elif pizza_choice == 7:
        user_selection = "Ham and Cheese"
        return user_selection
    elif pizza_choice == 8:
        user_selection = "Buffalo Chicken"
        return user_selection
    elif pizza_choice == 9:
        user_selection = "Supreme"
        return user_selection
    else:
        return "Pesto"

# Main Routine goes here


# loop for testing purposes...
while True:
    print()

    # ask user for an integer
    pizza_choice = int_check("Choose a pizza from the menu (1-10): ", 1, 10)

    pizza_selected = pizza_selection(pizza_choice)

    print(f"You chose {pizza_selected}")
