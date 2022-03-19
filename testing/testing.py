#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sedona Thomas"
__date__ = "03/08/2022"
__version__ = "1.0.1"
__maintainer__ = "Sedona Thomas"
__links__ = ["https://github.com/sedona-thomas/Navagetur"]
__email__ = "sedona.thomas@columbia.edu"

'''
    Attempting to create standalone GUI for application
'''


from tkinter import *
from tkhtmlview import HTMLLabel

app = Tk()
app.geometry("800x800")
with open("../website/pages/index.html") as file:
    my_label = HTMLLabel(app, html="".join([line.rstrip() for line in file]))
my_label.pack()
app.mainloop()
