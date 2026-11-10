print("="*30)
print(f"{"Torneio de CS2":^30}")
print("="*30)

listaJogadores = [("victor", "calanguinhos")]

while True: 
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("3 - Buscar jogador")
    print("4 - Lançar pontuação")
    print("5 - Ver pontuações de um jogador")
    print("6 - Relatórios")
    print("0 - Sair")
    opcao = int(input("Sua opção: "))

    if opcao == 0:
        print("Fim do programa")
        break

    elif opcao == 1:
        print("="*20)
        print("Cadastrar Jogador")
        print("="*20)
        while True:
            nome = str(input("Nome: "))
            equipe = str(input("Equipe: "))
            if (nome, equipe) in listaJogadores:
                print("Esse jogador já foi cadastrado.")
                break
            else:
                print("Jogador Cadastrado com sucesso!")
                print("="*20)
                break   