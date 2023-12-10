#!/usr/bin/env python

##############################################
# Introduction to Recursion – Data Structure
# and Algorithm
##############################################

"""
function recursively calculates the sum of natural numbers up to nth term
"""

# def sequence_sum_alt(n_term):
#     total = 0
#     for i in range(n_term):
#         total += (i + 1)
#     print(total)


# def sequence_sum(n_term):
#     if n_term == 1:
#         return 1
#     else:
#         return n_term + sequence_sum(n_term - 1)
        
    
# if __name__ == "__main__":
#     print(sequence_sum(10))


# def print_fun(test):
#     if test < 1:
#         return
#     else:
#         print(test, end=" ")
#         print_fun(test - 1) #statement 2
#         print(test, end=" ")
#         return


# Fibonacci function to get numbers up to the nth term
# def fibonacci_number(term):
#     if term == 0:
#         return 0
    
#     if term == 1 or term == 2:
#         return 1
#     else:
#         return(fibonacci_number(term - 1) + fibonacci_number(term - 2))


# if __name__ == "__main__":
#     n = 5
#     print("Fibonacci series of 5 numbers is :", end=" ")
#     for i in range(n): # The function produces the next term to the inputed term, So to get just the right numbers a range is used from 0 to n-1, hence range(n)
#         print(fibonacci_number(i), end=" ")

# Other function to get the nth term of a fibonacci series

# def fibonacci(nth_term):
#     a, b = 0, 1
#     print(f"Fibonacci series of 5 numbers is : {a}", end=" ")

#     for _ in range(nth_term - 1):
#         a, b = b, a + b
#         print(a, end=" ")
#     return a

# fibonacci(5)



# Write a program and recurrence relation to find the Factorial of n where n>2 

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#        return (num * factorial(num - 1))

    
# print(factorial(3))



##############################################
# Python Array
##############################################
# import array as arr

# # variable_name = arr.array(typecode, [elements])

# numbers = arr.array("i", [10, 20, 30])
# numbers1 = arr.array("d", [10.0, 20.0, 30.0, 40.0])
# print(len(numbers), len(numbers1))



#################################
# Linked Lists in Python
#################################

# Vertex	Linked List of Vertices
# 1     	2 → 3 → None
# 2     	4 → None
# 3     	None
# 4     	5 → 6 → None
# 5     	6 → None
# 6     	None


#  This adjacency list could also be represented in code using a dict:

graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}

# The keys of this dictionary are the source vertices,
#  and the value for each key is a list. This list is
#  usually implemented as a linked list.


# How to Use collections.deque
from collections import deque
# deque()
# print(deque())


# If you want to populate it at creation, then you can give it an iterable as input

# print(deque(["a,", "b", "c"]))
# print(deque("abc"))
# print(deque([{"data": "a"}, {"data": "b"}]))

# linked_list = deque("abcde")
# print(linked_list)
# linked_list.append("f")
# print(linked_list)
# linked_list.pop()
# print(linked_list)

# #  you can also use deque to quickly add or remove elements from the left side, or head, of the list:
# linked_list.appendleft("z")
# print(linked_list)
# linked_list.popleft()
# print(linked_list)


# How to Implement Queues and Stacks


# Queues
# queue = deque()
# print(queue)

# queue.append("Mary")
# queue.append("John")
# queue.append("Susan")
# print(queue)

# removed_member = queue.popleft()
# print(queue, removed_member)


# Stacks
# history = deque()

# history.appendleft("https://realpython.com/")
# history.appendleft("https://realpython.com/pandas-read-write-files/")
# history.appendleft("https://realpython.com/python-csv/")

# print(history)

# Now suppose that after the user read both articles, they wanted to go
#  back to the Real Python home page to pick a new article to read.
#  Knowing that you have a stack and want to remove elements using
#  LIFO, you could do the following:

# history.popleft()
# print(history)
# history.popleft()
# print(history)


