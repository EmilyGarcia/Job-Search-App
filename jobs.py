from pprint import pprint
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from functools import partial
from functions import *

###################################################################################################################################
##############################################              GUI              ######################################################
###################################################################################################################################

# main gui window
master = Tk()

# enter city prompt
Label(master, text="City").grid(row=0)

# entry box
e1 = Entry(master)
e1.grid(row=0, column=1) # assigns location in master

# finds five job listings
jobs = partial(displayJobs, e1, master)
Button(master, text="Find", command=jobs).grid(row=0, column=2, sticky=W, pady=4)

# initial buttons w/ default text
b1 = Button(master, text= "Job 1", width= 40)
b1.grid(row=4, column=0, sticky=W, pady=4)
b2 = Button(master, text= "Job 2", width= 40)
b2.grid(row=5, column=0, sticky=W, pady=4)
b3 = Button(master, text= "Job 3", width= 40)
b3.grid(row=6, column=0, sticky=W, pady=4)
b4 = Button(master, text= "Job 4", width= 40)
b4.grid(row=7, column=0, sticky=W, pady=4)
b5 = Button(master, text= "Job 5", width= 40)
b5.grid(row=8, column=0, sticky=W, pady=4)

Button(master, text='Map', width= 10 command= mapThat()).grid(row=9, column=0, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit, width= 10).grid(row=9, column=1, sticky=W, pady=4)

mainloop()


