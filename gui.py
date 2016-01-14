""" GUI to display student data. """
import tkinter
import logging
from student_info import student_props
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
        self.roll_label.grid(column=0, row=0, sticky='W')
        self.roll_entry = tkinter.Entry(self, textvariable=self.roll_value)
        self.roll_entry.grid(column=0, row=1, sticky='W')
        self.roll_entry.bind("<Return>", self.on_press_enter)
        self.roll_value.set("")

        get_button = tkinter.Button(self, text="get info", command=self.on_button_click)
        get_button.grid(column=0, row=2, sticky='W')

        self.student_values = {}
        self.student_labels = {}
        for i, prop in enumerate(student_props):
            self.student_values[prop] = tkinter.StringVar()
            self.student_labels[prop] = tkinter.Label(self, textvariable=self.student_values[prop])
            self.student_labels[prop].grid(column=1, row=i+1, columnspan=2, sticky='NW')
            self.student_values[prop].set("<%s>" % prop)

        self.photo_label = tkinter.Label(self, text='<image>')
        self.photo_label.grid(column=3, row=0, columnspan=2, rowspan=4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(True, True)
        self.update()
        self.geometry(self.geometry())
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

    def get_student_info(self):
        logging.debug('getting student info for %s', self.roll_value.get())
        self.student = self.cache.fetch_info(self.roll_value.get())
        if 'photo' in self.student:
            image = ImageTk.PhotoImage(self.student['photo'])
            self.photo_label.configure(image=image)
            self.photo_label.image = image
        for prop in student_props:
            self.student_values[prop].set(self.student.get(prop, ""))

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
