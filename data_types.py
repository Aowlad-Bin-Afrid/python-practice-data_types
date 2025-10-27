# Basic data-types examples
# Created by Afrid
# Date: 2025-10-27
# Description: Examples of basic Python data types — int, float, string, and boolean.

# Integer example
x = 25
z = -20
print(x,type(x))
print(z,type(z))

age = 18
print("\nInteger Example:")
print(f"Age: {age} | Type: {type(age)}")

x = 60
z = 40
y = x+z 
print(f"sum:{y} type,{type(y)}")

a = 40
b = 20
d = a-b
print(f"difference: {d} type,{type(d)} ")

# float example (decimal numbers)
a = 90.23
b = 203.0
c = -23.40
print(a, type(a))
print(b, type(b))
print(c, type(c))

w = 50.50
v = 50.50
c = w+v
print("sum:",c,type(c))

x = 10.0
y = 10
z = x+y # int + float = folat
print(f"sum:{z} type,{type(z)}")

# String (text)

name ="afrid"
x = "10.12"
y = "10"
print(f"name,{type(name)}\n x,{type(x)}\n y,{type(y)}")

a, h, r, s = "afrid", "hasu", "rhat", "sakib"
print(a,r,s,h)

print("\nFind out how old you will be in 5 years.")
name = input("Enter your name: ")
age  = int(input("Enter your age: "))
age += 5
print(f"Hi,{name} after 5 years you will be {age}")

# Boolean example (True or False)
x = 10 > 5
print(x, type(x))

y = 5 > 10
print(y, type(y))

a = 10 == 10
print(a, type(a))

b = 10 != 2
print(b, type(b))

age = int(input("Enter your age :  "))

if 18 <= age <= 50 :
    print("acceptable")
elif   age > 50 :
    print("sorry")
else:
    print("not acceptable")














