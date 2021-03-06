#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escreva um programa que calcule a autonomia de automóvel, de acordo com algumas condições (considerando a velocidade média de 80 km/h):
# Rendimento da gasolina (100%): 22 km/l / Rendimento do etanol (100%): 15 km/l
# – Rendimento gasolina/etanol
# • 10% etanol: 21 km/l • 20% etanol: 20 km/l • 30% etanol: 19 km/l
# • 40% etanol: 18 km/l • 50% etanol: 17 km/l • 50% a 90% etanol: 16 km/l
# O usuário deve fornecer a distância a ser percorrida e sua velocidade média; e a quantidade (em litros) de etanol e de gasolina.
# O rendimento tem as seguintes reduções nas faixas de velocidade:
# – Maior que 0 km/h e menor que 80 km/h: redução de 20 % no rendimento
# – Maior que 80 km/h: redução de 30% no rendimento
# O programa deverá apresentar mensagem indicando a autonomia do veículo e, caso o combustível não seja suficiente, qual a quantidade em litros para abastecimento e em quanto tempo isto deverá acontecer.
distancia = float(raw_input("Distância a ser percorrida em km: "))
vmedia = float(raw_input("Velocidade média: "))
etanol = float(raw_input("Quantidade em litros de etanol: "))
gasolina = float(raw_input("Quantidade em litros de gasolina: "))
if etanol == 0:
	print "100 % de gasolina."
	rend_gasolina = 22 * gasolina
	print "Autonomia de", rend_gasolina, "litros de gasolina."
	if vmedia > 0 and vmedia <= 80: reducao = rend_gasolina * 0.2
	else: reducao = rend_gasolina * 0.3
	novo_rend_gasolina = rend_gasolina - reducao
	if distancia > rend_gasolina: print "Serão necessários", distancia - rend_gasolina, "litros de gasolina para completar a viagem."
if gasolina == 0:
	print "100 % de etanol."
	rend_etanol = 15 * etanol
	print "Autonomia de", rend_etanol, "litros de etanol."
	if vmedia > 0 and vmedia <= 80: reducao = rend_etanol * 0.2
	else: reducao = rend_etanol * 0.3
	novo_rend_etanol = rend_etanol - reducao
#if gasolina > 0 and etanol > 0:
#	print "Mistura de etanol e gasolina."
#	perc_etanol = 
#	print "Percentual de etanol:", perc_etanol, "%"
#	if perc_etanol > 0 and perc_etanol <= 10: rend_misto = 21 * etanol
#	elif perc_etanol > 10 and perc_etanol <= 20: rend_misto = 20 * etanol
#	elif perc_etanol > 20 and perc_etanol <= 30: rend_misto = 19 * etanol
#	elif perc_etanol > 30 and perc_etanol <= 40: rend_misto = 18 * etanol
#	elif perc_etanol > 40 and perc_etanol <= 50: rend_misto = 17 * etanol
#	else: rend_misto = 16 * etanol
#	print "O rendimento com etanol e gasolina foi de", rend_misto, "litros."
