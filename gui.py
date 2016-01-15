""" GUI to display student data. """
import tkinter
from tkinter import W, N, E, S
import logging
from student_info import student_props, student_display_props
from PIL import ImageTk


class App(tkinter.Tk):
    def __init__(self, parent, info_cache):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.cache = info_cache
        self.initialize()

    def initialize(self):
        self.grid()

        self.roll_value = tkinter.StringVar()
        self.roll_label = tkinter.Label(self, text="Roll Number")
        self.roll_label.grid(column=0, row=0, sticky=W)
        self.roll_entry = tkinter.Entry(self, textvariable=self.roll_value)
        self.roll_entry.grid(column=0, row=1, sticky=W)
        self.roll_entry.bind("<Return>", self.on_press_enter)
        self.roll_value.set("")

        get_button = tkinter.Button(self, text="get info", command=self.on_button_click)
        get_button.grid(column=0, row=2, sticky=W)

        self.student_values = {}
        self.student_labels = {}
        self.student_disps = {}
        for i, prop in enumerate(student_props):
            self.student_values[prop] = tkinter.StringVar()
            self.student_disps[prop] = tkinter.Label(self, text=student_display_props[i]+' : ')
            self.student_labels[prop] = tkinter.Label(self, textvariable=self.student_values[prop])
            self.student_labels[prop].grid(column=2, row=i, sticky=E+W)
            self.student_disps[prop].grid(column=1, row=i, sticky=E+W)
            self.student_values[prop].set("")

        self.photo_label = tkinter.Label(self, text='<image>')
        self.photo_label.grid(column=3, row=0, columnspan=2, rowspan=7, sticky=N+S+E+W)

        self.error_msg = tkinter.StringVar()
        self.error_msg.set("")
        self.error_msg_label = tkinter.Label(self, textvariable=self.error_msg)
        self.error_msg_label.grid(column=0, row=3, rowspan=4, sticky=N+S+E+W)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)
        self.grid_columnconfigure(4, weight=2)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

    def get_student_info(self):
        logging.debug('getting student info for %s', self.roll_value.get())
        try:
            self.student = self.cache.fetch_info(self.roll_value.get())
            self.error_msg.set("")
            if 'photo' in self.student:
                image = ImageTk.PhotoImage(self.student['photo'])
                self.photo_label.configure(image=image)
                self.photo_label.image = image
            else:
                self.error_msg.set("Error: \nNo photo available")
            for prop in student_props:
                self.student_values[prop].set(self.student.get(prop, ""))
        except ValueError:
            self.error_msg.set("Error: \nInvalid Roll Number")

    def on_button_click(self):
        self.get_student_info()
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

    def on_press_enter(self, event):
        self.get_student_info()
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)


def start_gui(cache):
    app = App(None, cache)
    app.title('Student Info')
    app.mainloop()
