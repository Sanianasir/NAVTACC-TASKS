cart = ["T-shirt", "Lamp", "Pen"]
print(cart)

# A list of mixed data types
my_list = [1, "Python", 3.14]
print(my_list)

# Empty list
my_list = []
print(my_list)

vowels = "aeiou"

# Convert a string to a list
vowels_list = list(vowels)
print(vowels_list)

languages = ["Python", "Swift", "C++"]

# Access the first item
print(f"languages[0] = {languages[0]}")

# Access the third item
print(f"languages[2] = {languages[2]}")

languages = ["Python", "Swift", "C++"]

# Access the last item
print('languages[-1] =', languages[-1])

# Access the third last item
print('languages[-3] =', languages[-3]) 

languages = ["Python", "Swift", "C++"]

# Access the last item
print('languages[-1] =', languages[-1])

# Access the third last item
print('languages[-3] =', languages[-3]) 

cart = ["T-shirt", "Lamp", "Pen"]

# Update second item to "Shoes"
cart[1] = "Shoes"

print(cart)    # ['T-shirt', 'Shoes', 'Pen']

cart = ["T-shirt", "Lamp", "Pen"]

# Add "Book" to the list
cart.append("Book")

print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Book']

cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]

# Add all the items from fav_items to cart
cart.extend(fav_items)

print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Headphones', 'Phone']

cart = ["T-shirt", "Lamp", "Pen"]

# Add "Book" at index 2 (3rd position)
cart.insert(2, "Book")

print(cart)    # ['T-shirt', 'Lamp', 'Book', 'Pen']

cart = ["T-shirt", "Lamp", "Pen", "Book"]

# Remove "Pen" from the list
cart.remove("Pen")    # ['T-shirt', 'Lamp', 'Book']

# Remove the last item
last_item = cart.pop()
print(cart)   # ['T-shirt', 'Lamp']
print(last_item)    # Book

# Clear the list
cart.clear()
print(cart)    # []

cart = ['T-shirt', 'Lamp', 'Pen', 'Book']

# Delete the third item (index 2)
del cart[2]
print(cart)    # ['T-shirt', 'Lamp', 'Book']

# Delete the list itself
del cart
print(cart)    # NameError: name 'cart' is not defined

favorite_items = ["T-shirt", "Lamp", "Pen"]

cart = favorite_items

# Add an item to favorite_items list
favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")

favorite_items = ["T-shirt", "Lamp", "Pen"]

# Copying a list
cart = favorite_items.copy()

# Add an item to favorite_items list
favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")

favorite_items = ["T-shirt", "Lamp", "Pen"]

size = len(favorite_items)
print(size)   # 3

cart = ["T-shirt", "Lamp", "Pen"]

result = "Lamp" in cart
print(result)   # True

result = "Book" in cart
print(result)   # False

cart_items = ["T-shirt", "Lamp", "Pen"]

for item in cart_items:
    print(item)

