class Restaurant:
  """
  A simple class to represent a restaurant.
  """
  def __init__(self, restaurant_name, cuisine_type):
    """
    Initializes the restaurant with a name and cuisine type.

    Args:
      restaurant_name: The name of the restaurant.
      cuisine_type: The type of cuisine served by the restaurant.
    """
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    """
    Prints a description of the restaurant, including its name and cuisine type.
    """
    print(f"Restaurant name: {self.restaurant_name}")
    print(f"Cuisine type: {self.cuisine_type}")

  def open_restaurant(self):
    """
    Prints a message indicating that the restaurant is open.
    """
    print(f"{self.restaurant_name} is now open!")

# Create an instance of the Restaurant class
restaurant = Restaurant("The Curry House", "Indian")

# Print the restaurant's attributes individually
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call the restaurant's methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
