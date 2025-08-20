#Remove Letters from a string
a = "Hello, World"
print(a.replace("Hello", "World"))
print(a.replace("World", "Hello"))

# Convert String to a List
a = "Hello, World"
m = list(a)
print(m)

# Convert a List of characters into String
l = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd']
n = ''.join(l)
print(n)

# Check if a string is or not
b = input("Enter a string: ")
if b == "":
    print("Empty string")
else:
    print(b)

# Convert a tuple to string
tup = ('1','2','3','4','5')
c = ''.join(tup)
print(c)

# Convert String to Set
s = "Hello, World"
v = set(s)
print(v)

# Convert set to a String
h = ('1','2','3','4','5')
k = ''.join(h)
print(k)

#Reverse String
y = "Hello"
rev = ""
for i in y:
    rev = i + rev
print(rev)

#Avoid Spaces
o = " Hello  World "
print(o.strip())