import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound
from easygui import *

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.
    while(True):
        choice = ["Cow","Duck","Dog","Cat","Llama"]
        output = choicebox("What animals do you want to see and hear?","Animal Farm",choice)
        if output == "Cow":
            moo()
        elif output == "Cat":
            meow()
        elif output == "Dog":
            woof()
        elif output == "Duck":
            quack()
        elif output == "Llama":
            llama_scream()
        choice1 = ["Yes","No"]
        output = choicebox("Do you want to see or hear another animal?","Animal Farm",choice1)
        if output == "No":
            quit()
    
    # TODO 2. Make it so that the user can keep entering new animals.

    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    show_image('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/cow.jpg')
    playsound('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/moo.wav')


def quack():
    show_image('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/duck.jpg')
    playsound('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/quack.wav')


def woof():
    show_image('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/dog.jpg')
    playsound('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/woof.wav')


def meow():
    playsound('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/meow.wav')
    show_image('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/cat.jpg')


def llama_scream():
    show_image('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/llama.jpg')
    playsound('C:/Users/Ishan Khandekar/Documents/GitHub/Level0-Module2/_03_methods/_1_animal_farm/llama.wav')


if __name__ == '__main__':
    animals()
