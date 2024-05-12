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

  # Other methods from previous exercises (open_restaurant, set_number_served, increment_number_served) can be included here

