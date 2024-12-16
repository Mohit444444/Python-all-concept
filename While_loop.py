# loops in python.
# loops are used to repeat instruction

# Q1- print number from 1 to 100
i = 0
while i <= 10:
    print(i)
    i += 1
    
# Q2- print number from 100 to 1 
num = 10
while num >= 1 :
    print(num)
    num -= 1

# Q3- multiplication table of a number n 
n = int(input("enter your number :"))
j = 1
while j <= 10:
    print(n,"*",j,"=", n*j)
    j += 1
    
# Q4- Print the elements of the following list using a loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx = 0 
while idx < len(nums):
    print(nums[idx])
    idx += 1
    
# Q5- Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
data = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 16
i = 0
while i < len(data):
    if (data[i]==x):  
      print("found at index :",i)
    i += 1