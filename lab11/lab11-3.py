import tkinter
import random
box = tkinter.Tk()
# set the size of the window, background color and title
box.geometry("300x300")
box.configure(bg="orange")
box.title("This is the title!")
# create a label
label_1 = tkinter.Label(box, text="This is a label!")
label_1.pack()
# create another label, with a different background color, font and font size
label_2 = tkinter.Label(box, text="This is another label!", bg="blue", fg="white", font=("Comic Sans MS", 16, "bold"))
label_2.pack()

box.mainloop()