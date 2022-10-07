# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
#
# sum=0
# previous_number=0
# for i in range(10):
#
#     sum=sum+i
    # print(sum)
    # print(i)
    #
    # print("Current number is :",i,"Previous number is :",previous_number,"sum is :",sum)
    # previous_number = i




# Exercise 2: Print characters from a string that are present at an even index number

# Name=input("Enter the Name")
# for i in Name:
#     index=Name.find(i)
#     # print(index)
#     if index % 2==0:
#         print(i)


# Exercise 3: Remove first n characters from a string

# name=input("Enter the name")
# number=int(input("Enter the number of element"))
# name2=[]
# for i in name:
#     if name.find(i)>=number:
#         name2.append(i)
# listToStr = ' '.join([str(elem) for elem in name2])
# print(listToStr)


# Exercise 4: Addition of natural numbers
# number=int(input("Enter the number of element"))
# sum=0
# for i in range(number+1):
#     print(i)
#     sum=sum+i
# print(sum)


#                                                 Exercise 5: factorials
# number=int(input("Enter the number of element"))
# factorial=1
# for i in range(1,number+1):
#     print(i)
#     factorial=factorial*i
# print(factorial)


# Exercise 6: While loop
# num=1
# while num<=10:
#     print(num)
#     num=num+1
#


# Functions
# Functions are of 3 types
# 1. Function without arguments
# def add():
#     number1=int(input("Enter the number of element"))
#     number2 = int(input("Enter the number of element"))
#     print(number1+number2)
# add()


# 2. Function with arguments
# def add(number1,number2):
#
#     print(number1+number2)
# add(2,3)


# 3. Function with arguments and return type

# def add(number1,number2):
#
#     return(number1+number2)
# print(add(2,3))

#                                                 Exercise 6: Sum of even numbers using function with argument and return type

def sum_even(num1,num2):

    sum=0
    for i in range(num1,num2+1):
        if i%2==0:
            sum=sum+i
    return(sum)
num1=int(input("enter the initial number"))
num2=int(input("enter the final number"))
print (sum_even(num1,num2))