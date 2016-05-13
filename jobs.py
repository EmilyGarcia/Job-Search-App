from pprint import pprint
import Tkinter
from functools import partial
from functions import *

###################################################################################################################################
##############################################              GUI              ######################################################
###################################################################################################################################

# Main GUI window
master = Tkinter.Tk()
master.title("Job Search")
master.configure( bg='light cyan', padx = 40, pady = 30)

# Enter city prompt - row 1
turquoiseBg = Label(master, width = 34, height = 2, fg='MediumPurple4', bg='turquoise' )
turquoiseBg.grid(row=1, column=0, sticky=W)
promptLabel = Label(master, text="Enter City", width = 10, fg='MediumPurple4', bg='turquoise' )
promptLabel.grid(row=1, column=0, sticky=W)

# Entry box - row 1
e1 = Entry(master)
e1.configure( fg='MediumPurple4', width= 20, relief = FLAT )
e1.grid(row=1, column=0) # assigns location in master

# Finds 5 job listings - row 1
jobs = partial(displayJobs, e1, master)

findBtn = Button(master, text="Find", command=jobs, width= 5, height = 1)
findBtn.configure(fg='MediumPurple4', bg='turquoise', highlightbackground='turquoise', relief = FLAT)
findBtn.grid(row=1, column=0, sticky=E, pady=4)

# Spacing - row 2
spacing1 = Label(master, text="First 5 Jobs in Search Results", fg='MediumPurple4', bg='light cyan')
spacing1.grid(row=2)

# Initial buttons w/ default text - rows 4-9
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

# Spacing - row 10
spacing2 = Label(master, bg='light cyan')
spacing2.grid(row=10)

# Map Button - row 11
mapBtn = Button(master, text='Map', command= mapThat, width= 10)
mapBtn.configure(fg='MediumPurple4', bg='light salmon', highlightbackground='light salmon', relief = FLAT)
mapBtn.grid(row=11, column=0, sticky=W, pady=4)

# Quit Button - row 11
quitBtn = Button(master, text='Quit', command=master.quit, width= 10)
quitBtn.configure(fg='MediumPurple4', bg='light salmon', highlightbackground='light salmon', relief = FLAT)
quitBtn.grid(row=11, column=0, sticky=E, pady=4)

mainloop()


