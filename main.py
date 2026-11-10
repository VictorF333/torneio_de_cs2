import tkinter as tk

# metadados da janela

janela = tk.Tk()
janela.title("Torneio de CS2")
janela.geometry("500x400")

# definição dos frames

listaJogadores = [("victor", "calanguinhos")]

menu = tk.Frame(janela)
menu.pack()
frame_cadastroJogador = tk.Frame(janela)
frame_listaJogadores = tk.Frame(janela)
frame_buscaJogador = tk.Frame(janela)
frame_lancarPontuacoes = tk.Frame(janela)
frame_verPontuacoes = tk.Frame(janela)
frame_relatorios = tk.Frame(janela)

# Menu inicial e botões funcionais

tk.Label(menu, text="=== Torneio IFRN de CS2 ===").pack()
tk.Label(menu, text="Bem vindo ao programa do Torneio Oficial de CS2 do IFRN!").pack()


def cadastrar_jogador():
  menu.pack_forget()
  frame_cadastroJogador.pack()
  botao_voltar.pack()

def listar_jogadores():
  menu.pack_forget()
  frame_listaJogadores.pack()
  botao_voltar.pack()

def buscar_jogador():
  menu.pack_forget()
  frame_buscaJogador.pack()
  botao_voltar.pack()

def lancar_pontuacoes():
  menu.pack_forget()
  frame_lancarPontuacoes.pack()
  botao_voltar.pack()

def ver_pontuacoes_jogador():
  menu.pack_forget()
  frame_verPontuacoes.pack()
  botao_voltar.pack()

def relatorios():
  menu.pack_forget()
  frame_relatorios.pack()
  botao_voltar.pack()

def voltar_tela_anterior():
  botao_voltar.pack_forget()
  listaFremes = [frame_cadastroJogador,frame_listaJogadores,frame_buscaJogador,frame_lancarPontuacoes,frame_verPontuacoes,frame_relatorios]
  for a in listaFremes:
    a.pack_forget()
  menu.pack()


tk.Button(menu, text="Cadastrar jogador", command=cadastrar_jogador).pack()
tk.Button(menu, text="Listar jogadores", command=listar_jogadores).pack()
tk.Button(menu, text="Buscar jogador", command=buscar_jogador).pack()
tk.Button(menu, text="Lançar pontuação", command=lancar_pontuacoes).pack()
tk.Button(menu, text="Ver pontuações de um jogador", command=ver_pontuacoes_jogador).pack()
tk.Button(menu, text="Relatórios", command=relatorios).pack()
botao_voltar = tk.Button(janela, text="Voltar ao menu", command=voltar_tela_anterior)

# Cadastrar Jogador

tk.Label(frame_cadastroJogador, text="Cadastrar Jogador").pack()
nick_entry = tk.Entry(frame_cadastroJogador)
equipe_entry = tk.Entry(frame_cadastroJogador)
tk.Label(frame_cadastroJogador, text="Nome do jogador").pack()
nick_entry.pack()
tk.Label(frame_cadastroJogador, text="Equipe ao qual pertence").pack()
equipe_entry.pack()


def cadastrar():
  nick = nick_entry.get()
  equipe = equipe_entry.get()
  if (nick, equipe) in listaJogadores:
    mensagem["text"] = "Este jogador já está cadastrado."
  elif (nick, equipe) == ("",""):
    mensagem["text"] = "Por favor, insira os dados nas caixas de texto para poder continuar."
  else:
    mensagem["text"] = "Jogador cadastrado com sucesso!"
  mensagem.pack()

mensagem = tk.Label(frame_cadastroJogador, text="")
tk.Button(frame_cadastroJogador, text="Cadastrar", command=cadastrar).pack()

# Listar Jogadores

# Buscar Jogadores

# Lanças Pontuações

# Ver Pontuações de um jogador

# Relatórios


janela.mainloop()