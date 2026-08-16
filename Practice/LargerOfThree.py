#Largest of Three Numbers:
#Take three numbers as input and find the largest number without using max().

x = input("Enter three numbers : ")
a, b, c = x.split(' ') #what I programmed
a, b, c = map(int, x.split()) # Actual code
if a > b :
    if a > c :
        print("Largest number of three numbers is : ",a)
    else :
        print("Largest number of three numbers is : ",c)
else :
    if b > c :
        print("Largest number of three numbers is : ",b)
    else :
        print("Largest number of three numbers is : ",c)