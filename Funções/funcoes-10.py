#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10 - Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "Natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "Craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
while True:
	iniciar = raw_input("\n\t\tJOGO DE CRAPS\nJogar? (S/N): ")
	if iniciar == "S" or iniciar == "s":
		import random
		numeros = []
		for i in range(2):
			numero = random.randint(2, 12)
			numeros.append(numero)
		print "Números:", numeros
		if numeros[0] == 7 or numeros[0] == 11: print "'Natural'. Ganhou!!"
		elif numeros[0] == 2 or numeros[0] == 3 or numeros[0] == 12: print "'Craps'. Perdeu!!"
		else:
			print "O número %d é seu 'Ponto'." % (numeros[0])
			for i in range(2):
				numero = random.randint(2, 12)
				numeros.pop()
				numeros.append(numero)
			print "Números:", numeros
			if numeros[0] >= 4 or numeros[0] <= 9 and numeros[0] != 7:
				for i in range(2):
					numero = random.randint(2, 12)
					numeros.pop()
					numeros.append(numero)
				print "Números:", numeros
			else:
				if numeros[0] == 7: print "Você perdeu!!"
	elif iniciar == "N" or iniciar == "n": print "Fim !!"
	else: print "Apenas S ou N!!"
