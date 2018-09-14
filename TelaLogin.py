from tkinter import *
from datetime import datetime
import hashlib

class janelaLogin:
    def __init__(self):
        def validacaoLogin(event=None):
            nome = self.nomeUsuario.get()
            senha = self.senhaUsuario.get()
            senha = hashlib.sha256(senha.encode()).hexdigest()
            print(senha)
            if(nome == ""):
                self.mensagemErro.config(text='PREENCHA O CAMPO USUÁRIO')
                self.mensagemErro.grid(row=3, column=2)
                return
            if(senha == ""):
                self.mensagemErro.config(text='PREENCHA O CAMPO SENHA')
                self.mensagemErro.grid(row=3, column=2)
                return
            print(self.nomeUsuario.get(), self.senhaUsuario.get())
            self.janela.destroy()

        def printHoraAtual(label):
            def mudar():
                if self.janela.winfo_exists():
                    label["text"] = ("%02d:%02d:%02d" % (datetime.now().hour, datetime.now().minute, datetime.now().second))
                    label.after(1000, mudar)
            if self.janela.winfo_exists():
                mudar()

        self.janela = Tk()
        self.janela.title("Sistema de gerenciamento de eventos")
        self.janela.bind('<Return>', validacaoLogin)

        #largura x altura + 'distancia de pixels desde a esquerda da tela' + 'distancia de cima'
        self.janela.iconbitmap("rayquaza.ico")

        self.data = Label(self.janela, width=8, text=("%02d/%02d/%d" % (datetime.now().day,datetime.now().month,datetime.now().year)))
        self.data.grid(row=1, column=0)
        self.relogio = Label(self.janela, width=self.data["width"])
        self.relogio.grid(row=1, column=3)
        printHoraAtual(self.relogio)

        self.labelUsuario = Label(self.janela, text="Usuário", width=6)
        self.labelSenha = Label(self.janela, text="Senha", width=6)
        self.nomeUsuario = Entry(self.janela, width="30")
        self.senhaUsuario = Entry(self.janela, width="30", show="*") #caixinha de texto, .get() retorna uma string
        self.login = Button(self.janela, text="Entrar", width=12, command=validacaoLogin)
        self.logo = PhotoImage(file="logo.gif")
        self.logoLabel = Label(self.janela, image=self.logo)
        self.mensagemErro = Message(self.janela, text="", foreground="red", width="500",)

        self.logoLabel.grid(row=2,column=1, columnspan=2, ipady=20, sticky=N+S+E+W)
        self.labelUsuario.grid(row=4, column=1, sticky=N+S+E+W, ipady=1)
        self.labelSenha.grid(row=5, column=1, sticky=N+S+E+W, ipady=1)
        self.nomeUsuario.grid(row=4, column=2, sticky=N+S+E+W)
        self.senhaUsuario.grid(row=5, column=2, sticky=N+S+E+W)
        self.login.grid(row=6, column=1, columnspan=2, pady=5)


        self.janela.mainloop()










'''
textoLabel = Label(janela, justify=LEFT, padx=10, text=At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily.).grid(row=3, column=1)


Label(janela,
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "Times").grid(row=4, column=1)
Label(janela,
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").grid(row=5 ,column=1)
Label(janela,
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").grid(row=6 ,column=1)
'''