# Buffet menu as a tuple (unchangeable)
buffet_foods = ("Pizza", "Pasta", "Chicken", "Salad", "Dessert")

# Printing the menu
print("The buffet offers:")
for food in buffet_foods:
  print(food)

# Trying to modify an item (will result in an error)
# buffet_foods[2] = "Tacos"  # This line will cause an error

# Updating the menu (tuples are immutable, so we create a new one)
revised_menu = ("Burgers", "Pasta", "Fries", "Salad", "Ice Cream")

# Printing the revised menu
print("\nThe revised menu offers:")
for food in revised_menu:
  print(food)
