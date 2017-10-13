#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem;
numero = 0
numeros = []
soma = 0
n = 0
acima_media = []
abaixo7 = []
while True:
	if numero != -1:
		numero = int(raw_input("(-1 = fim): "))
		numeros.append(numero)
	else:
		numeros.remove(-1)
		media = sum(numeros) / len(numeros)
		print "Quantidade de valores que foram lidos:", len(numeros)
		print "Todos os valores na ordem em que foram informados:",
		for i in range(len(numeros)):
			print numeros[i],
		print "\nTodos os valores na ordem inversa:",
		for i in range(len(numeros)):
			numeros.reverse()
			print numeros[i],
		print "\nSoma dos valores: %d\nMédia dos valores: %.2f" % (sum(numeros), media)
		for numero in numeros:
			if numero > media:
				acima_media.append(numero)
			if numero < 7:
				abaixo7.append(numero)
		if len(acima_media) == 0:
			print "Sem números acima da média."
		else:
			print "\nNúmeros acima da média:",
			for i in range(len(acima_media)):
				print acima_media[i],
		if len(abaixo7) == 0:
			print "Sem números abaixo de 7."
		else:
			print "\nNúmeros abaixo de 7:",
			for i in range(len(abaixo7)):
				print abaixo7[i],
		break
