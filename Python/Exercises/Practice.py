# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
#
sum=0
previous_number=0
for i in range(10):

    sum=sum+i
    # print(sum)
    # print(i)

    print("Current number is :",i,"Previous number is :",previous_number,"sum is :",sum)
    previous_number = i



<<<<<<< HEAD





=======
>>>>>>> b78cc3f19afa715881b4982d5bfd3456e83e5447
# Exercise 2: Print characters from a string that are present at an even index number

Name=input("Enter the Name")
for i in Name:
    index=Name.find(i)
    # print(index)
    if index % 2==0:
        print(i)


# Exercise 3: Remove first n characters from a string

name=input("Enter the name")
number=int(input("Enter the number of element"))
name2=[]
for i in name:
    if name.find(i)>=number:
        name2.append(i)
listToStr = ' '.join([str(elem) for elem in name2])
print(listToStr)


# Exercise 4: Addition of natural numbers
number=int(input("Enter the number of element"))
sum=0
for i in range(number+1):
    print(i)
    sum=sum+i
print(sum)


# Exercise 5: factorials
number=int(input("Enter the number of element"))
factorial=1
for i in range(1,number+1):
    print(i)
    factorial=factorial*i
print(factorial)


# Exercise 6: While loop
num=1
while num<=10:
    print(num)
    num=num+1
#


# Functions
# Functions are of 3 types
# 1. Function without arguments
def add():
    number1=int(input("Enter the number of element"))
    number2 = int(input("Enter the number of element"))
    print(number1+number2)
add()
