def print_models(unprinted_designs, completed_models):
  """
  Simulates printing each design until no unprinted designs remain.
  Moves each design to the completed list after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Prints a message listing all completed models."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)
