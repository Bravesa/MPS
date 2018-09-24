import re
import sqlite3 as sqlt

def add_usuario():
    print("Criando novo usuário")
    nome = ""
    while re.match(r"\w+", nome) == None:
        nome = input("Digite o nome: ")
        nome.strip
    
    nome.strip()

    senha = ""

    while re.match(r"\w+", senha) == None:
        senha = input("Digite a senha: ")

    csr.execute("INSERT INTO usuarios VALUES ('{0}', '{1}')".format(nome, senha))
    print("{0} adicionado".format(nome))
    conn.commit()

conn = sqlt.connect("banco.db")

csr = sqlt.Cursor(conn)
csr.execute("CREATE TABLE IF NOT EXISTS usuarios (cadastro text, senha text)")


