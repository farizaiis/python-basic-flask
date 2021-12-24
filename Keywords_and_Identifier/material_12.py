# GLOBAL
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15
read1()
# Output = 10
write1()
read1()
# Output = 5
write2()
read1()
# Output = 5


# IN
a = [1, 2, 3, 4]
print(3 in a)
# Output = True
print(0 in a)
# Output = False


# IS
print(True is True)
# Output = True
print(True is False)
# Output = False