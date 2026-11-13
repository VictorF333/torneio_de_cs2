print("=" * 30)
print(f'{"TORNEIO DE CS2":^30}')
print("=" * 30)

listaJogadores = []
listaPontuacoes = []

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
            listaJogadores.append((codigo, nome, equipe))

def cadastrarJogador():
    print("=" * 20)
    print("CADASTRAR JOGADOR")
    print("=" * 20)

    codigo = input("Codigo: ").strip()
    nome = input("Nome: ").strip().title()
    equipe = input("Equipe: ").strip().title()

    if nome == "":
        print("O nome nao pode ficar vazio!")
        return

    if codigo == "":
        print("O codigo nao pode ficar vazio!")
        return
    
    if equipe == "":
        print("O jogador nao pode ficar sem equipe!")
        return

    for jogador in listaJogadores:
        if codigo == jogador[0]:
            print("Esse código ja foi cadastrado!")
            return
    listaJogadores.append((codigo, nome, equipe))

    arquivo = open("usuarios.txt", "a")
    arquivo.write(codigo + ";" + nome + ";" + equipe + "\n")
    arquivo.close()
    print("Jogador cadastrado com sucesso!")


def listarJogadores():
    print("=" * 40)
    print(f"{"LISTA DE JOGADORES":^40}")
    print("=" * 40)

    if len(listaJogadores) == 0:
        print("Nenhum jogador cadastrado.")
        
    else:
        for jogador in listaJogadores:
            print(f"{jogador[0]},{jogador[1]},{jogador[2]}")
            
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
            print("=" * 40)
            print(f"Código: {jogador[0]}")
            print(f"Nome: {jogador[1]}")
            print(f"Equipe: {jogador[2]}")
            encontrado = True
        
    if not encontrado:
        print("Jogador não encontrado.")

def verEquipes():
    equipes = []
    for c in range(0, len(listaJogadores)):
        if listaJogadores[c][2] not in equipes:
            equipes.append((100+c, listaJogadores[c][2]))

    print("-----------------------")
    print("codigo     Equipe")
    print("-----------------------")
    for a, b in equipes:
        print(f"{a:<10} {b}")
    print("-----------------------")

def lancarPontuacao():
    codigo = int(input("O código da equipe: "))
    rodada = int(input("Rodada: "))
    valor = int(input("Pontuação: "))
    
    pass

carregarJogadores()
opcao = ""

while opcao != "0":
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("3 - Buscar jogador")
    print("4 - Ver Equipes")
    print("5 - Lançar pontuação")
    print("6 - Ver pontuações de um jogador")
    print("7 - Relatórios")
    print("0 - Sair")

    opcao = input("Sua opção: ")

    if opcao == "1":
        cadastrarJogador()

    elif opcao == "2":
        listarJogadores()

    elif opcao == "3":
        buscarJogador()

    elif opcao == "4":
        verEquipes()

if opcao == "0":
    print("Sistema encerrado!")
