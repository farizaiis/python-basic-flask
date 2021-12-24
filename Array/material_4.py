brands = ['Coke', "Apple", "Google", "Microsoft", "Toyota"]
print(brands)
# Output = ['Coke', 'Apple', 'Google', 'Microsoft', 'Toyota']

# Finding the length of array
num_brands = len(brands)
print(num_brands)
# Output = 5

# Adding an element to an array
brands.append('Intel')
print(brands)
# Output = ['Coke', 'Apple', 'Google', 'Microsoft', 'Toyota', 'Intel']

# Removing an element from array
brands.remove('Coke')
print(brands)
# current Brands = ['Apple', 'Google', 'Microsoft', 'Toyota', 'Intel']
del brands[1] # => delete 'Google'
print(brands)
# current Brands = ['Apple', 'Microsoft', 'Toyota', 'Intel']
brands.pop(1) # => delete 'Microsoft'
print(brands)
