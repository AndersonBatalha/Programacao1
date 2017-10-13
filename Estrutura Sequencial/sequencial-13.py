#!/usr/bin/env python
# coding: utf-8
# 13. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 (h = altura)
# Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
print ("Peso ideal de uma pessoa - Para homens ou mulheres.")
sexo = str (raw_input ("Sexo [m/f]: "))
altura = float (raw_input ("Altura: "))
peso = float (raw_input ("Peso: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
diferenca_homem = peso - peso_ideal_homem
diferenca_mulher = peso - peso_ideal_mulher
diferenca_homem2 = peso_ideal_homem - peso
diferenca_mulher2 = peso_ideal_mulher - peso
if sexo == "m":
	peso_ideal_homem = (72.7 * altura) - 58
	if peso > peso_ideal_homem:
		print ("Acima do peso.")
		print ("O peso ideal e: %.2f") % peso_ideal_homem
		print ("Deve perder: %.2f") % diferenca_homem
	elif peso < peso_ideal_homem:
		print ("Subnutrido.")
		print ("O peso ideal e: %.2f") % peso_ideal_homem
		print ("Deve ganhar: %.2f") % diferenca_homem2
	elif peso == peso_ideal_homem:
		print ("Em forma!!")
elif sexo == "f":   
	peso_ideal_mulher = (62.1 * altura) - 44.7
	if peso > peso_ideal_mulher:
		print ("Acima do peso.")
		print ("O peso ideal e: %.2f") % peso_ideal_mulher
		print ("Deve perder: %.2f")% diferenca_mulher
	elif peso < peso_ideal_mulher:
		print ("Subnutrida.")
		print ("O peso ideal e: %.2f") % peso_ideal_mulher
		print ("Deve ganhar: %.2f") % diferenca_mulher2
	elif peso == peso_ideal_mulher:
		print ("Em forma!!")
else:
	print "Sexo inválido. Tente novamente."
