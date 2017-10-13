#!/usr/bin/env python
# coding: utf-8
# 17. Fa�a um Programa para uma loja de tintas. O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada. Considere que a cobertura da tinta � de 1 litro para cada 6 metros quadrados e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00 ou em gal�es de 3,6 litros, que custam R$ 25,00.
# Informe ao usu�rio as quantidades de tinta a serem compradas e os respectivos pre�os em 3 situa��es:
# comprar apenas latas de 18 litros;
# comprar apenas gal�es de 3,6 litros;
# misturar latas e gal�es, de forma que o pre�o seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto �, considere latas cheias.
print ("Programa para uma loja de tintas - versao 2.")
recipiente = str (raw_input ("Latas, galoes ou ambos [l/g/a]: "))
area = float (raw_input ("Area (m2): "))
quantidade_latas = area / 54
preco_total_latas = quantidade_latas * 80
quantidade_galoes = area / 3.6
preco_total_galoes = quantidade_latas * 25
quantidade = (area / 3.6) + (area / 54)
preco_total = (quantidade * 80) + (quantidade * 25) - 10/100
if recipiente == "l":
	print ("Latas de tinta: %.0f") % quantidade_latas
	print ("Preco total: R$ %.0f") % preco_total_latas
elif recipiente == "g":
	print ("Latas de tinta: %.0f") % quantidade_galoes
	print ("Preco total: R$ %.0f") % preco_total_galoes
elif recipiente == "a":
	print ("Latas de tinta: %.0f") % quantidade
	print ("Preco total: R$ %.0f") % preco_total
