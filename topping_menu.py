# Importing packages
import pandas

import numpy as np

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

print("Extra Toppings")
print(topping_frame)
print()
