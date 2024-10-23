string_given = "Television"
n = int(input("Position to be changed: "))
string = [d for d in str(string_given)]
for i in range(1,len(string)//n):
    if i == 1:
        string[(n-1)*i] = '_'
    else:
        string[n*i] = '_'
    
print(''.join(string))