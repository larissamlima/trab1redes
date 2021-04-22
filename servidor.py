from tkinter import *
import time, socket, sys
 
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 7777

janela = Tk ()
 
s_ip1 = StringVar()
s_ip1.set(s_ip)

new_socket.bind((host_name, port))
lb1 = Label(janela, text="Binding successful!")
lb2 = Label(janela, text="This is your IP: ")
lb2a = Label(janela, textvariable = s_ip1)
 
#name = input('Enter name: ')
 
lb3 = Label(janela, text="Enter name: ")
name = StringVar ()
ed1 = Entry(janela, textvariable = name)

new_socket.listen(1) 
 
#conn, add = new_socket.accept()
 
#print("Received connection from ", add[0])
#print('Connection Established. Connected From: ',add[0])
 
#client = (conn.recv(1024)).decode()
#print(client + ' has connected.')
 
#conn.send(name.encode())
#while True:
#    message = input('Me : ')
#    conn.send(message.encode())
#    message = conn.recv(1024)
#    message = message.decode()
#    print(client, ':', message)

lb1.grid(row=0, column=0) 
lb2.grid(row=1, column=0)
lb2a.grid(row=1, column=1)
lb3.grid(row=3, column=0)
ed1.grid(row=3, column=1)


janela.geometry("300x300") 

janela.mainloop()
