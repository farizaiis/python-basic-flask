# implicit type conversion
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print('datatype of num_int:', type(num_int))
# Output = datatype of num_int: <class 'int'>
print('datatype of num_flo:', type(num_flo))
# Output = datatype of num_flo: <class 'float'>
print('value of num_new:',num_new)
# Output = value of num_new: 124.23
print('datatype of num_new:', type(num_new))
# Output = datatype of num_new: <class 'float'>

num_str = '456'
print('datatype of num_int:', type(num_str))
# Output = datatype of num_new: <class 'float'>
# print(num_int + num_str)
# Error implicit conversion will not work here

num_str = int(num_str)
print('datatype of num_int:', type(num_str))
# Output = 
print(num_int + num_str)
# Output = 
