class Restaurant:
  """
  A simple class to represent a restaurant with customer tracking.
  """
  def __init__(self, restaurant_name, cuisine_type):
    """
    Initializes the restaurant with a name, cuisine type, and number served.

    Args:
      restaurant_name: The name of the restaurant.
      cuisine_type: The type of cuisine served by the restaurant.
    """
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    """
    Prints a description of the restaurant, including its name, cuisine type, and number served.
    """
    print(f"Restaurant name: {self.restaurant_name}")
    print(f"Cuisine type: {self.cuisine_type}")
    print(f"Customers served: {self.number_served}")

  def open_restaurant(self):
    """
    Prints a message indicating that the restaurant is open.
    """
    print(f"{self.restaurant_name} is now open!")

  def set_number_served(self, served):
    """
    Sets the number of customers served to a new value.

    Args:
      served: The new number of customers served.
    """
    self.number_served = served

  def increment_number_served(self, customers):
    """
    Increments the number of customers served by a given amount.

    Args:
      customers: The number of additional customers served.
    """
    self.number_served += customers

# Create an instance of the Restaurant class
restaurant = Restaurant("The Curry House", "Indian")

# Print the initial number of customers served
print(f"Customers served: {restaurant.number_served}")

# Change the number served directly
restaurant.number_served = 10
print(f"Customers served (after change): {restaurant.number_served}")

# Use the set_number_served method
restaurant.set_number_served(25)
print(f"Customers served (after set_number_served): {restaurant.number_served}")

# Use the increment_number_served method (simulate a day's business)
restaurant.increment_number_served(50)
print(f"Customers served (after increment_number_served): {restaurant.number_served}")
