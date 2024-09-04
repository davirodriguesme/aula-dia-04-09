import tkinter
from tkinter import *
#from clientess import clientesss
class Clientes:
    def __init__(self, master = None):
        self.fontep = ("arial", "10", "bold")
        self.titulo1 = Label()
        self.titulo1["text"] = "Clientes:"
        self.titulo1["font"] = ("times new roman", "13", "bold")
        self.titulo1.pack()

        self.cont6 = Frame(master)
        self.cont6["padx"] = 30
        self.cont6.pack()
        self.cli = Label(self.cont6, text="Cli_id:", font=self.fontep)
        self.idcli = Entry(self.cont6)
        self.idcli["width"] = 10
        self.b1 = Button(self.cont6, text="Buscar",command=self.buscarCliente, font=self.fontep)
        self.b1["width"] = 12
        self.cli.pack(side=LEFT)
        self.idcli.pack(side=LEFT)
        self.b1.pack(side=RIGHT)


        self.cont3 = Frame(master)
        self.cont3["padx"] = 30
        self.cont3.pack()
        self.Nome = Label(self.cont3, text="Nome:", font=self.fontep, padx= -20)
        self.idnome1 = Entry(self.cont3)
        self.idnome1["width"] = 28
        self.Nome.pack(side=LEFT)
        self.idnome1.pack(side=LEFT)


        self.cont2 = Frame(master)
        self.cont2["padx"] = 30
        self.cont2.pack()
        self.end = Label(self.cont2, text="Endereço:", font=self.fontep)
        self.idend = Entry(self.cont2)
        self.idend["width"] = 24
        self.end.pack(side=LEFT)
        self.idend.pack(side=LEFT)


        self.cont4 = Frame(master)
        self.cont4["padx"] = 30
        self.cont4.pack()
        self.tel = Label(self.cont4, text="Uf:", font=self.fontep, padx=-20)
        self.idtel = Entry(self.cont4)
        self.idtel["width"] = 26
        self.tel.pack(side=LEFT)
        self.idtel.pack(side=LEFT)

        self.cont5 = Frame(master)
        self.cont5["padx"] = 30
        self.cont5.pack()
        self.email = Label(self.cont5, text="E-mail:", font=self.fontep, padx= -20)
        self.idema = Entry(self.cont5)
        self.idema["width"] = 28
        self.email.pack(side=LEFT)
        self.idema.pack(side=LEFT)

        self.cont6 = Frame(master, padx=30)
        self.cont6.pack()
        self.bot11 = Button(self.cont6, text="Inserir", command=self.inserirCliente, font=self.fontep, width=7)
        self.bot12 = Button(self.cont6, text="Alterar", command=self.alterarCliente, font=self.fontep, width=7)
        self.bot13 = Button(self.cont6, text="Excluir", command=self.excluirCliente, font=self.fontep, width=7)
        self.bot11.pack(side=LEFT)
        self.bot12.pack(side=LEFT)
        self.bot13.pack(side=LEFT)

    def buscarCliente(self):
        idcli = self.txtidcli.get()
        resultado = self.usuario.buscar(idUsuario)
        if resultado:
            self.idcli.delete(0, Tk.END)
            self.idcli.insert(Tk.END, resultado[1])
            self.txtnome_cidade.delete(0, Tk.END)
            self.txtnome_cidade.insert(Tk.END, resultado[2])
            self.txtUf.delete(0, Tk.END)
            self.txtUf.insert(Tk.END, resultado[3])
            self.txtemail.delete(0, Tk.END)
            self.txtemail.insert(Tk.END, resultado[4])
            self.Cod_cidade.delete(0, Tk.END)
            self.Cod_cidade.insert(Tk.END, resultado[5])
            self.lblMensagem.config(text="Busca realizada com sucesso!")
        else:
            self.lblMensagem.config(text="Usuário não encontrado!")

    def inserirCliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.inserir(nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário inserido com sucesso!")

    def alterarCliente(self):
        idUsuario = self.txtIdUsuario.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.alterar(idUsuario, nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário alterado com sucesso!")

    def excluirCliente(self):
        idUsuario = self.txtIdUsuario.get()
        self.usuario.excluir(idUsuario)
        self.lblMensagem.config(text="Usuário excluído com sucesso!")

Root = Tk()
Clientes(Root)
Root.mainloop()