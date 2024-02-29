# data types
A data type, in programming, is a classification that specifies which type of value a variable has and what type of mathematical, relational or logical operations can be applied to it without causing an error. 

- A string, for example, is a data type that is used to classify text 
and an integer is a data type used to classify whole numbers.
- a float is a data type used to classify decimal numbers
- a list is used to store collections of data
- A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value. values to have to but the keys have to be unique.
- Tuples are also used to store collections of data, just like Lists, Sets, and Dictionaries, all with different qualities and usage. A tuple is a collection which is ordered and it is immutable.
- The range() function returns a sequence of numbers, starting from 0 by default, and it is exlcusive - it excludes the last number

# You can check the type of an object using the type() function.
type(12) #=> int

# String
Read next slide

# Useful String Operations - read slide

# Numeric - read slide

# Special Values - read
To control the stream and outcomes of a program in the form of flow control statements, we can use a condition followed by a clause.

A condition evaluates down to a Boolean value of True or False, presenting a point where a decision is made in the program. That is, a condition would tell us if something evaluates to True or False.

# Python docs are your friend

# Variables
read next slide

# Functions
A function is a block of code that performs a task. It can be called and reused multiple times. You can pass information to a function and it can send information back. Many programming languages have built-in functions that you can access in their library, but you can also create your own functions

# Problem 
Ask what the problem is here. How can we fix it? what is the solution here?

# Solution: a function - code slide

# Why functions? - code slide

# Control Flow

# Basic flow is top to bottom, line-by-line
print("How old are you?")
age = int(input())

if age >= 18:
  print("you can vote!")

# if / else
print("what's your age?")

age = int(input())

if age >= 18:
  print("you can vote!")
else:
  print("too young to vote...")

# if / elif / else
from datetime import datetime

hour = datetime.now().hour

if hour < 12:
  print("Good morning!")
elif hour > 12:
  print("Good afternoon!")
elif hour >= 20:
  print("Good night!")
else:
  print("Lunch time!")

# Ternary operator
import random

print("heads or tails?")
choice = input()
coin = random.choice(["heads", "tails"])

result = (choice == coin) if "winner" else "loser"
print(f"{result}, that was {coin}.")

# Multiple conditions - AND - read

# Multiple conditions - OR - read