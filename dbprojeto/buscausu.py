from tkinter import *
from tkinter import ttk

from usuario import Usuarios
import os
import sys


class Busca:
    def __init__(self, master=None):
        self.fontep = ("arial", "10", "bold")

        # Título
        self.titulo1 = Label(master, text="Informe os dados:", font=("times new roman", "13", "bold"))
        self.titulo1.pack()

        # Campo de busca por ID
        self.cont2 = Frame(master, padx=30)
        self.cont2.pack()
        self.idusu = Label(self.cont2, text="IDusuario:", font=self.fontep)
        self.idinfo = Entry(self.cont2, width=10)
        self.b1 = Button(self.cont2, text="Buscar", font=self.fontep, width=6)
        self.idusu.pack(side=LEFT)
        self.idinfo.pack(side=LEFT)
        self.b1.pack(side=RIGHT)

        # Campos de dados do usuário
        self.cont3 = Frame(master, padx=30)
        self.cont3.pack()
        self.Nome = Label(self.cont3, text="Nome:", font=self.fontep, padx=-20)
        self.idnome = Entry(self.cont3, width=27)
        self.Nome.pack(side=LEFT)
        self.idnome.pack(side=LEFT)

        self.cont4 = Frame(master, padx=30)
        self.cont4.pack()
        self.tel = Label(self.cont4, text="Telefone:", font=self.fontep, padx=-20)
        self.idtel = Entry(self.cont4, width=24)
        self.tel.pack(side=LEFT)
        self.idtel.pack(side=LEFT)

        self.cont5 = Frame(master, padx=30)
        self.cont5.pack()
        self.email = Label(self.cont5, text="E-mail:", font=self.fontep, padx=-20)
        self.idema = Entry(self.cont5, width=26)
        self.email.pack(side=LEFT)
        self.idema.pack(side=LEFT)

        self.cont6 = Frame(master, padx=30)
        self.cont6.pack()
        self.usuario = Label(self.cont6, text="Usuário:", font=self.fontep, padx=-20)
        self.idusa = Entry(self.cont6, width=25)
        self.usuario.pack(side=LEFT)
        self.idusa.pack(side=LEFT)

        self.cont7 = Frame(master, padx=30)
        self.cont7.pack()
        self.senha = Label(self.cont7, text="Senha:", font=self.fontep, padx=-20)
        self.idsen = Entry(self.cont7, show="*", width=26)
        self.senha.pack(side=LEFT)
        self.idsen.pack(side=LEFT)

        # Botões de ação
        self.cont8 = Frame(master, padx=30)
        self.cont8.pack()
        self.bot2 = Button(self.cont8, text="Inserir", command=self.inserirUsuario, font=self.fontep, width=7)
        self.bot3 = Button(self.cont8, text="Alterar", command=self.alterarUsuario, font=self.fontep, width=7)
        self.bot4 = Button(self.cont8, text="Excluir", command=self.excluirUsuario, font=self.fontep, width=7)
        self.bot2.pack(side=LEFT)
        self.bot3.pack(side=LEFT)
        self.bot4.pack(side=LEFT)

        # Mensagem de retorno
        self.lblmsg = Label(master, text="", font=self.fontep)
        self.lblmsg.pack()

        # Ação do botão de busca
        self.b1["command"] = self.buscarUsuario

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.cont9 = Frame(master)
        self.cont9["padx"] = 20
        self.cont9.pack(pady=10)

        self.tree = ttk.Treeview(self.cont9, columns=("Id", "nome", "Telefone", "email", "usuario", "senha"),
                                 show="headings")
        self.tree.heading("Id", text="idusuario")
        self.tree.heading("nome", text="nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("email", text="email")
        self.tree.heading("usuario", text="usuario")
        self.tree.heading("senha", text="senha")
        self.tree.bind('<<TreeviewSelect>>', self.selecionausuario)
        self.tree.pack()

        self.atualizarTabela()

    def atualizarTabela(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4], u[5]))

    def Selecionarusuario(self):
        user = Usuarios
        idusuario = self.idusuario.get()
        self.Authentic["text"] = user.selectUser(idusuario)
        self.idusuario.delete(0, END)
        self.idusuario.insert(INSERT, user.idusuario)
        self.nome.delete(1, END)
        self.nome.insert(INSERT, user.Nome)
        self.telefone.delete(2, END)
        self.telefone.insert(INSERT, user.Telefone)
        self.email.delete(3, END)
        self.email.insert(INSERT, user.email)
        self.usuario.delete(4, END)
        self.usuario.insert(INSERT, user.usuario)
        self.senha.delete(5, END)
        self.senha.insert(INSERT, user.senha)

    def selecionausuario(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')
            self.idinfo.delete(0, END)
            self.idinfo.insert(INSERT, values[0])
            self.idnome.delete(0, END)
            self.idnome.insert(INSERT, values[1])
            self.idtel.delete(0, END)
            self.idtel.insert(INSERT, values[2])
            self.idema.delete(0, END)
            self.idema.insert(INSERT, values[3])
            self.idusa.delete(0, END)
            self.idusa.insert(INSERT, values[4])
            self.idsen.delete(0, END)
            self.idsen.insert(INSERT, values[5])

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idinfo.get()
        self.lblmsg["text"] = user.selectUser(idusuario)
        self.idinfo.delete(0, END)
        self.idinfo.insert(INSERT, user.idusuario)
        self.idnome.delete(0, END)
        self.idnome.insert(INSERT, user.nome)
        self.idtel.delete(0, END)
        self.idtel.insert(INSERT, user.telefone)
        self.idema.delete(0, END)
        self.idema.insert(INSERT, user.email)
        self.idusa.delete(0, END)
        self.idusa.insert(INSERT, user.usuario)
        self.idsen.delete(0, END)
        self.idsen.insert(INSERT, user.senha)
        self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.idnome.get()
        user.telefone = self.idtel.get()
        user.email = self.idema.get()
        user.usuario = self.idusa.get()
        user.senha = self.idsen.get()
        self.lblmsg["text"] = user.insertUser()
        self.limparCampos()
        self.atualizarTabela()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idinfo.get()
        user.nome = self.idnome.get()
        user.telefone = self.idtel.get()
        user.email = self.idema.get()
        user.usuario = self.idusa.get()
        user.senha = self.idsen.get()
        self.lblmsg["text"] = user.updateUser()
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idinfo.get()
        self.lblmsg["text"] = user.deleteUser()
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        """Função para limpar os campos após uma operação."""
        self.idinfo.delete(0, END)
        self.idnome.delete(0, END)
        self.idtel.delete(0, END)
        self.idema.delete(0, END)
        self.idusa.delete(0, END)
        self.idsen.delete(0, END)

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')


root = Tk()
app = Busca(master=root)
root.mainloop()
