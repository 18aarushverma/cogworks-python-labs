# Problem 3: Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
def is_palindrome(s):
    reg_s = []
    s = s.lower()
    s = list(s)
    for let in range(len(s)):
      if s[let].isalnum():
        reg_s.append(s[let])
    new_s = []
    for let in range(len(s)):
      if s[len(s)-let-1].isalnum():
        new_s.append(s[len(s)-let-1])
    return new_s == reg_s


assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("race a car") == False
assert is_palindrome(" ") == True
