# value1 = 100
# print(type(value1))
# # Output = <class 'int'>
# print(isinstance(value1,int))
# # Output = True
# print(isinstance(value1,float))
# # Output = False
# print(isinstance(value1,complex))
# # Output = False

# value2 = 100.24
# print(type(value2))
# # Output = <class 'float'>
# print(isinstance(value2,int))
# # Output = False
# print(isinstance(value2,float))
# # Output = True
# print(isinstance(value2,complex))
# # Output = True


# value3 = 50 + 6j
# print(type(value3))
# # Output = <class 'complex'>
# print(isinstance(value3,int))
# # Output = False
# print(isinstance(value3,float))
# # Output = False
# print(isinstance(value3,complex))
# # Output = True


# print(0b1101)
# # Output = 13
# print(0xab)
# # Output = 171
# print(0o23)
# # Output = 19

# print(10 + 33.4)
# # Output = 43.4


# print(int(10.5))
# # Output = 10
# print(int(-20.99))
# # Output = -20
# print(float(10))
# # Output = 10.0

# from decimal import Decimal as D
# import decimal
# print(0.2)
# # Output = 0.3
# print(D(0.2))
# # Output = 0.200000000000000011102230246251565404236316680908203125
# print(decimal.Decimal(0.3))
# # Output = 0.299999999999999988897769753748434595763683319091796875

# from fractions import Fraction as F
# print(F(1.5))
# # Output = 3/2
# print(F(5))
# # Output = 5
# print(F(1,5))
# # Output = 1/5

# import math
# print(math.pi)
# # Output = 3.141592653589793
# print(math.cos(10))
# # Output = -0.8390715290764524
# print(math.log(10))
# # Output = 2.302585092994046
# print(math.log10(10))
# # Output = 1.0
# print(math.exp(10))
# # Output = 22026.465794806718
# print(math.factorial(5))
# # Output = 120
# print(math.sinh(10))
# # Output = 11013.232874703393

import random
print('Random number -> ', random.randrange(5,15))
# Output = Random number ->  12
print('Random number -> ', random.randrange(5,15))
# Output = Random number ->  12
print('Random number -> ', random.randrange(5,15))
# Output = Random number ->  11
print('Random number -> ', random.randrange(5,15))
# Output = Random number ->  7

day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print(random.choice(day))
# Output = Sat
print(day)
# Output ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
random.shuffle(day)
print(day)
# Output = ['Sun', 'Fri', 'Thu', 'Wed', 'Sat', 'Tue', 'Mon']
print(random.random())
# Output = 0.011655865052920933