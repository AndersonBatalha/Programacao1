#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 13 - Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random
palavras = ["armario", "bacia", "caderno", "dicionario", "estudante", "feriado", "gato", "helicoptero", "inteligente", "jaboticaba", "lampada", "moeda", "namorado", "olho", "pastel", "queijo", "rato", "salsa", "tentativa", "urso", "vagem", "zebra"]

def embaralhaPalavra(palavra):
	lista = list(palavra)
	random.shuffle(lista)
	embaralhado = "".join(lista)
	print "Palavra embaralhada:", embaralhado
	return embaralhado

def jogar():
	tentativas = 0
	print "\nJOGO DA PALAVRA EMBARALHADA\n"
	n = random.randint(0, len(palavras)-1)
	resposta = palavras[n]
	embaralhaPalavra(resposta)
	while tentativas <= 5:
		tentativas += 1
		tentativa = raw_input("Digite sua %da tentativa: "%(tentativas))
		if tentativa == resposta:
			if tentativas == 1:
				print "Você acertou após %d tentativa" %(tentativas)
			else:
				print "Você acertou após %d tentativas" %(tentativas)
			break
	else:
		print "Fim de jogo! A resposta correta é %s" %(resposta)

opcao = raw_input("Deseja iniciar o jogo? (S/N)   ")
if opcao == "S" or opcao == "s":
	jogar()
