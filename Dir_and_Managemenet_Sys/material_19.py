import os
print(os.getcwd()) #Return the present working directory
print(os.getcwdb()) #Return the present working directory as a byte object

os.chdir('C:\\Users\\bstop\\Documents\\koneksi\\fariz\\python-flask\\test') #Use to change directory
print(os.listdir()) #All files and sub directories inside a directory can be known using listdir

# used to make a new directory
os.mkdir('test')

# used to rename a directory
os.rename('Test','New_One')

# Removing a file and directory
os.remove('Test.txt') #remove file 
os.rmdir('New_One') #remove directory

os.chdir('C:\\Users\\bstop\\Documents\\koneksi\\fariz\\python-flask')
