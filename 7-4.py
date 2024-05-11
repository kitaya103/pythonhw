toppings = []

while True:
  topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()

  if topping == 'quit':
    break

  toppings.append(topping)
#   print(f"Adding {topping} to your pizza.")

if toppings:
  print("Your pizza will have:")
  for topping in toppings:
    print(f"- {topping}")
else:
  print("You didn't choose any toppings.")
