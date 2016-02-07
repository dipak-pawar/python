# Write Python code that prints out the number of hours in 7 weeks.

n_weeks = 7 * 24 * 7 
print(n_weeks)

# --------------------------------------
# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 383.89327

foo = str(x).find('.')
number = int(str(x)[0:foo])
float = int(str(x)[foo+1:foo+2])
if float >= 5: print(number); number = number + 1
print(number)


# ----------------------------------------------
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#word = "madam"
# test case 2
 word = "madman" # uncomment this to test

foo = 0 if (word[::-1] == word) else -1

is_palindrome = foo

print is_palindrome