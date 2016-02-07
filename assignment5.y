import time

def find_exec_time(code):
	start_time = time.clock()
	eval(code)
	t_time = time.clock() - start_time
	return t_time

def boss(n):
	i = 0
	while i < n:
		print(i)


user_input = input()
foo = eval(user_input)
print(foo)
print(find_exec_time(user_input))


#!!!!IMPORTANT - HASHING
# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
	sum = 0
	if keyword:
		for char in keyword:
			sum = sum + ord(char)

	return sum % buckets

print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11



# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hmm = []; i = 0
    while(i < nbuckets):
        hmm.append([])
        i = i + 1
    return hmm



    # Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]
        


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]