# WITH
with open('example.txt', 'w') as f:
    f.write('Hello World')
# Will create a new file wit body 'Hello World', if name of the file aready exist it will replace the old file

# YIELD
def generator():
    for i in range(6):
        yield i

g = generator()
for i in g:
    print(i)
# Output = 0 1 2 3 4 5