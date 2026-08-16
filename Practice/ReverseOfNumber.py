#Reverse a Number
#Reverse an integer without converting it to a string.

x = int(input("Enter a number : "))
y = 0
while x :
    y *= 10
    y += x % 10
    x //= 10
print(y)