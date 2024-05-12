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

class IceCreamStand(Restaurant):
  """
  An ice cream stand that inherits from the Restaurant class.
  """
  def __init__(self, restaurant_name, cuisine_type="ice cream"):
    """
    Initializes the ice cream stand with a name and sets cuisine type to ice cream by default.

    Args:
      restaurant_name: The name of the ice cream stand.
    """
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = []
    

  def display_flavors(self):
    """
    Prints a list of the ice cream flavors offered by the stand.
    """
    print(f"{self.restaurant_name} offers the following flavors:")
    for flavor in self.flavors:
      print(f"- {flavor}")

# Create an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Cool Cones")

# Add some flavors to the list
ice_cream_stand.flavors = ["chocolate", "strawberry", "mint chip"]

# Call the method to display flavors
ice_cream_stand.display_flavors()
