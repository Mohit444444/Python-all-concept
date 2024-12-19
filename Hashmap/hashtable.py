# hashmap/hashtable 
def printk(str, k):
    HM = {}
    
    for char in str:
        if char in HM:
            HM[char] += 1
        else:
            HM[char] = 1
    
    chars = []
    for char in HM:
        if HM[char] == k:
            chars.append(char)
    return chars
  
s = "abcdab"
k = 2
print(printk(s, k))  # Output: None
