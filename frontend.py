# this will be for the frontend
from tkinter import *
from tkinter import ttk

class Front:

    def __init__():
        # create main window
        root = Tk()
        root.minsize(640,480)
        root.maxsize(1920,1080)

        # create labels
        accLabel = Label(root, text="Accounts")
        amtLabel = Label(root, text="Amount")
        cbLabel = Label(root, text="Cash Back")

        # position labels
        accLabel.grid(row=0, column=0)
        amtLabel.grid(row=0, column=20)
        cbLabel.grid(row=0, column=40)


        # keeps main frame running
        root.mainloop()


if __name__ == '__main__':
    Front.__init__()