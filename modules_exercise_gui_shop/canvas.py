from tkinter import Tk, Canvas


def create_root():
    root = Tk() # making the window
    root.title("GUI Shop")  # title of the window
    root.geometry("700x600")    # size of the window
    root.resizable(False, False)    # resize the window == False for both, horizontally and vertically

    return root


# making a frame in the window
def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)     # pin the grid to the window on 0, 0 and expanding it 700 width and 700 height

    return frame


root = create_root()    # writing the window in a variable to be easily accessible as a module
frame = create_frame()

