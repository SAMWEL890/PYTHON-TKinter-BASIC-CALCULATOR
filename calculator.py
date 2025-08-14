from tkinter import *
window = Tk()

text = Text(window,
              font=('Arial',28,'bold'),
              )

text.place(x=0, y=0, width=500, height=50)
#THE TITTLE AND THE ICON
window.title("CALCULATOR")
window.geometry('500x450')

def insert_digit(digit):
    text.insert(END, str(digit))

# Update button creation like this:
button1 = Button(window,
                text="1",
                relief=RAISED,
                command=lambda: insert_digit(1),
                padx=5,
                pady=5)
button1.place(x=0, y=50)

button2 = Button(window,
                text="2",
                relief=RAISED,
                command=lambda: insert_digit(2),
                padx=5,
                pady=5)
button2.place(x=100, y=50)

button3 = Button(window, text="3", relief=RAISED, command=lambda: insert_digit(3), padx=5, pady=5)
button3.place(x=200, y=50)


button4 = Button(window, text="4", relief=RAISED, command=lambda: insert_digit(4), padx=5, pady=5)
button4.place(x=0, y=100)

button5 = Button(window, text="5", relief=RAISED, command=lambda: insert_digit(5), padx=5, pady=5)
button5.place(x=100, y=100)

button6 = Button(window, text="6", relief=RAISED, command=lambda: insert_digit(6), padx=5, pady=5)
button6.place(x=200, y=100)

button7 = Button(window, text="7", relief=RAISED, command=lambda: insert_digit(7), padx=5, pady=5)
button7.place(x=0, y=150)

button8 = Button(window, text="8", relief=RAISED, command=lambda: insert_digit(8), padx=5, pady=5)
button8.place(x=100, y=150)

button9 = Button(window, text="9", relief=RAISED, command=lambda: insert_digit(9), padx=5, pady=5)
button9.place(x=200, y=150)

button0 = Button(window, text="0", relief=RAISED, command=lambda: insert_digit(0), padx=5, pady=5)
button0.place(x=100, y=200)

button10 = Button(window,
                text="+",
                relief=RAISED,
                command=lambda: insert_digit("+"),
                padx=5,
                pady=5)
button10.place(x=300, y=50)

button11 = Button(window,
                text="-",
                relief=RAISED,
                command=lambda: insert_digit("-"),
                padx=5,
                pady=5)
button11.place(x=300, y=100)


button12 = Button(window,
                text="/",
                relief=RAISED,
                command=lambda: insert_digit("/"),
                padx=5,
                pady=5)
button12.place(x=300, y=150)

button13 = Button(window,
                text="*",
                relief=RAISED,
                command=lambda: insert_digit("*"),
                padx=5,
                pady=5)
button13.place(x=300, y=200)

backspacebutton = Button(window,
                text="backspace",
                relief=RAISED,
                command=lambda: text.delete("end-2c", "end-1c"),
                padx=5,
                pady=5)
backspacebutton.place(x=200, y=200)

clearbutton = Button(window,
                text="clear",
                relief=RAISED,
                command=lambda: text.delete("end-100c", "end"),
                padx=5,
                pady=5)
clearbutton.place(x=350, y=200)

def calculate():
    try:
        expression = text.get("1.0", END).strip()
        result = eval(expression)
        text.delete("1.0", END)
        text.insert(END, str(result))
    except Exception:
        text.delete("1.0", END)
        text.insert(END, "Error")

equals_button = Button(window,
                text="=",
                relief=RAISED,
                command=calculate,
                padx=5,
                pady=5)
equals_button.place(x=0, y=200)

#FUNCTIONS OF THE BUTTONS


window.config(background="black")

window.mainloop()