# a = {'a':2, 'a':3, 'c':10}
# print(a)

# t = (2, 3, 4)
# print(t[0])
# # tuple' object does not support item assignment
# # t[0] = 10

# for i in range(5):
#     print(i)

# print("How old are you?")
# age = int(input())

# if age >= 18:
#   print("you can vote!")

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

# STOP_MESSAGE = "I am going to work right now!"

# def coach_answer(your_message):
#   if your_message == STOP_MESSAGE or your_message == STOP_MESSAGE.upper():
#     ""
#   elif your_message.ends_with("?"):
#     "Silly question, get dressed and go to work!"
#   else:
#     "I don't care, get dressed and go to work!"
    
# def coach_answer_enhanced(your_message):
#     answer = coach_answer(your_message)
#     if answer == "":
#         ""
#     elif your_message.upcase == your_message:
#         "I can feel your motivation! #{answer}"
#     else:
#         return answer

def is_uppercase(inp):
    has_symbol = any(ch in "!@#$%¨&*()_+-=?/<,>.:;^~`´" for ch in inp)
    if has_symbol:
        return has_symbol
    else:
        return inp.isupper()

print(is_uppercase('&$&'))