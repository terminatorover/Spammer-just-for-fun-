from tkinter import * 
from tkinter import tkk
from tkinter import messagebox 

import smtplib 
import os 

root = Tk()
root.title("Simple E-mail client")

mainframe = ttk.Frame(root, padding = " 5 5 15 15")
mainframe.grid(column=9, row=9, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure( 0, weight=1)


def  send(*args):
    try: 
        login_username = str(username.get())
        login_password = str( password.get())
        spam_no = str(spam_number.get())
        msg = str(message.get())
        reciver = str(to_adress.get())

---------------------

        server = smtplib.SMTP('smtp.gmail.com',587)
#establish connection 
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(login_username, login_password)
        
#send mail
        server.sendmail(sender,recpient,msg)  
        nmessagebox.showinfo("Complete: You're message has been successfully sent")
        os._exit(1)

    except:
        
        messagebox.showerror("Sorry, We are not able to send you're message at this time. \n Try again Later")

   

--------------------

username = StringVar()
password = StringVar()
spamn_number = IntVar()
to_adrr = StringVar()
message = StringVar()


#labels for data entries 
ttk.Label(mainframe, text="Login Email: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Login Password: ").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Your message: ").grid(column=1, row=3, sticky=W)




#data entries
username_entry = ttk.Entry(mainframe, width=7, textvariable=Username)
username_entry.grid(column=2, row=1, sticky=W)

password_entry = ttk.Entry(mainframe, width=7, textvariable=password)
password_entry.grid(column=2, row=2, sticky=W)

message_entry = ttk.Entry(mainframe, width=7, height= 20, textvariable=message)
message_entry.grid(column=2, row=3, sticky=W) 






#get some nice paddings 
for child in mainframe.winfo_children(): child.grid_configure(padx=5 , pady=5)

username_entry.focus()
root.mainloop()



#Buttons 

ttk.Button(mainframe, text="Send", command=start). grid(column 4, row=2, sticky=W)





