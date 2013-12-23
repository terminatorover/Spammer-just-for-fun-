from tkinter import * 
from tkinter import tkk
from tkinter import messagebox 

import smtplib 
import os 

root = Tk()
root.title("Simple E-mail client)

mainframe = ttk.Frame(root, padding = " 5 5 15 15")
mainframe.grid(column=9, row=9, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure( 0, weight=1)


def  	start_spam(*args):
	try: 
		login_user = username.get()
		login_pass = password.get()
		spam_no = spam_number.get()
		msg = message.get()
		reciver = to_adress.get()
		
		server

username = StringVar()
password = StringVar()
spamn_number = IntVar()
to_adrr = StringVar()
message = StringVar()


#labels for data entries 
ttk.Label(mainframe, text="Login Email: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Login Password: ").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Your message: ").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Spam number:").grid(column=1, row=4, sticky=W)



#data entries
username_entry = ttk.Entry(mainframe, width=7, textvariable=Username)
username_entry.grid(column=2, row=1, sticky=W)

password_entry = ttk.Entry(mainframe, width=7, textvariable=password)
password_entry.grid(column=2, row=2, sticky=W)

message_entry = ttk.Entry(mainframe, width=7, height= 20, textvariable=message)
message_entry.grid(column=2, row=3, sticky=W) 

span_entry = ttk.Entry(mainframe, width=7, textvariable=spam_number)
spam_entry.grid(column=2, row=4, sticky=W)




#get some nice paddings 
for child in mainframe.winfo_children(): child.grid_configure(padx=5 , pady=5)

username_entry.focus()
root.mainloop()



#Buttons 

ttk.Button(mainframe, text="Send", command=start). grid(column 4, row=2, sticky=W)





