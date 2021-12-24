tuple1 = ()
print(tuple1)
# Output = ()

# Create tuple with integer element
tuple2 = (1, 2, 3)
print(tuple2)
# Output = (1, 2, 3)

# Tuple with mix data type
tuple3 = (101, 'Anirban', True)
print(tuple3)
# Output = (101, 'Anirban', True)

# Nested tuple
tuple4 = ("points", [1, 2, 3], (4, 5, 6))
print(tuple4)
# Output = ('points', [1, 2, 3], (4, 5, 6))

# Tuple without any parentheses
tuple5 = 101, 'Fariz', True
print(tuple5)
# Output = (101, 'Fariz', True)

# Tuple unpacking is also posibble
empid,empname,empsal = tuple5
print(empid)
# Output = 101
print(empname)
# Output = Fariz
print(empsal)
# Output = True
print(type(tuple5))
# Output = <class 'tuple'>