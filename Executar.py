import Banco

print("Bem vindo!")

inp = input("[R] - Criar registro | [C] - Consultar banco de dados | [S] - Sair\n[?]=")

while ((inp != "S") and (inp != "s")):
    
    if (inp == "R") or (inp == "r"):
        Banco.add_usuario()
    elif (inp == "C") or (inp == "c"):
        print("consultar")

    inp = input("[R] - Criar registro | [C] - Consultar banco de dados | [S] - Sair\n[?]=")