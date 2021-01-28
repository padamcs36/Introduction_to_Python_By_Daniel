'''
connecting scrollbar to the widgets
1. widget(yscrollcommand = scrollbar.set)
2. scrollbar.config(command.widget.yview)
'''
from tkinter import *
tk = Tk()
tk.geometry("300x250")
#creating scrollbar
scrollbar = Scrollbar(tk)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(tk, yscrollcommand=scrollbar.set)
# for i in range(200):
#     listbox.insert(END, f"item {i}")

text = Text(tk, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH, padx=50)

# listbox.pack()
# scrollbar.config(command=listbox.yview)
scrollbar.config(command=text.yview())
tk.mainloop()