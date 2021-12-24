class my_complex_number:
    # Constructor Method
    def __init__(self, real=0, imag=0):
        print("my_complex_number constructor...")
        self.real_part = real
        self.imag_part = imag

    def display_complex(self):
        print('{0}+{1}j'.format(self.real_part, self.imag_part))

# Create a new object against my_complex_number class
complex1 = my_complex_number(40,50)
complex1.display_complex()
# Output will be like below comment
# my_complex_number constructor...
# 40+50j

complex2 = my_complex_number(30, 40)
complex2.new_attribute = 80
print(complex2.real_part, complex2.imag_part, complex2.new_attribute)
# Output will be like below comment
# my_complex_number constructor...
# 30 40 80

del complex1
print(complex1)
#Output : NameError: name 'complex1' is not defined