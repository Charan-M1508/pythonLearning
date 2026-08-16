#Sum of Digits
#Write a program that takes an integer and calculates the sum of its digits.

#String Input
x = input("Enter a number : ")
z = 0
for y in x.strip() :
    z += int(y)
print("Sum of digits = ",z)

#Integer Input
x = int(input("Enter a number : "))
y = 0
while x :
    y += x % 10
    x //= 10
print(y)