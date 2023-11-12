import tkinter
import random
box = tkinter.Tk()
# define a function that will be called when the button is pressed, change the text of label_1
def press():
    label_1.configure(text="You pressed the button!")
# define another function that will be called when the button is pressed, change the text of label_1 and display a random number in label_2
def press2():
    label_1.configure(text="here is a random number: ")
    label_2.configure(text=random.randint(1, 100))
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
# create a button
button_1 = tkinter.Button(box, text="This is a button!", command=press)
button_1.pack()
# create another button, with a different background color, font and font size
button_2 = tkinter.Button(box, text="This is another button!", bg="blue", fg="white", font=("Comic Sans MS", 16, "bold"), command=press2)
button_2.pack()

box.mainloop()