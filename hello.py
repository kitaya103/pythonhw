# Travel destinations (not alphabetical order)
travel_wishlist = ["Japan", "Italy", "New Zealand", "Peru", "Iceland"]

# Print original list
print("Original List:", travel_wishlist)

# Print sorted list (without modifying original)
print("Alphabetical Order (sorted):", sorted(travel_wishlist))

# Print original list again (unchanged)
print("Original List (unchanged):", travel_wishlist)

# Print reverse alphabetical order (sorted)
print("Reverse Alphabetical Order (sorted):", sorted(travel_wishlist, reverse=True))

# Print original list again (unchanged)
print("Original List (unchanged):", travel_wishlist)

# Reverse list order
travel_wishlist.reverse()
print("Reversed List:", travel_wishlist)

# Reverse list order again (back to original)
travel_wishlist.reverse()
print("Original Order Restored:", travel_wishlist)

# Sort list in alphabetical order (modifies original)
travel_wishlist.sort()
print("Sorted List (Alphabetical):", travel_wishlist)

# Sort list in reverse alphabetical order (modifies original)
travel_wishlist.sort(reverse=True)
print("Sorted List (Reverse Alphabetical):", travel_wishlist)
