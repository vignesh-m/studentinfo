""" Tk GUI for displaying student details """
from Tkinter import *
import ttk

def main():
    root = Tk()
    root.title("Student Info")

    main = ttk.Frame(root, padding="3 3 12 12")
    main.grid(0, 0, sticky=(N,W,E,S))
    main.columnconfigure(0, weight=1)
    main.rowconfigure(0, weight=1)

    roll_no = StringVar()
