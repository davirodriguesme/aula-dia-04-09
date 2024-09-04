import tkinter as tk
from tkinter import *

from cidades import cidadess
from tkinter import ttk

class Cidade:
    def __init__(self, master=None):
        self.fontep = ("arial", "10", "bold")
        self.titulo1 = Label()
        self.titulo1["text"] = "Informe os dados da sua cidade:"
        self.titulo1["font"] = ("times new roman", "13", "bold")
        self.titulo1.pack()

        self.cont2 = Frame(master)
        self.cont2["padx"] = 30
        self.cont2.pack()
        self.idcid = Label(self.cont2, text="IDcidade:", font=self.fontep)
        self.idcidai = Entry(self.cont2)
        self.idcidai["width"] = 10
        self.b1 = Button(self.cont2, text="Buscar", font=self.fontep)
        self.b1["width"] = 5
        self.idcid.pack(side=LEFT)
        self.idcidai.pack(side=LEFT)
        self.b1.pack(side=RIGHT)

        self.cont3 = Frame(master)
        self.cont3["padx"] = 30
        self.cont3.pack()
        self.Nomecidade = Label(self.cont3, text="Cidade:", font=self.fontep, padx=10)
        self.idcnome = Entry(self.cont3)
        self.idcnome["width"] = 18
        self.Nomecidade.pack(side=LEFT)
        self.idcnome.pack(side=LEFT)

        self.cont4 = Frame(master)
        self.cont4["padx"] = 30
        self.cont4.pack()
        self.uf = Label(self.cont4, text="Unidade Federal:", font=self.fontep, padx=-20)
        self.iduf = Entry(self.cont4)
        self.iduf["width"] = 11
        self.uf.pack(side=LEFT)
        self.iduf.pack(side=LEFT)

        self.cont5 = Frame(master, padx=30)
        self.cont5.pack()
        self.bot7 = Button(self.cont5, text="Inserir", command=self.inserircidade, font=self.fontep, width=5)
        self.bot8 = Button(self.cont5, text="Alterar", command=self.alterarcidade, font=self.fontep, width=5)
        self.bot9 = Button(self.cont5, text="Excluir", command=self.excluircidade, font=self.fontep, width=5)
        self.bot7.pack(side=LEFT)
        self.bot8.pack(side=LEFT)
        self.bot9.pack(side=LEFT)

        self.lblmsg = Label(master, text="", font=self.fontep)
        self.lblmsg.pack()

        self.cont6 =  Frame(master)
        self.cont6["padx"] = 30
        self.cont6.pack()

        self.tree = ttk.Treeview(self.cont6, columns=("Cod_cidade", "nome_cidade", "Uf"), show='headings')
        self.tree.heading("Cod_cidade", text="Cod_cidade")
        self.tree.heading("nome_cidade", text="nome_cidade")
        self.tree.heading("Uf", text="Uf")
        self.tree.bind("<<TreeviewSelect>>", self.buscarcidade)
        self.tree.pack()

        # Ação do botão de busca
        self.b1["command"] = self.buscarcidade


    def buscarcidade(self):
        cid = cidadess()
        Cod_cidade = self.idcidai.get()
        resultado = cid.selectcid(Cod_cidade)

        if "sucesso" in resultado:
            self.idcidai.delete(0, END)
            self.idcidai.insert(INSERT, cid.Cod_cidade)

            self.idcnome.delete(0, END)
            self.idcnome.insert(INSERT, cid.nome_cidade)

            self.iduf.delete(0, END)
            self.iduf.insert(INSERT, cid.Uf)

            self.lblmsg["text"] = "Cidade encontrada!"
        else:
            self.lblmsg["text"] = "Cidade não encontrada!"

    def inserircidade(self):
        cid = cidadess()
        cid.nome_cidade = self.idcnome.get()
        cid.Uf = self.iduf.get()
        self.lblmsg["text"] = cid.insertcid()
        self.limparcid()

    def alterarcidade(self):
        cid = cidadess()
        cid.Cod_cidade = self.idcidai.get()
        cid.nome_cidade = self.idcnome.get()
        cid.Uf = self.iduf.get()
        self.lblmsg["text"] = cid.updatecid()
        self.limparcid()

    def excluircidade(self):
        cid = cidadess()
        cid.Cod_cidade = self.idcidai.get()
        self.lblmsg["text"] = cid.deletecid()
        self.limparcid()

    def limparcid(self):
        self.idcidai.delete(0, END)
        self.idcnome.delete(0, END)
        self.iduf.delete(0, END)

root = Tk()
Cidade(root)
root.mainloop()

