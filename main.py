print(f'{"TORNEIO DE CS2":^30}')

listaJogadores = []

def carregarJogadores():
    arquivo = open("usuarios.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        dados = linha.strip().split(";")

        if len(dados) == 3:
            codigo = dados[0]
            nome = dados[1]
            equipe = dados[2]
            listaJogadores.append((int(codigo), nome, equipe))

def cadastrarJogador():
    print("=" * 20)
    print("CADASTRAR JOGADOR")
    print("=" * 20)

    nome = input("Nome: ").strip().title()
    equipe = input("Equipe: ").strip().title()

    if nome == "":
        print("O nome nao pode ficar vazio!")
        return

    if equipe == "":
        print("O jogador nao pode ficar sem equipe!")
        return

    for jogador in listaJogadores:
        if nome in jogador and equipe in jogador:
            print("Este jogador já foi cadastrado.")
            return

    codigo = 0
    for jogador in listaJogadores:
        if jogador[0] > codigo:
            codigo = jogador[0]
    codigo += 1

    listaJogadores.append((codigo, nome, equipe))

    arquivo = open("usuarios.txt", "a")
    arquivo.write(str(codigo) + ";" + nome + ";" + equipe + "\n")
    arquivo.close()
    print("Jogador cadastrado com sucesso!")

def listarJogadores():
    print("=" * 40)
    print(f'{"LISTA DE JOGADORES":^40}')
    print("=" * 40)

    if len(listaJogadores) == 0:
        print("Nenhum jogador cadastrado.")

    else:
        print("Equipe         Nome           Equipe")
        print("-"*40)
        for jogador in listaJogadores:
            print(f"{jogador[0]:<15}{jogador[1]:<15}{jogador[2]}")

    print("-"*40)

def buscarJogador():
    print("=" * 40)
    print("BUSCAR JOGADOR")
    print("=" * 40)

    busca = input("Digite o nome do jogador: ").strip().lower()
    encontrado = False

    if busca == "":
        print("Digite um nome para buscar.")
        return

    for jogador in listaJogadores:
        if busca in jogador[1].lower():
            print("Dados sobre o jogador:")
            print(f"Código: {jogador[0]}")
            print(f"Nome: {jogador[1]}")
            print(f"Equipe: {jogador[2]}")
            encontrado = True

    if not encontrado:
        print("Jogador não encontrado.")

def verEquipes():
    equipes = {}
    for c in range(0, len(listaJogadores)):
        if listaJogadores[c][2] not in equipes.values():
            equipes[str(100+c)] = listaJogadores[c][2]

    print("-----------------------")
    print("codigo     Equipe")
    print("-----------------------")
    for a, b in equipes.items():
        print(f"{a:<10} {b}")

def lancarPontuacao():
    print("=" * 20)
    print(f'{"Lançar Pontuação":^20}')
    print("=" * 20)

    codigo = input("O código da equipe: ").strip()
    rodada = input("Rodada: ").strip()
    valor = input("Pontuação: ").strip()

    if codigo == '' or rodada == '' or valor == '':
        print("Campo obrigatório, adicione as informações!")
        return

    arquivo = open("pontuacao.txt", "a")
    arquivo.write(codigo + ";" + rodada + ";" + valor + "\n")
    arquivo.close()
    print("Pontuação cadastrada com sucesso!")

    codigo = int(codigo)
    rodada = int(rodada)
    valor = int(valor)

def verPontuacoes():
    print("Em construção")

def relatorios():
    print("Em construção")


carregarJogadores()
opcao = ""

while opcao != "0":
    print("="*30)
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("3 - Buscar jogador")
    print("4 - Ver Equipes")
    print("5 - Lançar pontuação")
    print("6 - Ver pontuações de uma equipe")
    print("7 - Relatórios")
    print("0 - Sair")
    print("="*30)

    opcao = input("Sua opção: ")

    if opcao == "1":
        cadastrarJogador()

    elif opcao == "2":
        listarJogadores()

    elif opcao == "3":
        buscarJogador()

    elif opcao == "4":
        verEquipes()

    elif opcao == "5":
        lancarPontuacao()

    elif opcao == "6":
        verPontuacoes()

    elif opcao == "7":
        relatorios()

if opcao == "0":
    print("Sistema encerrado!")
