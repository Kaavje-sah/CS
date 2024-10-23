# WAP to input a string and print the largest word in it.
# Input: "I love Python programming"
def largest_word(s):
    words = s.split()
    max_len = max(len(word) for word in words)
    return max((word for word in words if len(word) == max_len), default=None)
print(largest_word(input("Enter a string: ")))
# Output: "programming"

# Explanation: The function splits the input string into words, finds the maximum length of words, and
# then returns the word with the maximum length. If there are multiple words with the maximum length,
# it returns the first one. The default parameter is used to handle the case when there are no
# words in the input string.