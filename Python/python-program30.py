i = True

while i == True:
    str = input("Enter string:")
    if str.istitle():
        print("The string is title case")
    if str.lower() == 'end':
        break