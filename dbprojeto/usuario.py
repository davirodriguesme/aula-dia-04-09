from Banco import Banco
from tkinter import *

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO tbl_usuarios (Nome, Telefone, email, usuario, senha)
            VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {str(e)}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE tbl_usuarios SET Nome=?, Telefone=?, email=?, usuario=?, senha=?
            WHERE idusuario=?
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {str(e)}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_usuarios WHERE idusuario=?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {str(e)}"

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios WHERE idusuario=?", (idusuario,))
            row = c.fetchone()
            if row:
                self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha = row
                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Usuário não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {str(e)}"
