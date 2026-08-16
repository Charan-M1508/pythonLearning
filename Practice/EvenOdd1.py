#1. Even or Odd
#Write a program that takes an integer from the user and prints whether it is even or odd.

x = int(input("Enter a number to find even or odd : "))
if x % 2 == 0 :
    print("Even")
else :
    print("Odd")