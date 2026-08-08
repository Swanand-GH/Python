#1. Write a script to perform the following three operations on given list
#Access the third element of a list
#List Length: Print the total number of items
#Check if the list is empty
#Given Input: numbers = [10, 20, 30, 40, 50]


numbers = [10, 20, 30, 40, 50]

third_element = numbers[2]
print("Third element:", third_element)

length = len(numbers)
print("Total number of items:", length)

if not numbers:
    print("The list is empty")
else:
    print("The list is not empty")
