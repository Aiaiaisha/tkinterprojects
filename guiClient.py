import socket 
from threading import Thread
from tkinter import *

#nickname = input("what is your name: ")
client_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8000
ip_address = "127.0.0.1"
client_server.connect((ip_address,port))

print("Connected to server")

class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.config(width=400,height=300)

        self.tls = Label(self.login,text="please login to continue",justify=CENTER,font=("Helvetica 14 bold"))
        self.tls.place(relx=0.2,rely=0.07,relheight=0.15)

        self.labelname = Label(self.login,text="Name: ",font="Helvetica 14 bold")
        self.labelname.place(relx = 0.1,rely = 0.2,relheight=0.2)
        self.entryname = Entry(self.login,font="Helvetica 14 bold")
        self.entryname.place(relx=0.35,rely=0.2,relwidth=0.4,relheight=0.12)

        self.go = Button(self.login,text="Continue",font="Helvetica 14 bold",command=lambda:self.goAhead(self.entryname.get()))
        self.go.place(relx=0.4,rely=0.55)

        self.window.mainloop()
    
    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv = Thread(target=self.recieve)
        rcv.start()

    def recieve(self):
        while True:
            try:
                message = client_server.recv(2048).decode("utf-8")
                if message == "NICKNAME":
                    client_server.send(self.name.encode("utf-8"))
                else:
                    print(message)

            except:
                print("an error ocurred")
                client_server.close()
                break



g = Gui()
