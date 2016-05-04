from tkinter import *

master = Tk()

listbox = Listbox(master, selectmode=SINGLE).grid(row=3, column=2, sticky=W, pady=4)
listbox.grid()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
    
Button(master, text=listbox.get(ACTIVE)).grid(row=3, column=2, sticky=W, pady=4)

mainloop()






