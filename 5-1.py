age = 25
name = "Alice"
user_logged_in = True

# Test 1 (True): Check if age is greater than 20
print("Is age > 20? I predict True.")
print(age > 20)

# Test 2 (False): Check if name is equal to "Bob"
print("\nIs name == 'Bob'? I predict False.")
print(name == "Bob")

# Test 3 (True): Check if user_logged_in is True
print("\nIs user_logged_in == True? I predict True.")
print(user_logged_in == True)

# Test 4 (False): Check if age is equal to "25" (compares type, not value)
print("\nIs age == '25'? I predict False.")
print(age == "25")

# Test 5 (True): Check if name starts with "Al"
print("\nDoes name start with 'Al'? I predict True.")
print(name.startswith("Al"))

# Test 6 (False): Check if length of name is less than 3 (considers spaces)
print("\nIs length of name < 3? I predict False.")
print(len(name) < 3)

# Test 7 (True): Check if user_logged_in is not False (opposite of True)
print("\nIs user_logged_in is not False? I predict True.")
print(user_logged_in is not False)

# Test 8 (False): Check if age is greater than or equal to 30
print("\nIs age >= 30? I predict False.")
print(age >= 30)

# Test 9 (True): Check if name contains the letter "l" (case-sensitive)
print("\nDoes name contain 'l'? I predict True.")
print("l" in name)

# Test 10 (False): Check if user_logged_in is less than True (boolean not comparable)
print("\nIs user_logged_in < True? I predict False.")
print(user_logged_in < True)
