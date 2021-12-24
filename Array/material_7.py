#Slicing on array
fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
print(fruits)
# Output = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']
# print(fruits[1:4]) # start from index 1, and end at index 3. index 4 not included
# Output = ['Banana', 'Mango', 'Grapes']
# print(fruits[ : 3]) # start from index 0 end at index 2. index 3 not included
# Output = ['Apple', 'Banana', 'Mango']
# print(fruits[-4:]) # start from index -4. index -5 and more not included 
# Output = ['Banana', 'Mango', 'Grapes', 'Orange']
print(fruits[-3:-1]) # start from index -3 end at index -2. index -1 not included
# Output = ['Mango', 'Grapes']