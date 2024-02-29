from random import randint
from tkinter import *
from tkinter import Listbox

janela = Tk()
janela.geometry('500x600')

lista_b = Listbox(janela, font=15)
lista_b.place(x=1, y=0, width=200, height=350)

escrolar_y = Scrollbar(janela, orient=VERTICAL, command=lista_b.yview) #SCROLLBARS \/
escrolar_y.place(x=201, y=0, height=350)
escrolar_x = Scrollbar(janela, orient=HORIZONTAL, command=lista_b.xview)
escrolar_x.place(x=0, y=351, width=200) #  /\
lista_b.configure(yscrollcommand=escrolar_y.set, xscrollcommand=escrolar_x.set) #configuração

i = StringVar()
i_en = Entry(janela, textvariable=i)
i_en.place(x=243, y=1, width=239, height=40)

sorteado = Label(janela, text="---")
sorteado.place(x=250, y=490)


def inserir():
    lista_b.insert(END, i.get())


def sortea():
    aleatorio = randint(0, lista_b.size()-1)

    sorteado.configure(text=lista_b.get(aleatorio))


def deleta():
    lista_b.delete(lista_b.curselection())


def deleta_tudo():
    lista_b.delete(0, lista_b.size())


def inserir_antes():
    lista_b.insert(lista_b.curselection(), i.get())
    lista_b.selection_clear(0, END)


b_inserir = Button(janela, text='inserir', background="#03babb", command=inserir)
b_inserir.place(x=260, y=75, width=50)

b_sortea = Button(janela, text="sortea", command=sortea)
b_sortea.place(x=100, y=395, width=46, height=30)

b_del = Button(janela, text="deleta", bg="#ca0000", command=deleta)
b_del.place(x=350, y=75)

b_delt = Button(janela, text="deletar tudo", bg="#cc0000", command=deleta_tudo)
b_delt.place(x=350, y=111)

b_ina = Button(janela, text="inserir antes", bg="#11babb", command=inserir_antes)
b_ina.place(x=260, y=111)

janela.mainloop()