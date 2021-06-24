import random
import os
import numpy as np
z = 0
x = []
casas_envenenadas = []
y = 0
i = 0
posicao_tabu = 1
inimigo = 2
jogador = 0
hero = "O"
veneno = False
antidoto = 1
def dados(x = 0,mini=1,maxi=7):
  x = random.randrange(mini,maxi)
  return x
#função do tabuleiro
def tabuleiro(casas = [],i=0,posicao=1,posicao_2=2,hero = "O",dif=0,x=0):  
  try: 
    if (len(casas) < 29):
      for i in range(32):        
        casas.append("_")

    if (casas[1] == "X"):
      for i in range(28):
        casas[i+2] = "_"
    if (posicao-1 < posicao_2-1):
      for i in range (posicao-1):
        casas[i] = "_" 
      dif = posicao
      for dif in range (posicao_2):
       casas[dif] = "_"
    if (posicao_2-1 < posicao-1):
       for i in range (posicao_2-1):
         casas[i] = "_" 
       dif = posicao_2
       for dif in range (posicao):
         casas[dif] = "_"
    if (posicao == posicao_2):
      posicao += 1
      for i in range (posicao_2-1):
       casas[i] = "_" 
    casas[posicao-1] = hero
    casas[posicao_2-1] = "X"
    casas = casas[0:10],casas[10:20],casas[20:30]
    casas = np.array(casas)   
    return casas
  except:
    return print("Valor inválido! erro na função tabuleiro.")

print("Use: 1 - Jogar dado.\t2 - Usar antidoto (1).\t3 - Sair.\n5 casas foram envenenadas ao acaso, você possui apenas 1 antidoto, boa sorte.\n")
print(tabuleiro())
#sorteando casas envenenadas
for i in range (5):
 casas_envenenadas.append(dados(0,2,30))
#inicio da brincadeira
while (posicao_tabu < 30 and inimigo < 30):
  try:
   jogador = int(input("\njogador: "))
   if (jogador == 1):
    if (posicao_tabu < 30 and inimigo < 30):
     if (veneno == True):
      hero = "C"
      posicao_tabu += dados(0,1,5)
      inimigo += dados()
     if (veneno == False):
      hero = "O"
      posicao_tabu += dados()
      inimigo += dados()
      for i in range (5):
       if (posicao_tabu == casas_envenenadas[i]):
        veneno = True
        hero = "C"
    if(posicao_tabu >= 30 and posicao_tabu >= inimigo):
     posicao_tabu = 30
     if (inimigo >=30):
       inimigo = 29
     os.system('cls' if os.name == 'nt' else 'clear')
     print(tabuleiro(x,y,30,inimigo,hero))
     print("Sua posição: ",posicao_tabu)
     print("Posição do inimigo", inimigo)
     print("Você venceu!")
     try:
      jogador = int(input("Deseja jogar novamente?\n1 - Sim.\t2 - Não.\nJogador: "))
      if (jogador == 1):
       os.system('cls' if os.name == 'nt' else 'clear')
       for i in range (5):
        casas_envenenadas[i] = dados(0,2,30)
       posicao_tabu = 1
       inimigo = 2
       hero = "O"
       veneno = False
       antidoto = 1
       tabuleiro(x,y,posicao_tabu,inimigo,hero)
       print(tabuleiro(x,y,posicao_tabu,inimigo,hero))
       print("\nUse: 1 - Jogar dado.\t2 - Usar antidoto (1).\t3 - Sair.")
      else:
       print("FIM DE JOGO")
       break
     except:
       print("FIM DE JOGO")
    elif (inimigo >= 30 and inimigo > posicao_tabu):
     inimigo = 30
     os.system('cls' if os.name == 'nt' else 'clear')
     print(tabuleiro(x,y,posicao_tabu,30,hero))
     print("Sua posição: ",posicao_tabu)
     print("Posição do inimigo", inimigo)
     print("você perdeu!")
     try:
      jogador = int(input("Deseja jogar novamente?\n1 - Sim.\t2 - Não.\nJogador: "))
      if (jogador == 1):
       os.system('cls' if os.name == 'nt' else 'clear')
       for i in range (5):
        casas_envenenadas[i] = dados(0,2,30)
       posicao_tabu = 1
       inimigo = 2
       hero = "O"
       veneno = False
       antidoto = 1
       tabuleiro(x,y,posicao_tabu,inimigo,hero)
       print(tabuleiro(x,y,posicao_tabu,inimigo,hero))
       print("\nUse: 1 - Jogar dado.\t2 - Usar antidoto (1).\t3 - Sair.")
      else:
       print("FIM DE JOGO")
       break
     except:
       print("FIM DE JOGO")
    else:
     os.system('cls' if os.name == 'nt' else 'clear')
     print(tabuleiro(x,y,posicao_tabu,inimigo,hero))
     print("\nUse: 1 - Jogar dado.\t2 - Usar antidoto (1).\t3 - Sair.")
     print("Sua posição: ",posicao_tabu)
     print("Posição do inimigo", inimigo)
     if (veneno == True):
      print("\nVocê está envenenado!")
      print("Você tem ",antidoto," antidoto")
   elif (jogador == 2):
    if (antidoto == 1 and veneno == True):
     antidoto = 0
     veneno = False
     hero = "O"
     os.system('cls' if os.name == 'nt' else 'clear')
     print(tabuleiro(x,0,posicao_tabu,inimigo,hero))
     print("\n Você está curado!")
     print("\nUse: 1 - Jogar dado.\t2 - Usar antidoto (0).\t3 - Sair.")
    elif (antidoto == 1 and veneno == False):
      os.system('cls' if os.name == 'nt' else 'clear')
      print(tabuleiro(x,0,posicao_tabu,inimigo,hero))
      print("Deixa de ser doido que tu tá saudável rapá.")
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print(tabuleiro(x,0,posicao_tabu,inimigo,hero))
      print("\nVocê não possui mais antidotos! Se vira, mermão.")
   elif (jogador == 3):
    print("JOGO ENCERRADO")
    break
   else:
     os.system('cls' if os.name == 'nt' else 'clear')
     print(tabuleiro(x,y,posicao_tabu,inimigo,hero))
     print("\nValor inválido!")
  except:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(tabuleiro(x,y,posicao_tabu,inimigo,hero))
    print("\nValor inválido!")