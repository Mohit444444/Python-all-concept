#  for loops in python

# print the element of the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

data = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for val in data :
    print(val) 
    
# Search for a number x in this tuple using loop:
#[1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 25
idx = 0
for data in nums:
    if(data==x):
        print("number found at idx",idx)
    idx += 1
    
# range in python
for el in range(1, 10):
    print(el)