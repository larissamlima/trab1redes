from tkinter import *
import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 7777

janela = Tk ()

ip1 = StringVar()
ip1.set(ip)

lb1 = Label(janela, text="This is your IP address: ")
lb1a = Label(janela, textvariable = ip1)
lb2 = Label(janela, text="Enter friend's IP address: ")

ed1 = Entry(janela, textvariable = server_host)

##################isso aqui foi só pra eu testar

#lb4 = Label(janela, textvariable = server_host)
#lb4 = Label(janela, textvariable = name)

lb3 = Label(janela, text="Enter Friend's name: ")
name = StringVar ()
ed2 = Entry(janela, textvariable = name)

################### essa é a parte do Fusca que eu não consegui colocar na interface #help

#socket_server.connect((server_host, sport))


#name1 = name.get()

#socket_server.send(name1.encode())
#server_name = socket_server.recv(1024)
#server_name = server_name.decode()


############# isso foi um teste mas não funciona e eu não sei como faz de verdade KKKKKKKKKKKKKKK

#lb5 = Label(janela, textvariable = name + ' has joined...' )


#while True:
#    message = (socket_server.recv(1024)).decode()
#    print(server_name, ":", message)
#    message = input("Me : ")
#    socket_server.send(message.encode())  


lb1.grid(row=0, column=0) 
lb1a.grid(row=0, column=1)
lb2.grid(row=1, column=0)

lb3.grid(row=2, column=0)
#lb4.grid(row=4, column=0)
#lb5.grid(row=4, column=0)

ed1.grid(row=1, column=1)
ed2.grid(row=2, column=1)


janela.geometry("300x300+100+100") 

janela.mainloop()
