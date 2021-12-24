# # Accessing element on dictionary/object
# new_obj = {1: 'Hello', 2: 'Hi', 3: 'Hola'}
# print(new_obj)
# # Output = {1: 'Hello', 2: 'Hi', 3: 'Hola'}
# print(new_obj[1])
# # Output = Hello
# print(new_obj.get(2))
# # Output = Hi

# # Updating Value
# new_obj[1] = 'Hey'
# print(new_obj)
# # Output = {1: 'Hey', 2: 'Hi', 3: 'Hola'}

# # Adding Value
# new_obj[4] = 'Namaste'
# print(new_obj)
# # Output = {1: 'Hey', 2: 'Hi', 3: 'Hola', 4: 'Namaste'}

# # remove a particular item
# print(new_obj.pop(1))
# # Output = Hey

# # remove an arbitory item
# print(new_obj.popitem())
# # Output = (4, 'Namaste')

# # delete a particular item
# del new_obj[2]
# print(new_obj)
# # Output = {3: 'Hola'}

# # delete entire obj/dictionary
# del new_obj

# Create new dictionary using comprehension
squares = {x: x*x for x in range(6)}
print(squares)
# Output = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Membership test
print(1 in squares)
# Output = True
print(2 not in squares)
# Output = False
print(25 in squares)
# Output = False

# Iterating through a dictionary
new_squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for i in new_squares:
    print(new_squares[i])

# using built-in in a dictionary
print(len(new_squares))

print(sorted(new_squares))

print(sorted(new_squares, reverse=True))