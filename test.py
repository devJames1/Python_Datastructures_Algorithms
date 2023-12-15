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

###################################
# Queue Implementation using list
###################################

# queue = []
# queue.append("a")
# queue.append("b")
# queue.append("c")
# print("Initial queue")
# print(queue)
# print("\nElements dequeued from queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))
# print("\nQueue after removing elements")
# print(queue)



###################################################
# Implementation using queue.Queue
###################################################
# from queue import Queue

# q = Queue(maxsize = 3)
# print(q.qsize())
# q.put("a")
# q.put("b")
# q.put("c")
# print("\nFull: ", q.full())
# print("\nElements dequeued from the queue")
# print(q.get())
# print(q.get())
# print(q.get())
# print("\nEmpty: ", q.empty())
# q.put(1)
# print("\nEmpty: ", q.empty())
# print("\nFull: ", q.full())
# print(q.qsize())


# Implementing custom Queue class

from collections import deque

# class Queue:

#     def __init__(self):
#         self._elements = deque()
    
#     def enqueue(self, element):
#         self._elements.append(element)
    
#     def dequeue(self):
#         return self._elements.popleft()


# fifo = Queue()
# fifo.enqueue("1st")
# fifo.enqueue("2nd")
# fifo.enqueue("3rd")

# print(fifo.dequeue())
# print(fifo.dequeue())
# print(fifo.dequeue())


#  If you want, you may improve your class by making it iterable
#  and able to report its length and optionally accept initial elements: 
# 
# 
class iterableMixin:
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(iterableMixin):

    def __init__(self, *elements):
        self._elements = deque(elements)
    
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()
    

# fifo = Queue("1st", "2nd", "3rd")
# print(len(fifo))

# for element in fifo:
#     print(element)

# print(len(fifo))


# We can extend your Queue class using inheritance and override the 
# dequeue() method to remove elements from the top of the stack:
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


# lifo = Stack()
# lifo.enqueue("1st")
# lifo.enqueue("2nd")
# lifo.enqueue("3rd")

# print(lifo.dequeue())
# print(lifo.dequeue())
# print(lifo.dequeue())



# When you push a new element onto a non-empty heap, 
# it’ll end up in the right spot, maintaining the heap 
# invariant. Note that this doesn’t necessarily mean that 
# the resulting elements will become sorted
from heapq import heappush
from heapq import heappop

# fruits = []
# heappush(fruits, "orange")
# heappush(fruits, "banana")
# heappush(fruits, "apples")
# heappush(fruits, "ap")
# heappush(fruits, "app")

# print(fruits)  # ['ap', 'app', 'banana', 'orange', 'apples']
# The point of a heap isn’t so much about sorting elements
#  but rather keeping them in a certain relationship to allow
#  for quick lookup. What really matters is that the first
#  element on a heap always has the smallest (min-heap) or
#  the highest (max-heap) value, depending on how you define
#  the condition for the mentioned relationship. Python’s
#  heaps are min-heaps, which means that the first element
#  has the smallest value.


# When you pop an element from a heap, you’ll always get
#  the first one, while the remaining elements might
#  shuffle a little bit:

# print(heappop(fruits))
# print(fruits)


# Now, how do you throw priorities into the mix? The heap compares
# elements by value rather than by their priority, after all. 
# To work around this, you can leverage Python’s tuple comparison, 
# which takes into account the tuple’s components, looking from 
# left to right until the outcome is known:

# person1 = ("John", "Brown", 42)
# person2 = ("John", "Doe", 42)
# person3 = ("John", "Doe", 24)

# print( person1 < person2)
# # True
# print( person2 < person3)
# # False


##########################################
# Building a Priority Queue Data Type
##########################################
from collections import deque
from heapq import heappush, heappop

# class PriorityQueue:
#     def __init__(self):
#         self._elements = []

#     def enqueue_with_priority(self, priority, value):
#         heappush(self._elements, (priority, value))

#     def dequeue(self):
#         print(self._elements)
#         return heappop(self._elements)
    

# Unfortunately, there are a few problems with the above 
# implementation that become apparent when you try to use it:

# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on") 
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# print(messages.dequeue())

# Ultimately, it’s up to you how you want to define the order 
# of your priorities. In this tutorial, a lower priority 
# corresponds to a lower numeric value, while a higher priority has a greater value.

# Because Python’s heap is a min-heap, its first element always 
# has the lowest value. To fix this, you can flip the sign of a 
# priority when pushing a tuple onto the heap, making the 
# priority a negative number so that the highest one becomes 
# the lowest:

# class PriorityQueue:
#     def __init__(self):
#         self._elements = []

#     def enqueue_with_priority(self, priority, value):
#         heappush(self._elements, (-priority, value))

#     def dequeue(self):
#         print(self._elements)
#         return heappop(self._elements)[1]
  
    
# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on") 
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# print(messages.dequeue())


# However, there are two problems with your implementation. 
# One of them you can already see in the output, while the 
# other will only manifest itself under specific circumstances. 
# Can you spot these problems?


# Handling Corner Cases in Your Priority Queue

# To be clear, this is a direct consequence of tuple comparison
# in Python, which moves to the next component in a tuple if 
# the earlier ones didn’t resolve the comparison. So, if two 
# messages have equal priorities, then Python will compare 
# them by value, which would be a string in your example. 
# Strings follow the lexicographic order, in which the word 
# Hazard comes before the word Windshield, hence the 
# inconsistent order.

# Consider the following data class to represent messages
#  in your queue:
from dataclasses import dataclass

# @dataclass(order=True)
# class Message:
#     event: str

# wipers = Message("Windshield wipers turned on")
# hazard_lights = Message("Hazard lights turned on")
# abs_warn = Message("ABS engaged")

# print(wipers < hazard_lights)

# For example, when you enqueue a critical message and an 
# important message, Python determines their order 
# unambiguously by looking at the corresponding priorities. 
# However, as soon as you try enqueuing another critical 
# message, you’ll get a familiar error

# messages.enqueue_with_priority(CRITICAL, wipers)
# messages.enqueue_with_priority(IMPORTANT, hazard_lights) #[(-3, Message(event='Windshield wipers turned on')), (-2, Message(event='Hazard lights turned on'))]
# print(messages.dequeue()) 

# messages.enqueue_with_priority(CRITICAL, abs_warn) #Traceback (most recent call last):TypeError: '<' not supported between instances of 'Message' and 'Message'

# print(messages.dequeue()) 

# This time around, the comparison fails because two of the messages 
# are of equal priority and Python falls back to comparing them 
# by value, which you haven’t defined for your custom Message 
# class instances.
# Ths was solved by adding a keyword argument to the @dataclass(order=True) decorator like so.

# Now it can compare data objects but still doesn't sort by insertion rather than hexicographically.
# Here's another FIX that handles both situations.

# You can solve both problems—that is, the sort instability and 
# the broken tuple comparison—by introducing another component 
# to the elements stored on the heap. This extra component 
# should be comparable and represent the time of arrival. 
# When placed between the element’s priority and value in 
# a tuple, it’ll resolve the order if two elements have the 
# same priority, regardless of their values.

# You can use the count() iterator from the itertools module to 
# count from zero to infinity in a concise way:

from itertools import count

# Refactoring the Code Using a Mixin Class


class PriorityQueue(iterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]
    


# CRITICAL = 3
# IMPORTANT = 2
# NEUTRAL = 1

# messages = PriorityQueue()
# messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on") 
# messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# print(len(messages))
# for objec in messages:
#     print(objec)


##################################
# Using Queues in Practice
###################################


