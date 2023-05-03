import random
import time
from colorama import init, Fore, Back, Style

init()

def slow_print(text):
    for char in text:
        print(Fore.BLUE + Back.WHITE + char, end=' ', flush = True)
        time.sleep(random.uniform(0.15, 0.5))
        print(Style.RESET_ALL, end=' ', flush=True)

def the_message():
    phrases = {
        "i":["I", "Me", "Myself"],
        "love": ["love", "adore", "cherish"],
        "you": ["you", "your soul", "your being"]
    }

    message = []
    for key in phrases:
        word = random.choice(phrases[key])
        message.append(word)

    return " ".join(message)

if __name__ == '__main__':
    message = the_message()
    slow_print(message)
    input()
