#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 37. Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
alturas = pesos = codigos = []
codigo = 0
while True:
	codigo = int(raw_input("\nCódigo: "))
	if codigo != 0:
		altura = float(raw_input("Altura (em metros): "))
		peso = float(raw_input("Peso (em kg): "))
		alturas.append(altura)
		pesos.append(peso)
		codigos.append(codigo)
	else:
		print "Resultado final\n\nAltura:\nCódigo: %d\tMaior: %.2f\nCódigo: %d\tMenor: %.2f\n\nPeso:\nCódigo: %d\tMais gordo: %d kg\nCódigo: %d\tMais magro: %d kg\n\nMédia de altura: %.2f\nMédia de peso: %.2f kg" % (codigos[alturas.index(max(alturas))], max(alturas), codigos[alturas.index(min(alturas))], min(alturas), codigos[pesos.index(max(pesos))], max(pesos), codigos[pesos.index(min(pesos))], min(pesos), sum(alturas) / len(alturas), sum(pesos) / len(pesos))
		break
