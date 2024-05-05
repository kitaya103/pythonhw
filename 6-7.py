person_1 = {
    "first_name": "Alice",
    "last_name": "Smith",
    "age": 30,
    "city": "New York"
}

person_2 = {
    "first_name": "Bob",
    "last_name": "Johnson",
    "age": 25,
    "city": "Los Angeles"
}

person_3 = {
    "first_name": "Charlie",
    "last_name": "Williams",
    "age": 40,
    "city": "Chicago"
}

people = [person_1, person_2, person_3]

# Printing information about each person
for person in people:
  print(f"\nFirst Name: {person['first_name']}")
  print(f"Last Name: {person['last_name']}")
  print(f"Age: {person['age']}")
  print(f"City: {person['city']}")
