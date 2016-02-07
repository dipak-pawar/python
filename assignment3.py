


# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    print(month_number)
    if len(days_in_month) >= month_number:
        return days_in_month[month_number - 1]

print(how_many_days(10))


# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list

print(countries[1][1])


# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

per = countries[0][2]/countries[2][2]
print(per)


# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'

print(stooges)

# Aliasing
# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

def replace_spy(spy):
    foo = spy
    spy[2] = foo[2] + 1
    return spy


# Define a procedure called print_all_elements that takes as input a list p and prints out every element.

def print_all_elements(number):
    i = 0
    while i < len(number):
        print(number[i])
        i = i + 1 


def fooo_for_for(list):
    for x in list:
        print(x)


#Define a procedure, sum_list, that takes as its input a list of numbers, and produces as its output
#the sum of all the elements in the input list

def sum_list(list):
    sum = 0;
    for x in list:
        sum = sum + x
    return sum

#Define a procedure, measure_udacity, that takes as its input a list of strings, and outputs a
#number that is a count of the number of elements in the input list that start with an uppercase
#letter 'U'.

def measure_udacity(list):
    count = 0
    for x in list:
        if x[0] == 'U': count = count + 1
    return count

#Define a procedure, find_element, that takes as its input a list and a value of any type, and outputs
#the index of the first element in the input list that matches the value. If there is no matching
#element, output -1.


def find_element(list, element):
    i = 0 ; length = len(list)
    while i < length:
        if list[i] == element: return i
        i = i + 1
    return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

# Using index & in
def find_element(list, value):
    if value in list: return list.index(value)
    return -1


# Define a procedure, union,that takes as inputs two lists It should modify the first input
# list to be the set union of the two lists. You may assume the first list is a set, that is, 
#it contains no repeated elements.


def union(list1, list2):
    for x in list2:
        if x not in list1: list1.append(x)
    return x 