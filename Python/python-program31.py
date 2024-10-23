# WAP to print the following pattern:
# let's say the string inputted is Python, 
#   P n
#  y   o
# t     h
# p     n
#  y   o
#   t h

def print_pattern(s):
    length = len(s)
    
    for i in range(length):
        line = [' '] * length
        
        if i <= length // 2:
            line[i] = s[i]
            line[length - 1 - i] = s[length - 1 - i] 
            print((line))
        else:
            line[length - 1 - i] = s[i]
            line[i] = s[length - 1 - i] 
            print((line))
        
input_string = "Python"
print_pattern(input_string)

#  Output:
# P    n
#  y  o
#   th
#   ht
#  o  y
# n    P