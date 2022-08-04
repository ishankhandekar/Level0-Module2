import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    ticket = ""
    ticket += str(random.randint(1,100))
    ticket += str(random.randint(1,100))
    ticket += str(random.randint(1,100))
    ticket += str(random.randint(1,100))
    ticket += str(random.randint(1,100))
    ticket += str(random.randint(1,100))
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo("Lottery Ticket","Your lottery ticket is " + ticket)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
