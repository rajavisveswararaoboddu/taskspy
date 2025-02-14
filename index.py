
 natural number
 n=int(input("enter"))
for i in range(1,n+1):
    print(i)

# print the elements in the list
list=[1,2,3,4,5,6,7,8,9]
 for i in list:
     print(i)

# create a variable - int,float,string,bool
 x=int(5)
 y=float(60)
 z=str("varshini")
 print(x)
 print(y)
 print(z)

# boolean--
# a=30
# b=20
# if a<b:
#     print("a is less than b")
# else:
#     print("a is greater than b")  
  
# arthematic operators
# x=8
# y=10
# print(x+y)
# print(x-y)
# print(x*y)
# print(x%y)
# print(x/y)
# print(x**y)
# print(x//y)

# logical operator
# and,or,not
# x=9
# print(x<3 and x>10)
# print(x<3 or x>10)
# print(not(x<9 and x>10))

# relational operator
# def myfunc():
#     n=int(input("enter"))
#     for i in range(0,n+1):
#         if i%2==0:
#             print("it is even")
#         else:{
#             print("it is odd")
#     } 
# myfunc()

# sides of a triangle
# side1 = float(input("side1 - "))
# side2 = float(input("side2 - "))
# side3 = float(input("side3 - "))
# print("triangle possible" if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1) else "triangle is not possible")

# battel warriors
# warrior1 = (100, 50)  
# warrior2 = (90, 50)
# health1, attack1 = warrior1
# health2, attack2 = warrior2
# if attack1 > attack2:
#     print("Warrior 1 wins")
# elif attack2 > attack1:
#     print("Warrior 2 wins")
# else:
#     if health1 > health2:
#         print("Warrior 1 wins")
#     elif health2 > health1:
#         print("Warrior 2 wins")
#     else:
#         print("Draw")

# prime number in a given range
# num1 = int(input("enter lower - "))
# num2 = int(input("enter upper - "))

# for p in range(num1,num2 + 1):
#     count = 0
#     for i in range(1,p + 1):
#         if p % i == 0:
#             count += 1
#     if count == 2:
#         print(p,"is a prime")  
    # else:
    #      print(p,"is Not a prime")    

#nearest number
# num = int(input("enter a number - ")) 

# while True:
#     if num in [0,1,2]:
#         print(num," is not exist")
#         break
#     num -= 1
#     count = 0
#     for i in range(1,num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num,"is a prime") 
#         break 

#Q1: Nearest leap year in the increasing side
# year = int(input("enter the year - "))
# year += 1
# while (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
#    print("is leap year")
# year = int(input("Enter a year: "))
# prev_year = year - 1
# next_year = year + 1
# while True:
#     if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
#         print("The nearest leap year is:", next_year)
#         break
#     elif (prev_year % 4 == 0 and prev_year % 100 != 0) or (prev_year % 400 == 0):
#         print("The nearest leap year is:", prev_year)
#         break
#     else:
#         prev_year -= 1
#         next_year += 1

# year = int(input("Enter a year: "))
# prev_year, next_year = year - 1, year + 1

# while not ((next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0) or (prev_year % 4 == 0 and prev_year % 100 != 0) or (prev_year % 400 == 0)):
#     prev_year -= 1
#     next_year += 1

# if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
#     print("The nearest leap year is:", next_year)
# else:
#     print("The nearest leap year is:", prev_year)

#Q2 -Perfect number 6 => 1, 2, 3, 6 => Sum of 1, 2, 3 => 6
# # num1 = int (input("enter the number"))
# sum = 0
# for i in range (1, num1):
#     if num1 % i == 0:
#         sum += i
#     if sum == num1:
#         print("prefect number")

#Q3: Find all armstrong number in a given range
#153 => 125 + 27 + 1 => 153
# for num in range(1, 1001):  
#     temp = num  
#     order = len(str(num))  
#     sum_of_powers = 0  

#     while temp > 0:  
#         digit = temp % 10  
#         sum_of_powers += digit ** order  
#         temp //= 10  

#     if num == sum_of_powers:  
#         print(num)

# def armstrong(num):
#     order = len(str(num))
#     sum_digit = sum(int(digit) ** order for digit in str(num))
#     return sum_digit == num
# armstrong = [num for num in range(0,1001) if armstrong(num)]
# print("armstrong numbers from 1 to 1000:",armstrong)


# write a program to print numbers from  -1 to -10
# def print_numbers():
#     for num in range(-1, -11, -1):
#         print(num)
# print_numbers()

# sum of digits in a number  - and add when it is even 
# def sum_of_digits(number):
#     num_str = str(number)
#     total_sum = 0
#     for i in num_str:
#         total_sum += int(i)
#     if total_sum % 2 == 0:
#         return total_sum
#     else:
#         return "The sum of the digits is not even."
# number = 1234
# result = sum_of_digits(number)
# print("Sum of digits:", result)

# prime number or not prime
# num1 = int(input("enter lower - "))
# num2 = int(input("enter upper - "))

# for p in range(num1,num2 + 1):
#     count = 0
#     for i in range(1,p + 1):
#         if p % i == 0:
#             count += 1
#     if count == 2:
#         print(p,"is a prime")  
    # else:
    #      print(p,"is Not a prime")
 
# range of numbers - check prime or not in  certain range of numbers 
# write a program to print sum of non-primes  digits in a given number  - 3437 => 3,3,7 =>13
# write a program to print max prime digit in a certain number  912780 =>2,7 => max - 7 
# compare first digit and last digit in a number  (print equal - if there are  equal )
#  print nth fibnocci number 
# print non-fibnocci numbers  in  given range  -(1 to 100) 
# reverse a num  in  negative numbers
