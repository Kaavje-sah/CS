# WAP to input a string and display the first and last character of the string.
# Input: "Hello"
def first_last_char(s):
    if len(s) > 0:
        print("First character: ", s[0])
        print("Last character: ", s[-1])
    else:
        print("String is empty")
first_last_char("Hello")
# Output: First character:  H, Last character:  o