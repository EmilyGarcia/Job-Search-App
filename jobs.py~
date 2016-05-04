#from urllib2 import urlopen
import requests
import json
from pprint import pprint
from tkinter import *
#def callback():
#    print ('City Entered')

#top = Tk()
#L1 = Label(top, text="City")
#L1.grid(row=0, column=0)
#E1 = Entry(top, bd = 5)
#E1.grid(row=0, column=1)

#MyButton1 = Button(top, text="Submit", width=10, command=callback)
#MyButton1.grid(row=1, column=1)

#top.mainloop()


def show_entry_fields():
   print("City: %s" % e1.get())

master = Tk()
Label(master, text="City").grid(row=0) #creates city prompt

e1 = Entry(master) # creates entry box

e1.grid(row=0, column=1) # assigns box location

city = e1.get()

# making request github jobs
payload = {'location': city}
ourRequest = requests.get('http://jobs.github.com/positions.json?', params=payload)
result = ourRequest.json()

#take first five jobs results
job1 = result[0]
job2 = result[1]
job3 = result[2]
job4 = result[3]
job5 = result[4]

Button(master, text='Show', command=show_entry_fields).grid(row=3, column=2, sticky=W, pady=4)

#Button(master, text= job1['title']).grid(row=4, column=0, sticky=W, pady=4)
#Button(master, text= job2['title']).grid(row=5, column=0, sticky=W, pady=4)
#Button(master, text= job3['title']).grid(row=6, column=0, sticky=W, pady=4)
#Button(master, text= job4['title']).grid(row=7, column=0, sticky=W, pady=4)
#Button(master, text= job5['title']).grid(row=8, column=0, sticky=W, pady=4)

Button(master, text='Quit', command=master.quit).grid(row=4, column=1, sticky=W, pady=4)

mainloop( )

pprint(result[0])
print(ourRequest.url)


