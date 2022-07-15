#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Genius.py
#  
#  Copyright 2021 Ludmila Dias
#  
# ----------------------------------------------------------------------

#IMPORTAÇÃO DE BIBLIOTECAS
from random import randint
import os
import pickle

#FUNÇÃO PARA LIMPAR A TELA
def limpaTela():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")

#FUNÇÃO QUE SALVO OS DADOS DO RECORDE
def salvarDados(recordeJogo): 
    with open("dados.bin", "wb") as f:
        pickle.dump(recordeJogo,f)

#FUNÇÃO PARA LER OS DADOS SALVOS DE RECORDE
def lerDados(recordeJogo): 
    if os.path.isfile("dados.bin"):
        with open("dados.bin", "rb") as f:
            recordeJogo=pickle.load(f)
    else:
        recordeJogo=[]

    return recordeJogo

#FUNÇÃO QUE VERIFICA SE UM NÚMERO
def verificaNum(correta,resposta):
    cont=0
    p=0

    for num in resposta:
        if num==correta[p]:
            cont+=1
        p+=1
    if cont==(p):
        return True
    else:
        return False

#FUNÇÃO QUE CALCULA A MAIOR PONTUAÇÃO DO JOGADOR
def maiorPontuacao(P,maiorP):
    if P>maiorP:
        maiorP=P
    return(maiorP)

#FUNÇÃO QUE CALCULA O MAIOR RECORDE DO JOGO   
def maiorRecorde(recordeJogador, recorde,nome):
    if recorde==[]:
        recorde=[recordeJogador,nome]
    elif recordeJogador>recorde[0]:
        recorde=[recordeJogador,nome]
    return(recorde)

#FUNÇÃO PRINCIPAL
def main(argv=None):

    #DECLARAÇÃO DE VARIÁVEIS
    x=int(0)
    recordeJogador=0
    recordeJogo=[]
    sair=1
    
    recordeJogo=lerDados(recordeJogo)
    limpaTela()
    principal='''
	 _______       ______        ___   __        ________       __  __        ______       
	/______/\     /_____/\      /__/\ /__/\     /_______/\     /_/\/_/\      /_____/\    
	\::::__\/__   \::::_\/_     \::\_\\  \  \    \__.::._\/     \:\ \:\ \     \::::_\/_     
	 \:\ /____/\   \:\/___/\     \:. `-\  \ \      \::\ \       \:\ \:\ \     \:\/___/\    
	  \:\\_  _\ /    \::___\/_     \:. _    \ \     _\::\ \__     \:\ \:\ \     \_::._\:\   
	   \:\_\ \ \     \:\____/\     \. \`-\  \ \   /__\::\__/\     \:\_\:\ \      /____\:\  
	    \_____\/      \_____\/      \__\/ \__\/   \________\/      \_____\/      \_____\/  
                                                                            BY LUDMILA DIAS

    BEM VINDO!
    APERTE "ENTER" PARA INICIAR.'''
    
    instruções='''
    INSTRUÇÕES:
    - Você receberá um número de 0-9 e deve memoriza-lo e reescreve-lo.
    - A cada rodada será te dado um novo valor, você deve escrever os números anteriores da sequência mais o fornecido.
    - Digite os números um por um, apertando "enter" após inseri-lo.
    - Caso erre um número no meio da sequência o jogo finalizará.
    - CUIDADO! A tela será limpa a cada rodada não permitindo você de verificar os números anteriores, então SE LIGA NA SEQUÊNCIA!

    PRONTO PARA INICIAR? DIGITE "ENTER".'''
    
    #IMPRESSÃO DA TELA PRINCIPAL, INSTRUÇÕES E ENTRADA DO "NOME"
    a=input(principal)
    limpaTela()
    nome=input("INSIRA SEU NOME: ")
    limpaTela()
    a=input(instruções)
    
    #COMANDO DE REPETIÇÃO QUE EXECUTA AS PARTIDAS
    while sair==1:
        correta=[]
        resposta=[]
        sorteado = randint(0,9)
        correta.append(sorteado)

        limpaTela()
        print("START!\n")
        print("O primeiro número sorteado foi:{}" .format(sorteado))

        x=int(input("Digite a sequência completa: "))
        resposta.append(x)

        #COMANDO DE REPETIÇÃO QUE EXECUTA AS RODADAS
        while verificaNum(correta,resposta)==True:
            resposta=[]
            cont=0
            sorteado = randint(0,9)
            correta.append(sorteado)
            limpaTela()
            print("O novo numero eh: {}" .format(sorteado))
            print("Digite a sequência completa: ")
            while verificaNum(correta,resposta)==True and cont<len(correta):
                x=int(input())
                resposta.append(x)
                cont+=1
        
        #MENSAGEM QUANDO O JOGADOR PERDE O JOGO
        P=len(correta)-1
        print("FIM DE JOGO! Você acertou ", P, " números!\n")

        recordeJogador=maiorPontuacao(P,recordeJogador)
        
        sair=int(input("Para sair digite 0\nPara jogar novamente digite 1\n"))
    
    recordeJogo=maiorRecorde(recordeJogador, recordeJogo, nome)

    #IMPRESSÃO DA MAIOR PONTUAÇÃO E RECORDE DO JOGO
    limpaTela()
    print("{} a sua maior pontuação foi: {}".format(nome,recordeJogador))
    print(f'''
        _________________________
        O recorde do jogo eh: {recordeJogo[0]}
        Melhor Jogador: {recordeJogo[1]}
        _________________________''')
    salvarDados(recordeJogo)

if __name__=='__main__':
    main()
