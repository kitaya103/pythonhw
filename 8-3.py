def make_shirt(size, message):
  """Prints a summary of the shirt size and message."""
  print(f"I'm going to make a {size} t-shirt with the message: {message}")

# Positional arguments
make_shirt('large', 'I love Python!')

# Keyword arguments
make_shirt(message='Eat, sleep, code.', size='medium')
