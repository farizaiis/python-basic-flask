# # Name (also called identifier) is simply a name given to objects

# # We can get the address (in RAM) of some object through the built-in function, id()
# # Note : You may get different value of id

# a = 2
# print(id(2))
# # Output = 2505803589968
# print(id(a))
# # Output = 2505803589968

# a = a+1
# print(id(a))
# # Output = 2505803590000
# print(id(3))
# # Output = 2505803590000


# Scopes
def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)
        # Output = 

    inner_function()
    print('a =', a)
    # Output = 

a = 10
print('a =', a)
# Output = 
outer_function()
print('a =', a)
# Output = 
