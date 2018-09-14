import tkinter as tk

class TelaCadastro:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.iconbitmap("rayquaza.ico")
        self.janela.title = "Cadastro de usuário"

        self.labelTitulo = tk.Label(self.janela, text="Cadastrar um novo usuário", width=50)
        self.labelNome = tk.Label(self.janela, text="Nome", width=50)
        self.labelDataNascimento = tk.Label(self.janela, text="Data de Nascimento", width=50)
        self.labeCPF = tk.Label(self.janela, text="CPF", width=50)
        self.labelEndereco = tk.Label(self.janela, text="Endereço", width=50)
        self.labelTelefone = tk.Label(self.janela, text="Telefone", width=50)
        self.labelSenha = tk.Label(self.janela, text="Senha", width=50)
        self.mensagemErro = Message(self.janela, text="", foreground="red", width="500",)
        self.var = int()
        self.checkAdm = tk.Checkbutton(self.janela, text="Cadastrar como Administrador", variable=self.var)


        self.janela.mainloop()


a = TelaCadastro()
