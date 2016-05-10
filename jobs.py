from pprint import pprint
import Tkinter
from functools import partial
from functions import *

###################################################################################################################################
##############################################              GUI              ######################################################
###################################################################################################################################

# main gui window
master = Tkinter.Tk()
master.title("Job Search")
master.configure( bg='light cyan', padx = 40, pady = 30)

# title - grid 0
#Label(master, text = "JOB SEARCH AND VISUALIZATION", height = 3, fg='MediumPurple4', justify=CENTER, bg='light cyan' ).grid(row=0, column=0)

# enter city prompt - grid 1
Label(master, width = 34, height = 2, fg='MediumPurple4', bg='turquoise' ).grid(row=1, column=0, sticky=W)
Label(master, text="Enter City", width = 10, fg='MediumPurple4', bg='turquoise' ).grid(row=1, column=0, sticky=W)

# entry box - grid 1
e1 = Entry(master)
e1.configure( fg='MediumPurple4', width= 20, relief = FLAT )
e1.grid(row=1, column=0) # assigns location in master

# finds five job listings - grid 1
jobs = partial(displayJobs, e1, master)
Button(master, text="Find", command=jobs, width= 5, height = 1, fg='MediumPurple4', bg='turquoise', highlightbackground='turquoise', relief = FLAT).grid(row=1, column=0, sticky=E, pady=10)

# spacing - grid 2
Label(master, bg='light cyan').grid(row=2)

# initial buttons w/ default text - grids 4-8
b1 = Button(master, text= "Job 1", width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT)
b1.grid(row=4, column=0, sticky=W, pady=4)
b2 = Button(master, text= "Job 2", width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT)
b2.grid(row=5, column=0, sticky=W, pady=4)
b3 = Button(master, text= "Job 3", width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT)
b3.grid(row=6, column=0, sticky=W, pady=4)
b4 = Button(master, text= "Job 4", width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT)
b4.grid(row=7, column=0, sticky=W, pady=4)
b5 = Button(master, text= "Job 5", width= 40, fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT)
b5.grid(row=8, column=0, sticky=W, pady=4)

# spacing - grid 9
Label(master, bg='light cyan').grid(row=9)

# maps five jobs - grid 10
Button(master, text='Map', width= 10, command= mapThat, fg='MediumPurple4', bg='light salmon', highlightbackground='light salmon', relief = FLAT).grid(row=10, column=0, sticky=W, pady=4)
# quit - grid 10
Button(master, text='Quit', command=master.quit, width= 10, fg='MediumPurple4', bg='light salmon', highlightbackground='light salmon', relief = FLAT).grid(row=10, column=0, sticky=E, pady=4)

mainloop()


