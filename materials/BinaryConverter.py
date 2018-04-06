import os
import tkinter as tk
from doctest import master
import tkinter.filedialog as filedialogue
from tkinter import *
from materials import GUIconnect

class SampleApp(tk.Tk):
    data=None
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas1 = PeeredCanvas(self, width=450, height=450, border=1, relief="sunken")
        self.canvas2 = PeeredCanvas(self, width=450, height=450, border=1, relief="sunken")
        toolbar = tk.Frame(self)

        self.menuBar = Menu(master=self)
        self.filemenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="File", menu=self.filemenu )
        self.config(menu=self.menuBar)
        self.filemenu.add_command(label="Save",command=self.save)
        self.filemenu.add_command(label="Load", command=self.load)

        process_button = tk.Button(self, text="Process", command=self.proceed)
        process_button.pack(in_=toolbar, side="right",padx=15, pady=10)
        self.thresoldvalue=StringVar()
        self.e = tk.Entry(master,textvariable=self.thresoldvalue)
        self.e.insert(0, "0")
        self.e.pack(in_=toolbar, side="right",padx=0, pady=10)
        lbl=tk.Label(master, text="Select Thershold: (0-255):")
        lbl.pack(in_=toolbar, side="right",padx=50, pady=10)
        self.img_name = tk.Label(master, text="Image Name")
        self.img_name.pack(in_=toolbar, side="left", padx=175, pady=10)
        toolbar.pack(side="top", fill="x")
        self.canvas1.pack(side="left", fill="both", expand=True)
        self.canvas2.pack(side="left", fill="both", expand=True)



    def save(self):
        try:
            filename='output.txt'
            f = open(filename, 'r+')
            f.truncate()
            foo=None
            for n in self.cordinates:
                x=n[0]
                y=n[1]
                hass=n[3]
                if hass=="#ffffff":
                    b=1
                else:
                    b=0
                foo=str(x)+","+str(y)+","+str(b)+ "\n"
                with open(filename, 'a') as f:
                    f.write(foo)
        except AttributeError:
            print("Load and process file before saving")


    def load(self):
        file=filedialogue.askopenfile()
        if file != None:
            self.data = file.read()
            filepath=file.name
            self.filename=os.path.split(filepath)[1]
            file.close()
            self.img_name.config(text=self.filename)

        threshold = int(self.thresoldvalue.get())
        Listfile = open(self.filename).readlines()
        anotherlist = []
        for datas in Listfile:
            my_list = datas.split(",")
            anotherlist.append(my_list)
        del anotherlist[0]

        inputimage = GUIconnect.GUI(threshold, anotherlist)
        outputvalue = inputimage.processes()
        avgth = outputvalue[1]
        self.e.delete(0, END)
        self.e.insert(0, avgth)



    def proceed(self):
        threshold = int(self.thresoldvalue.get())
        Listfile = open(self.filename).readlines()
        anotherlist = []
        for datas in Listfile:
            my_list = datas.split(",")
            anotherlist.append(my_list)
        del anotherlist[0]

        inputimage=GUIconnect.GUI(threshold,anotherlist)
        outputvalue=inputimage.processes()
        self.cordinates=outputvalue[0]

        for item in self.cordinates:
            x=item[0]
            y=item[1]
            colorcode=item[2]
            binarycode=item[3]
            self.canvas1.create_rectangle(x, y, x, y, fill=colorcode)
            self.canvas2.create_rectangle(x, y, x, y, fill=binarycode)

class PeeredCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        self.peers = []
        tk.Canvas.__init__(self, *args, **kwargs)

app = SampleApp()
app.title("Binary Image Creator")
app.mainloop()