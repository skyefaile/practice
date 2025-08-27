# Importing packages
import pandas

import numpy as np

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
