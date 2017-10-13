#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 7 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
prestacoes = []
p = prestacao = atraso = perc = total = 0
def valorPagamento():
	prestacoes = []
	p = prestacao = atraso = perc = total = 0
	while True:
		p = float(raw_input("Valor da prestação: "))
		if p != 0:
			prestacao += 1
			atraso = int(raw_input("Dias de atraso: "))
			if atraso == 0:
				prestacoes.append(p)
				print prestacoes, "\nSem dias de atraso.\t\tValor da prestação: %.2f\n" % (p)
			else:
				perc = (3 / 100.0 + (1 / 100 * atraso)) * p
				total = p + perc
				prestacoes.append(total)
				print prestacoes, "\nValor da prestação: %.2f\t\t%d dias de atraso.\n" % (total, atraso)
		else:
			print "Prestações:"
			for i in range(len(prestacoes)):
				print "%d - %.2f" % (i, prestacoes)
			break

print valorPagamento()
