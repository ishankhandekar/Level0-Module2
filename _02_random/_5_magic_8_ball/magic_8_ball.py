import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring("Magic 8 ball","Ask a question")
    # Make a variable and initialize it to a random number between 0 and 3
    rand = random.randint(0,3)
    # If the random number is 0
    if rand == 0:
        messagebox.showinfo("Magic 8 ball","Yes")
        # tell the user "Yes"

    # If the random number is 1
    elif rand == 1:
        messagebox.showinfo("Magic 8 ball","No")
        # tell the user "No"

    # If the random number is 2
    elif rand == 2:
        messagebox.showinfo("Magic 8 ball","Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    elif rand == 3:
        messagebox.showinfo("Magic 8 ball","I don't know the answer to this question.")
        # write your own answer
