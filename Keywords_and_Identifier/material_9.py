# # TRUE FALSE
# print(5 == 5)
# # Output = True
# print(5 > 5)
# # Output = False


# # NONE
# print(None == 0)
# # Output = False
# print(None == False)
# # Output = False
# print(None == [])
# # Output = False
# print(None == None)
# # Output = True

# def a_void_function():
#     a = 1
#     b = 2
#     c = a + b

# x = a_void_function()
# print(x)
# # Output = None

# # AND, OR, NOT
# print(True and False)
# # Output = False
# print(True or False)
# # Output = True
# print(not False)
# # Output = True

# # AS
# import math as myMath
# print(myMath.cos(myMath.pi))
# # Output = -1.0

# # ASSERT
# assert 5 > 5
# # No output but error
# assert 5 == 5
# # No output but no error

# # BREAK
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)
# # Output = 1 2 3 4

# # CONTINUE
# for x in range(1,8):
#     if x == 5:
#         continue
#     print(x)
# # Output = 1 2 3 4 5 6 7

# CLASS
class example_class:
    def function1(params):
        print("function1() executing...")
    def function2(params):
        print("function2() executing...")
ob1 = example_class()
ob1.function1()
# Output = function1() executing...
ob1.function2()
# Output = function2() executing...


# DEF
def function_name(params):
    pass
function_name(19)
# No output but no error

# DEL
a = 10
print(a)
# Output = 10
del a
# print(a)
# Output = 'Error, a is not defined.' because already delete at line 83

# IF ELIF ELSE
num = 2
if num == 1:
    print('One')
elif num == 2:
    print('Two')
else:
    print('Something Else')
# Output = 'Two' . Because num not equal to 1 and then it will be next to the next if condition, and then stop at the second condition because its True 2 equal to 2

# TRY RAISE CATCH FINALLY
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print('Division cannot be performed')
finally:
    print('Success')
# Output : Division cannot be performed, Success

for i in range(1, 5):
    print(i)
# Output : 1 2 3 4