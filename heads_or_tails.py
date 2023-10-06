# this is a funtion that emulates the heads or tails game
import random


def heads_or_tails():
    print("Welcome to the heads or tails game!")
    coin = random.randint(1, 1000000)
    if coin % 2 == 0:
        return ("heads")
    else:
        return ("tails")


user_1 = {}
user_2 = {}
user_1["name"] = input("Enter your name:")
user_1["choice"] = input("Enter heads or tails:")
user_2["name"] = input("Enter your name:")
user_2["choice"] = input("Enter heads or tails:")
winner = heads_or_tails()
if user_1["choice"] == winner:
    print(user_1["name"] + " Wins!")
elif user_2["choice"] == winner:
    print(user_2["name"] + " Wins!")
    