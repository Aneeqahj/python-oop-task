# Task 1
# Easy Ticket

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x500")
window.resizable("false", "false")
window.title("Easy Ticket")
window['bg'] = "lightgreen"
variable = StringVar(window)


class Tickets:
    result = StringVar()
    variable.set("Select")

    def __init__(self, window):
        self.number = Label(window, text="Enter cell number: ", bg="lightyellow")
        self.number.place(x=100, y=50)
        self.number_entry = Entry(window, bg="lightyellow")
        self.number_entry.place(x=280, y=50)
        self.category = Label(window, text="Select Category", bg="lightyellow")
        self.category.place(x=100, y=80)
        self.option = OptionMenu(window, variable, "Soccer", "Movie", "Theater")
        self.option.place(x=280, y=80, width=100)
        self.tickets = Label(window, text="Number of Tickets: ", bg="lightyellow")
        self.tickets.place(x=100, y=130)
        self.tickets_entry = Entry(window, bg="lightyellow")
        self.tickets_entry.place(x=280, y=130)
        self.btncalc = Button(window, text="Calculate", command=self.Calculate, bg="yellow", borderwidth=5)
        self.btncalc.place(x=300, y=180, height=40)
        self.btnclear = Button(window, text="Clear", command=self.clear, bg="yellow", borderwidth=5)
        self.btnclear.place(x=40, y=450, height=40)
        self.btnexit = Button(window, text="Exit", command=self.exit, bg="yellow", borderwidth=5)
        self.btnexit.place(x=500, y=450, height=40)
        self.label1 = Label(window, width=50, height=10, text="", textvariable=self.result, bg="lightyellow")
        self.label1.place(x=100, y=230)

    def Calculate(self):
        try:
            if len(self.number_entry.get()) != 10:
                raise ValueError
            if variable.get() == "Soccer":
                sol = 40 * int(self.tickets_entry.get()) * 1.14
            elif variable.get() == "Movie":
                sol = 75 * int(self.tickets_entry.get()) * 1.14
            elif variable.get() == "Theater":
                sol = 100 * int(self.tickets_entry.get()) * 1.14
            self.result.set(sol)
        except ValueError:
            messagebox.showerror(title="Must be 10 numbers!")

    def clear(self):
        self.number_entry.delete(0, END)
        self.tickets_entry.delete(0, END)
        variable.set("Select")

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")


obj = Tickets(window)
window.mainloop()
