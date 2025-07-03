from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.configure(bg="gray")
        master.resizable(False, False)

root=Tk()
root.mainloop()