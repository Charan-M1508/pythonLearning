#Palindrome
#Check whether a string is a palindrome.

x = input("Enter a string : ")
y = len(x)
a = ""
while y != 0 :
    a += x[y-1]
    y -= 1
if x == a :
    print("Palindrome")
else :
    print("Not a Palindrome")