from tkinter import *
from datetime import datetime

class janelaLogin:
    def __init__(self):
        def validacaoLogin(event=None):
            nome = nomeUsuario.get()
            senha = senhaUsuario.get()
            if(nome == ""):
                mensagemErro.config(text='PREENCHA O CAMPO USUÁRIO')
                mensagemErro.grid(row=3, column=2)
                return
            if(senha == ""):
                mensagemErro.config(text='PREENCHA O CAMPO SENHA')
                mensagemErro.grid(row=3, column=2)
                return
            print(nomeUsuario.get(), senhaUsuario.get())
            janela.destroy()

        def printHoraAtual(label):
            def mudar():
                label["text"] = ("%02d:%02d:%02d" % (datetime.now().hour, datetime.now().minute, datetime.now().second))
                label.after(1000, mudar)
            mudar()

        janela = Tk()
        janela.title("Sistema de gerenciamento de eventos")
        janela.bind('<Return>', validacaoLogin)

        #largura x altura + 'distancia de pixels desde a esquerda da tela' + 'distancia de cima'
        janela.iconbitmap("rayquaza.ico")

        data = Label(janela, width=8, text=("%02d/%02d/%d" % (datetime.now().day,datetime.now().month,datetime.now().year)))
        data.grid(row=1, column=0)
        relogio = Label(janela, width=data["width"])
        relogio.grid(row=1, column=3)
        printHoraAtual(relogio)

        labelUsuario = Label(janela, text="Usuário", width=6)
        labelSenha = Label(janela, text="Senha", width=6)
        nomeUsuario = Entry(janela, width="30")
        senhaUsuario = Entry(janela, width="30", show="*") #caixinha de texto, .get() retorna uma string
        login = Button(janela, text="Entrar", width=12, command=validacaoLogin)
        logo = PhotoImage(file="logo.gif")
        logoLabel = Label(janela, image=logo)
        mensagemErro = Message(janela, text="", foreground="red", width="500",)

        logoLabel.grid(row=2,column=1, columnspan=2, ipady=20, sticky=N+S+E+W)
        labelUsuario.grid(row=4, column=1, sticky=N+S+E+W, ipady=1)
        labelSenha.grid(row=5, column=1, sticky=N+S+E+W, ipady=1)
        nomeUsuario.grid(row=4, column=2, sticky=N+S+E+W)
        senhaUsuario.grid(row=5, column=2, sticky=N+S+E+W)
        login.grid(row=6, column=1, columnspan=2, pady=5)


        janela.mainloop()










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