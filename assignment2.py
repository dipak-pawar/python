def square(n):
	return n * n

print(square(5))

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum(a,b,c):
	return a + b + c


# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.



def bigger(a,b):
    if a>b:
        return a
    return b


# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'


def is_friend(name):
   	if (name[0] == 'D') | (name[0] == 'N'):
   		return True;
	return False;


# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.
def biggest(a,b,c):
    if a >= b:
        if a >= c:
            return a
        return c
    elif a < b:
        if b > c:
            return b
        return c

print biggest(6, 7, 7)

print biggest(6, 9, 3)

print biggest(7, 3, 3)

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    no = 1;
    while(no <= n):
        print(no)
        no = no + 1


# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    if(n == 0):
        return 1
    number = n * factorial(n-1)
    return number


# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if (day == 'Saturday') | (day == 'Sunday'):
        return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False


def stamps(n):
    p_five = 0; p_two = 0; p_one = 0
    if n == 0:
        return p_five,p_two, p_one
    p_five = n // 5
    p_rem = (n % 5)
    if p_rem != 0:
        p_two = p_rem // 2
        p_two_rem = (p_rem % 2)
        if p_two_rem != 0:
            p_one = p_two_rem // 1
    return p_five, p_two, p_one

print(stamps(5))
print(stamps(8))
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print(stamps(29))
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print(stamps(0))
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps