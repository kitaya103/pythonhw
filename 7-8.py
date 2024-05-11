sandwich_orders = ["Tuna sandwich", "Chicken salad sandwich", "BLT", "Ham and cheese"]
finished_sandwiches = []

for sandwich in sandwich_orders:
  print(f"I made your {sandwich}.")
  finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
