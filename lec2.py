#Lecture2
#Example 1 
# a = int(input("Enter an integer :"))
# if a > 30:
#     print("a is greater than 30")
# if a > 40:
#     print("a is greater than 40")
# if a > 50:
#     print("a is greater than 50")
# else:
#     print("I dont know")

#Example 2:

# a = int(input("Enter an integer :"))
# if a > 30:
#     print("a is greater than 30")
# elif a > 40:
#     print("a is greater than 40")
# elif a > 50:
#     print("a is greater than 50")
# else:
#     print("I dont know")

#Example 3:

# a = int(input("Enter an integer:"))
# if a%2 == 0:
#     print("Divisible by 2")
# elif a%3 == 0:
#     print("Divisble by 3")
# elif a%5 == 0:
#     print("Divisible by 5")
# elif a%7 == 0:
#     print(("Divisble by 7"))
# else:
#     print("I dont know")

#Example 4:

# a = int(input("Enter an integer:"))
# if a%5 == 0:
#     print("Divisible by 5")
#     if a % 7 == 0:
#         print("Divisible by 7")
#     else:
#         print("Not divisible by 7")
# elif a%7 == 0:
#     print("divisble by 7")
# else:
#     print("Not divisible by 7 or 5")

#Example 5:
# name1 = "SaiU"
# password1 = "12345"

# name = input("Enter your name:")
# password = input("Enter your password:")

# if name == name1 and password == password1:
#     print("Log in succesful.")
# else:
#     print("Invalid credentials.")

#Exercise 1:
# num = int(input("Enter a number:"))
# if num%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

#Exercise 2:
# num1 = int(input("enter a number:"))
# num2 = int(input("enter another number:"))
# print("1.Addition")
# print("2. Subraction")
# print("3.Product")
# print("Division")
# c = int(input("Enter your choice:"))
# if c == 1:
#     print(f"answer:{num1 + num2}")
# elif c == 2:
#     print(f"answer:{num1 - num2 }")
# elif c == 3:
#     print(f"answer: {num1 * num2}")
# elif c == 4:
#     print(f"answer: {num1/num2}")
# else:
#     print("Invalid option")

#Exercise 3
# l = int(input("Length of the rectangle:"))
# b = int(input("Breadth of the rectangle:"))
# if l < 0 or b < 0:
#     print("invalid inputs")
# else:
#     print(f"Area: {l*b}")
#     print(f"Perimeter:{2*(l+b)}")

#Exercise 4
# a = int(input("a:"))
# b = int(input("b:"))
# c = int(input("c:"))
# r = b**2 - 4*a*c
# if r > 0:
#     print("The roots are real")
# elif r == 0:
#     print("The roots are equal")
# elif r < 0:
#     print("The roots are complex")

#Exercise 5
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = b**2 - 4*a*c
x1 = (-b - d**0.5)/2*a
x2 = (-b + d**0.5)/2*a
print( f"your roots are{x1}and {x2}")