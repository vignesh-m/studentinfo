import tkinter
import logging

import student_info

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.roll_value = tkinter.StringVar()
        self.roll_label = tkinter.Label(self, text="Roll Number")
        self.roll_label.grid(column=0, row=0, stick='W')
        self.roll_entry = tkinter.Entry(self,textvariable=self.roll_value)
        self.roll_entry.grid(column=0,row=1,sticky='W')
        self.roll_entry.bind("<Return>", self.OnPressEnter)
        self.roll_value.set("")

        get_button = tkinter.Button(self,text="get info",
                                command=self.OnButtonClick)
        get_button.grid(column=0,row=2, sticky='W')

        self.name_value = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.name_value)
        label.grid(column=1,row=1,columnspan=2,sticky='W')
        self.name_value.set("<name>")

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.roll_entry.focus_set()
        self.roll_entry.selection_range(0, tkinter.END)

    def get_student_info(self):
        logging.debug('getting student info for %s',self.roll_value.get())
        self.student = student_info.fetch_info(self.roll_value.get())
        
        self.name_value.set(self.student.get("name","<name>"))

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
