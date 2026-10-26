from numpy import *
import textwrap
import cmath

# ##arr = array([1,2,3,4,5,6,7,8], int)
# arr = ones(5,int)

# print(arr.dtype)
# print(arr)

# arr = array([
#     [1,2,3],
#     [4,5,6]
# ])

# print(arr)

# on = {25,14,95,63,76}
# # #on.pop(2)

# print(on[2])

# f = ['apple','banana','mango']
# print(f[-1][-1])

# f = (1,2,3)
# f[2] = 4


# a = 4
# b = 6
# a,b = b,a

# print(a)
# print(b)

# print(10<<2)

# True = False
# while True:
#     print(True)
#     break

# print('Telusko', end='')
# print('navin')

# a = array('ch',[1,2,3,4])
# print(a)


# x = int(input("Enter a number"))
# y = int(input("Enter a number"))
# z = int(input("Enter a number"))
# n = int(input("Enter a number"))

# list2 = []
# a = 0

# try:
#     while a <= x:
#         b = 0
#         while b <= y:
#             c = 0
#             while c <= z:
#                 list1 = [a,b,c]
#                 if a+b+c != n:
#                     list2.append(list1)
#                 c += 1
#             b += 1
#         a += 1
#     print(list2)
# except Exception as e:
#     print(e)



# n = int(input())
# arr = map(int, input().split())
# List1 = []
# j = -100
# k = -100
# for i in arr:
#     if n == 0:
#         break
#     List1.append(i)
#     if i > j:
#         j = i
# for i in List1:
#     if i > k and i != j:
#         k = i
# print(k)



# students = []
# # Read the number of students
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])

# unique_scores = sorted(list(set([student[1] for student in students])))
# second_lowest_score = unique_scores[1]

# second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_score])

# for name in second_lowest_students:
#     print(name)


        
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# print(student_marks[query_name])

# student_marks = {'harry': [20.0, 57.0, 67.0], 'harsh': [30.0, 43.0, 24.0], 'luie': [46.9, 75.7, 23.6]}
# query_name = input()
# list1 = student_marks[query_name]
# avrg = lambda a: f"{sum(a)/len(a):.2f}"
# print(avrg(list1))


# N = int(input())
# list = []
# while N != 0:
#     cmd,*num = input().split()
#     match str(cmd):
#         case 'insert':
#             list.insert(int(num[0]),int(num[1]))
#         case 'append':
#             list.append(int(num[0]))
#         case 'print':
#             print(list)
#         case 'remove':
#             list.remove(int(num[0]))
#         case 'reverse':
#             list.reverse()
#         case 'sort':
#             list.sort()
#         case 'pop':
#             list.pop()
#         case _:
#             print("Wrong command please try again")
#             N += 1
#     N -= 1


# N = int(input())
# my_list = []

# for _ in range(N):
#     cmd, *num = input().split()
    
#     # Convert all extracted string numbers into integers upfront
#     args = [int(i) for i in num]
    
#     match cmd:
#         case 'insert':
#             my_list.insert(args[0], args[1])
#         case 'append':
#             my_list.append(args[0])
#         case 'print':
#             print(my_list)
#         case 'remove':
#             my_list.remove(args[0])
#         case 'reverse':
#             my_list.reverse()
#         case 'sort':
#             my_list.sort()
#         case 'pop':
#             my_list.pop()
#         case _:
#             print("Wrong command please try again")



# s = input()
# ch = list(s)
# string = ''
# for i in ch:
#     if i.islower():
#         string += i.upper()
#     elif i.isupper():
#         string += i.lower()
#     else:
#         string += i
# print(string)


# s = input()
# ch = s.split()
# print(ch)
# ch = '-'.join(ch)
# print(ch)


# first = input()
# last = input()
# txt = f"Hello {first} {last}! You just delved into python."
# print(txt)


# s = input()
# txt = list(s)

# for i in txt:
#     if i.islower():
#         lr = True
#     elif i.isupper():
#         up = True
#     elif i.isdigit():
#         dg = True
#     elif lr and up and dg:
#         break
# if lr and up and dg:
#     print("True")
# else:
#     print("False")
# if lr and up:
#     print("True")
# else:
#     print("False")
# if dg:
#     print("True")
# else:
#     print("False")
# if lr:
#     print("True")
# else:
#     print("False")
# if up:
#     print("True")
# else:
#     print("False")

# def wrap(string, max_width):
#     n = len(string)
#     count = 0
#     s = ''
#     while count <= n:
#         count += max_width
#         s += string[count-max_width:count]+'\n'
#     s += string[count:n]
#     return s

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# number = int(input())
# width = len(bin(number)[2:])
    
# for i in range(1, number + 1):
#     # Convert to each format and remove the Python prefix (0o, 0x, 0b)
#     dec_val = str(i)
#     oct_val = oct(i)[2:]
#     hex_val = hex(i)[2:].upper()
#     bin_val = bin(i)[2:]
    
#     # Print each value right-aligned to the calculated width, separated by a single space
#     print(f"{dec_val.rjust(width)} {oct_val.rjust(width)} {hex_val.rjust(width)} {bin_val.rjust(width)}")


# n,m = map(int,input().split())
# print(n,m)
# mid = n//2 + 1
# midrow = (m-7)//2
# print(mid)
# row = (m-3)//2
# k = 1
# for i in range(1,n+1):
#     if i < mid:
#         print((row*'-')+(k*'.|.')+(row*'-'))
#         row -= 3
#         k += 2
#     elif i == mid:
#         print((midrow*'-')+'WELCOME'+(midrow*'-'))
#     elif i > mid:
#         row += 3
#         k -= 2
#         print((row*'-')+(k*'.|.')+(row*'-'))


# Lowercase letters (a to z) range from 97 to 122.
# Uppercase letters (A to Z) range from 65 to 90.
# for i in range(97, 123):
#     print(chr(i),end=' ')



# size = int(input())
# count = ((size*2 - 1)*2 - 1)
# row = (count-1)//2
# alpha = 96+size
# k = 1
# for i in range(1,(size+1)):
#     print((row*'-'),end="")
#     for j in range(alpha,alpha-k,-1):
#         if i == 1:
#             print(chr(j),end="")
#         else:
#             print(chr(j)+'-',end="")
#     for j in range(alpha-k+2,alpha+1):
#         if j == alpha:
#             print(chr(j),end="")
#         else:
#             print(chr(j)+'-',end="")
#     print(((row)*'-'))
#     row -= 2
#     k += 1
# k -= 2
# row += 4
# for i in range(1,size):
#     print((row*'-'),end="")
#     for j in range(alpha,alpha-k,-1):
#         if i == size-1:
#             print(chr(j),end="")
#         else:
#             print(chr(j)+'-',end="")
#     for j in range(alpha-k+2,alpha+1):
#         if j == alpha:
#             print(chr(j),end="")
#         else:
#             print(chr(j)+'-',end="")
#     print(((row)*'-'))
#     row += 2
#     k -= 1


# s = input()
# arr = list(s.split())
# k = s
# arr2 = []
# for i in arr:
#     a = list(i)
#     x = a[0]
#     a[0] = x.upper()
#     x = ''.join(a)
#     arr2.append(x)
# for i in range(len(arr)):
#     k = k.replace(arr[i],arr2[i])
# print(k)

# a = list(arr[0])
# b = list(arr[1])
# x = a[0]
# a[0] = x.upper()
# y = b[0]
# b[0] = y.upper()
# x = ''.join(a)
# y = ''.join(b)
# result = x + ' ' + y
# print(result)

# HelloWorldLol


# n = int(input())
# arr = []
# for i in range(n):
#     a,b = list(input().split())
#     arr.append([a,b])
# for i in arr:
#     try:
#         print(int(i[0])//int(i[1]))
#     except ZeroDivisionError as e:
#         print("Error Code:",'integer division or modulo by zero')
#     except ValueError as e:
#         print("Error Code:",e)
#     except Exception as e:
#         print(("Error Code:",e))


# s = input()
# print(abs(complex(s)))
# print(cmath.phase(complex(s)))
