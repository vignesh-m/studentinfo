import tkinter
import logging

from student_info import fetch_info,student_props

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.roll_value = tkinter.StringVar()
        self.roll_label = tkinter.Label(self, text="Roll Number")
        self.roll_label.grid(column=0, row=0, sticky='W')
        self.roll_entry = tkinter.Entry(self,textvariable=self.roll_value)
        self.roll_entry.grid(column=0,row=1,sticky='W')
        self.roll_entry.bind("<Return>", self.OnPressEnter)
        self.roll_value.set("")

        get_button = tkinter.Button(self,text="get info",
                                command=self.OnButtonClick)
        get_button.grid(column=0,row=2, sticky='W')

        self.student_values = {}
        self.student_labels = {}
        for i,prop in enumerate(student_props):
            self.student_values[prop] = tkinter.StringVar()
            self.student_labels[prop] = tkinter.Label(self,textvariable=self.student_values[prop])
            self.student_labels[prop].grid(column=1,row=i+1,columnspan=2,sticky='NW')
            self.student_values[prop].set("<%s>"%prop)


        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

    def get_student_info(self):
        logging.debug('getting student info for %s',self.roll_value.get())
        self.student = fetch_info(self.roll_value.get())
        for prop in student_props:
            self.student_values[prop].set(self.student.get(prop,""))

    def OnButtonClick(self):
        self.get_student_info()
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

    def OnPressEnter(self,event):
        self.get_student_info()
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

def start_gui():
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
