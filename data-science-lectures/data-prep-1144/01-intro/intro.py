# a = {'a':2, 'a':3, 'c':10}
# print(a)

# t = (2, 3, 4)
# print(t[0])
# # tuple' object does not support item assignment
# # t[0] = 10

# for i in range(5):
#     print(i)


# print("what's your age?")

# age = int(input())

# if age >= 18:
#   print("you can vote!")
# else:
#   print("too young to vote...")

# from datetime import datetime

# hour = datetime.now().hour

# if hour < 12:
#   print("Good morning!")
# elif hour > 12:
#   print("Good afternoon!")
# elif hour >= 20:
#   print("Good night!")
# else:
#   print("Lunch time!")

# import random

# print("heads or tails?")
# choice = input()
# coin = random.choice(["heads", "tails"])

# result = (choice == coin) if "winner" else "loser"
# print(f"{result}, that was {coin}.")












# print("How old are you?")
# age = int(input())

# if age >= 18:
#   print("you can vote!")
# else:
#     print('You cannot vote :(')

from datetime import datetime

# hour = 15
# # print(hour)

# if hour < 12:
#     print('Good Morning!')
# elif hour > 12 and hour <  20:
#     print('Good afternoon!')
# elif hour >= 20:
#     print('Good Night!!!')
# else:
#     print('Lunch Time!!')

import random

print('heads or tails')
choice = input()

coin = random.choice(['heads', 'tails'])

# ternary operator
result = choice == coin if 'winner' else 'loser'



print(f'{result}, that was {coin}.')