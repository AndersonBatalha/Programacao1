#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
total = 0
qtde_cds = int(raw_input("Quantidade de CDs: "))
for i in range(1, qtde_cds + 1):
	valor_unidade = float(raw_input("Valor do CD %d: " % i))
	total += valor_unidade
else:
	print "Valor médio gasto: %.2f" % (total / qtde_cds)
