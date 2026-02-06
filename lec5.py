# a = "advait"
# i = 0 
# while a != "\0":
#     print(a[i])
#     i += 1
#^shows error 

s = input("Enter a string in lower case")
ss = ""
for i in s:
    if ord(i)<=ord('z') and ord(i)>=ord('a'):
        ss = ss+chr(ord(i)-32)
    else: 
        ss =ss+i
print(ss)