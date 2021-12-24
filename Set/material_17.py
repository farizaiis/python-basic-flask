set10 = {11, 12, 13, 14, 15}
print(set10)
# Output = {11, 12, 13, 14, 15}

# Data mix allowed
set1 = {101, 'Fariz', True}
print(set1)
# Output = {'Fariz', True, 101}

# Duplicate value not allowed
set2 = {11,12,11}
print(set2)
# Output = {11, 12}

# Set cannot have mutable items
# set = {1, 2, [3,4]} not allowed

# add an element
set10.add(20)
print(set10)
# Output = {20, 11, 12, 13, 14, 15}

# add multiple element
set10.update([21,22,23])
print(set10)
# Output = {11, 12, 13, 14, 15, 20, 21, 22, 23}

# add list and set
set10.update([24,25,26],{27,28,29})
print(set10)
# Output = {11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}

# remove and discard. if we use remove and the element not present it will be error, but not when using discard
set10.discard(11)
print(set10)
# Output = {12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}

set10.remove(12)
print(set10)
# Output = {13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}

set10.pop()
print(set10)
# Output = {14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29}

set10.clear()
print(set10)
# Output = set()


# Set operation union and use | for union
set5 = {0, 1, 2}
set6 = {3, 4, 5}
print(set5 | set6)
# Output = {0, 1, 2, 3, 4, 5}

print(set6 | set5)
# Output = {0, 1, 2, 3, 4, 5}

print(set5.union(set6))
# Output = {0, 1, 2, 3, 4, 5}

print(set6.union(set5))
# Output = {0, 1, 2, 3, 4, 5}


# Set operator intersection
print(set5 & set6)
# Output = set()

print(set6 & set5)
# Output = set()

print(set5.intersection(set6))
# Output = set()

print(set6.intersection(set5))
# Output = set()


# Set operator difference
print(set5 - set6)
# Output = {0, 1, 2}
print(set6 - set5)
# Output = {3, 4, 5}
print(set5.difference(set6))
# Output = {0, 1, 2}
print(set6.difference(set5))
# Output = {3, 4, 5}

# Set operator symmetric difference
print(set5 ^ set6)
# Output = {0, 1, 2, 3, 4, 5}
print(set6 ^ set5)
# Output = {0, 1, 2, 3, 4, 5}
print(set5.symmetric_difference(set6))
# Output = {0, 1, 2, 3, 4, 5}
print(set6.symmetric_difference(set5))
# Output = {0, 1, 2, 3, 4, 5}

# Set membership
print(0 in set5)
# Output = True
print(0 not in set5)
# Output = False
print(4 in set5)
# Output = False
print(4 not in set5)
# Output = True

# Iterating throug a set
for x in set('Welcome'):
    print(x)
    # Output = l o c m e w ==> random output

# Built in function with set
set7 = {0, 1, 2, 3, 4}
print(len(set7))
# Output = 
print(max(set7))
# Output = 
print(min(set7))
# Output = 
print(sorted(set7))
# Output = 
print(sorted(set7, reverse=True))
# Output = 
