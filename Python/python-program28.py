s= input('Enter s')
c = 0
for i in s:
    if i.isalpha():
        c += 1
print("Total number of characters", c)