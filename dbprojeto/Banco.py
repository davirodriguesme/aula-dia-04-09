import sqlite3

class Banco:
    def __init__(self):
        # Conecta ao banco de dados (cria o arquivo 'banco.db' se ele não existir)
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''
                    CREATE TABLE IF NOT EXISTS tbl_cidade(
                        Cod_cidade INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_cidade TEXT NOT NULL,
                        Uf TEXT NOT NULL
                    )
        ''')

        c.execute('''
                    CREATE TABLE IF NOT EXISTS tbl_clientes (
                    idcli INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_cidade TEXT,
                    Uf TEXT,
                    email TEXT,
                    Cod_cidade INTEGER,
                    FOREIGN KEY (Cod_cidade) REFERENCES cidadess(Cod_cidade)
                    )
        ''')
        c.execute('''
                    CREATE TABLE IF NOT EXISTS tbl_usuarios (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Telefone TEXT,
                    email TEXT,
                    usuario TEXT NOT NULL,
                    senha TEXT NOT NULL
                    )
                    ''')
        self.conexao.commit()  # Confirma a criação da tabela

    def fechar_conexao(self):
        self.conexao.close()