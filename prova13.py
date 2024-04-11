from tkinter import *

def converter_centi_pra_metros():
    valor = entry_centimetros.get()
    if not valor.isdigit():
        label_metros.config(text='Não é um número! Tente novamente')
    centi = float(valor)
    metros = centi / 100
    label_metros.config(text=f'Conversão: {metros  } metros')
    





root = Tk()
root.title('Conversor de centímetros para metros')
root.geometry('400x250')
#Pegar a unidade de medida em centímetros
label = Label(root,text='Digite uma distância em centímetros: ',font=('Arial',10))
label.grid(row=0,column=0)
#Espaço para o usuário digitar a distância em centímetros
entry_centimetros = Entry(root)
entry_centimetros.grid(row=0,column=1)

#Resultado da conversão
label_metros = Label(root,text='',font=('Arial',10,'bold'))
label_metros.grid(row=3,column=0,columnspan=2)

#Botão que converte os dados do entry para metros
button = Button(root,text='Converter',command=converter_centi_pra_metros)
button.grid(row=1,column=0,columnspan=2)

root.mainloop()
