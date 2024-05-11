def make_sandwich(*ingredients):
  """Prints a summary of the sandwich being ordered."""
  print("\nI'm making a sandwich with:")
  for ingredient in ingredients:
    print(f"- {ingredient}")

# Call the function with different numbers of arguments
make_sandwich('bread', 'cheese', 'turkey')
make_sandwich('roast beef', 'mustard')
make_sandwich('hummus', 'spinach', 'tomato')
