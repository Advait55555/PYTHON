#Adding both strings
# s1 = "Sai University"
# s2 = "scds"
# s3 = s1 + s2 #Adds both of the strings
# print(s3)

# s4 = "advait"
# print("my name is "+s4+" "+"and im schizophrenic")

# #for loop syntax
# for i in range(0,6):
#     print(i,end = ' ')

# s1 = "Sai University"

# for i in range(0,7):
#     print(s1[i],end = ",")

# for i in s1:
#     print(s1,end = ',')

# for i in range (65,96):
#     print(chr(i), end = " ")

# str1 = input("Enter a string:")
# l1 = len(str1)
# for i in range(l1,0,-1):
#     print(str1[i],end = "       ITSSSSSSSS AN ERROR !!!!!!!

# n = int(input("Enter the range:"))
# for i in range(1,n+1):
#     if i%2 == 0 and i%3 == 0:
#         print( i,end = ',')

#using for loop, count the number of vowels and consonants
# vow = ['a','e','i','o','u']
# s1 = "sai university"
# count = 0
# ccount = 0
# for i in range(0,14):
#     if s1[i] == "a" or s1[i] == "e" or s1[i] == "i" or s1[i] == "o" or s1[i] == "u":
#         count += 1
#     else:
#         ccount += 1
# print(f"vowel count = {count}")
# print(f"consonant count = {ccount}")

vow = ['a','e','i','o','u']
s1 = "sai university"
count = 0
ccount = 0
for i in range(0,14):
    for j in range(0,5):
        if s1[i] == vow[j]:
            count += 1
        elif s1[i] != vow[j]:
            ccount += 1
print(f"vowel count = {count}")
print(f"consonant count = {ccount}")    