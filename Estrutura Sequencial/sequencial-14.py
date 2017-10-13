#!/usr/bin/env python
# coding: utf-8
# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
print ("Joao Papo-de-Pescador.")
peso_peixes = float(raw_input("Peso pescado: "))
multa = (peso_peixes - 50) * 4
excesso = peso_peixes - 50
if peso_peixes > 50:
	print "O excesso foi de", excesso, "kg. Deve pagar R$", multa, "de multa."
else:
	print "Nada a pagar."
