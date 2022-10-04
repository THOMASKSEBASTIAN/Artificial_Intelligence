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



# Exercise 3: Print characters from a string that are present at an even index number

Name=input("Enter the Name")
for i in Name:
    index=Name.find(i)
    # print(index)
    if index % 2==0:
        print(i)


