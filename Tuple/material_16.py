# Accessing elements in tuple
tuple1 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1)
# Output = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple1[1])
# Output = e
print(tuple1[3])
# Output = c
print(tuple1[5])
# Output = m

# Nested tuple
nest_tuple2 = ('Point', [1, 3, 4], (8, 9, 10))
print(nest_tuple2)
# Output = ('Point', [1, 3, 4], (8, 9, 10))
print(nest_tuple2[0][2])
# Output = i
print(nest_tuple2[1][2])
# Output = 4
print(nest_tuple2[2][2])
# Output = 10

# Slicing tuple
print(tuple1[1:3])
# Output = ('e', 'l')
print(tuple1[:-3])
# Output = ('w', 'e', 'l', 'c')
print(tuple1[3:])
# Output = ('c', 'o', 'm', 'e')
print(tuple1[:])
# Output = ('w', 'e', 'l', 'c', 'o', 'm', 'e')

# Tuple Concentation
tuple2 = ('w', 'e', 'l')
tuple3 = ('c', 'o', 'm', 'e')
print(tuple2 + tuple3)
# Output = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(('Again',) * 4)
# Output = ('Again', 'Again', 'Again', 'Again')

# Tuple method
tuple4 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple4.count('e'))
# Output = 2
print(tuple4.index('c'))
# Output = 3

# Tuple operation
print('c' in tuple4)
# Output = True
print('c' not in tuple4)
# Output = False
print('a' in tuple4)
# Output = False
print('a' not in tuple4)
# Output = True


# Builtin function tuple
tuple7 = (22,33,55,44,77,66,11)
print(max(tuple7))
# Output = 77
print(min(tuple7))
# Output = 11
print(sorted(tuple7))
# Output = [11, 22, 33, 44, 55, 66, 77]
print(sorted(tuple7, reverse=True))
# Output = [77, 66, 55, 44, 33, 22, 11]
print(len(tuple7))
# Output = 7