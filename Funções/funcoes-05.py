#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto: quantia de imposto sobre vendas expressa em porcentagem
# custo: custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.
taxa_imposto = custo = total = imposto = 0
def soma_imposto(taxa_imposto, custo, imposto, total):
	custo = float(raw_input("\nCusto do produto: "))
	imposto = int(raw_input("Porcentagem sobre o custo: "))
	taxa_imposto = custo * (imposto / 100.0)
	total = custo - taxa_imposto
	return "Custo do produto com os impostos: R$ %.2f" % total
while True:
	print soma_imposto(taxa_imposto, custo, imposto, total)
