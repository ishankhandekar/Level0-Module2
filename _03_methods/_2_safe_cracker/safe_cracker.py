import random
import sys
from tkinter import messagebox, Tk
from playsound import playsound


def crack_the_safe():
    pass
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations
    for i in range(999000,999999):
        try_code(i)


# ======================= DO NOT EDIT THE CODE BELOW =========================

wekncrzpasfdkjhcfjse = random.randint(0, 999)


def try_code(guess):
    print("trying " + str(guess))

    secret_code = 999999 - wekncrzpasfdkjhcfjse

    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        play_the_sound_of_success()
        sys.exit(0)


def play_the_sound_of_success():
    playsound('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_2_safe_cracker/me-gusta.wav')


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
