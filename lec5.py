# a = "advait"
# i = 0 
# while a != "\0":
#     print(a[i])
#     i += 1
#^shows error 

# s = input("Enter a string in lower case")
# ss = ""
# for i in s:
#     if ord(i)<=ord('z') and ord(i)>=ord('a'):
#         ss = ss+chr(ord(i)-32)
#     else: 
#         ss =ss+i
# print(ss)

a = int(input("enter an integer:"))
sum = 0
while a!=0:
    lastdigit = a%10
    sum = sum + (lastdigit**2)
    a = a//10
print(sum)

