#  WAP to input a string and display not vowel element of the string
#  Input: "Python is fun"
#  Output: "Pythn s fn"

vowels=['a','e','i','o','u']
def not_vowel(s):
    return ''.join([i for i in s if i.lower() not in vowels])
print(not_vowel(input('Enter a string')))
