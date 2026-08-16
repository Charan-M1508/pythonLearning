#Count Vowels
#Given a string, count how many vowels (a, e, i, o, u) it contains.

x = input("Enter a String : ")
z = 0
for y in x.strip() :
    if y in "aeiou":
        z += 1
print("Count of vowels in given string = ",z)