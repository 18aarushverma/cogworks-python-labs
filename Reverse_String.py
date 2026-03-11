# Problem 2: Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.

def reverse_string(s):
  s = list(s)
  new_s = []
  for let in range(len(s)):
    new_s.append(s[len(s)-let-1])
  return new_s

s1 = ["h","e","l","l","o"]
reverse_string(s1)
