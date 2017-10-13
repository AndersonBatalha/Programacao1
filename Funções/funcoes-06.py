#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
am = am1 = am2 = pm = horas = minutos = 0
def converte_horario(am, am1, am2, pm, minutos):
	pm = int(raw_input("\nInforme a hora na notação de 24 horas: "))
	minutos = int(raw_input("Informe os minutos: "))
	am1 = pm + 12
	am2 = pm - 12
	if am < 0:
		return "\nNa notação de 24 horas: %d:%d.\nNa notação de 12 horas: %d:%d" % (pm, minutos, am1, minutos)
	else:
		return "\nNa notação de 24 horas: %d:%d.\nNa notação de 12 horas: %d:%d" % (pm, minutos, am2, minutos)
while True:
	print converte_horario(am, am1, am2, pm, minutos)
