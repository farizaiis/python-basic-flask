# LAMBDA
a = lambda x: x*2
for i in range(1,6):
    print(i, a(i))
# Output = 1 2, 2 4, 3 6, 4 8, 5 10

# NONLOCAL
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("inner Function", a)
    inner_function()
    print("Outer function", a)

outer_function()
# Output = inner function 10, outer function 10

# PASS
def function(args):
    pass
function(10)
# No output but no error because using pass

# RETURN
def func_return():
    a = 10
    return a
print(func_return())
# Output = 10

# WHILE
i = 5
while(i>0):
    print(i)
    i -= 1