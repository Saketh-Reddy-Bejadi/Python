from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, str(current) + str(number))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except Exception:
        entry.delete(0, END)
        entry.insert(END, "Error")

def clear():
    entry.delete(0, END)

window = Tk()
window.title("Digital Calculator")

window.configure(bg="#212121")
window.resizable(width=False, height=False)

entry = Entry(
    window, width=25, 
    borderwidth=5, 
    font=("Arial", 14),
    justify="right")
entry.grid(
    row=0,column=0, 
    columnspan=4, padx=10, 
    pady=10
    )

button_bg = "#757575"
button_fg = "#FFFFFF"
button_active_bg = "#616161"
button_active_fg = "#FFFFFF"

button_1 = Button(
    window,text="1", padx=20, 
    pady=10,bg=button_bg, fg=button_fg,
    activebackground=button_active_bg, 
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"), 
    command=lambda: button_click(1)
    )
button_2 = Button(
    window, text="2", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(2)
    )
button_3 = Button(
    window, text="3",padx=20, 
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg, 
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"), 
    command=lambda: button_click(3)
    )
button_4 = Button(
    window, text="4", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(4)
    )
button_5 = Button(
    window, text="5", padx=20, pady=10,
    bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(5)
    )
button_6 = Button(
    window, text="6", padx=20, pady=10,
    bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(6)
    )
button_7 = Button(
    window, text="7", padx=20, 
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(7)
    )
button_8 = Button(
    window, text="8", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg, 
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(8)
    )
button_9 = Button(
    window, text="9", padx=20, 
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(9)
    )
button_0 = Button(
    window, text="0", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click(0)
    )

button_add = Button(
    window, text="+", padx=19,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click("+")
    )
button_subtract = Button(
    window, text="-", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click("-")
    )
button_multiply = Button(
    window, text="*", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click("*")
    )
button_divide = Button(
    window, text="/", padx=20,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"),
    command=lambda: button_click("/")
    )
button_equals = Button(
    window, text="=", padx=42,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg, 
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"), command=calculate
    )
button_clear = Button(
    window, text="Clear", padx=28,
    pady=10, bg=button_bg, fg=button_fg,
    activebackground=button_active_bg,
    activeforeground=button_active_fg,
    font=("Arial", 12, "bold"), command=clear
    )

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equals.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

window.mainloop()
