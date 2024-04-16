from tkinter import *

def login_correto():
    senha = entry_senha.get()
    email = entry_login.get()
    if len(senha) > 6 and '@' in email:
        msg.config(text='Login realizado com sucesso!',fg='Blue')
    else:
        msg.config(text='Email e/ou senha incorreto(s)',fg='Red')
        

root = Tk()
root.geometry('600x300')
root.title('Sistema de login')
#Parao login ser correto
correto = Label(root,text='*Na senha é obrigatório ter mais de 6 digítos',font=('Arial',8))
correto.grid(row=0,column=0)

login = Label(root,text='Digite seu email:',font=('Arial',12))
login.grid(row=1,column=0)
#Entrada para login
entry_login = Entry(root)
entry_login.grid(row=1,column=1)

senha = Label(root,text='Digite sua senha:',font=('Arial',12))
senha.grid(row=2,column=0)
#Entrada para senha
entry_senha = Entry(root)
entry_senha.grid(row=2,column=1)
#Botão de login
button = Button(root,text='Login',font=('Arial',12),command=login_correto)
button.grid(row=3,column=1,columnspan=2)
#Mensagem
msg = Label(root,text='',font=('Arial',12,'bold'))
msg.grid(row=4,column=1,columnspan=2)

root.mainloop()