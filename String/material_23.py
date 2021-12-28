# using enumerate()
mystr = 'university'

my_list_enumerate = list(enumerate(mystr))
print('list(enumerate(mystr)) ', my_list_enumerate)
# Output = list(enumerate(mystr))  [(0, 'u'), (1, 'n'), (2, 'i'), (3, 'v'), (4, 'e'), (5, 'r'), (6, 's'), (7, 'i'), (8, 't'), (9, 'y')]    

# use \n to a new line. example = 'ABC\nDEF'
# use \t to a new line. example = 'ABC\tDEF'
print('ABC written \x41\x42\x43\x44 (HEX) Presentation')
# Output = ABC written ABCD (HEX) Presentation

# Format method
default_order = '{} {} and {}'.format('Today', 'is', 'Sunday')
print(default_order)
# Output = Today is and Sunday

positional_order = '{1} {0} and {2}'.format('is', 'Today', 'Sunday')
print(positional_order)
# Output = Today is and Sunday

keyword_order = '{t} {i} and {s}'.format(i='is',t='Today',s='Sunday')
print(keyword_order)
# Output = Today is and Sunday

print('Required binary representation of {0} is {0:b}'.format(20))
# Output = Required binary representation of 20 is 10100
print('Exponent representation: {0:e}'.format(1566.345))
# Output = Exponent representation: 1.566345e+03   
print('One third is: {0:.3f}'.format(1/3))
# Output = One third is: 0.333



# String methods
print('gOOd moRNing tO alL'.lower())
# Output = good morning to all
print('gOOd moRNing tO alL'.upper())
# Output = GOOD MORNING TO ALL
print('gOOd moRNing tO alL'.find('tO'))
# Output = 13
print('gOOd moRNing tO alL'.find('to'))
# Output = -1
print('gOOd moRNing tO alL'.replace('alL', 'Everybody'))
# Output = gOOd moRNing tO Everybody
print('gOOd moRNing tO alL'.replace('all', 'Everybody'))
# Output = gOOd moRNing tO alL