#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 43. O cardápio de uma lanchonete é o seguinte:
# Especificação		Código		Preço
# Cachorro Quente	100			R$ 1,20
# Bauru Simples		101			R$ 1,30
# Bauru com ovo		102			R$ 1,50
# Hambúrguer		103			R$ 1,20
# Cheeseburguer		104			R$ 1,30
# Refrigerante		105			R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
while True:
	cardapio = {100:["Cachorro Quente", 1.2], 101:["Bauru Simples", 1.3], 102:["Bauru com ovo", 1.5], 103:["Hamburguer", 1.2], 104:["Cheeseburger", 1.3], 105:["Refrigerante", 1]}
	pedido = {}
	codigos = []
	pedidos = []
	precos = []
	l = []
	t = []
	total_unidade = 0
	print "\n\t\t\tCardápio\n\nEspecificação\t\tCódigo\t\tPreço\n"
	for i in range(len(cardapio.keys())):
		print "%s\t\t%d\t\tR$ %.2f" % (cardapio.values()[i][0], cardapio.keys()[i], cardapio.values()[i][1])
	n = int(raw_input("\nNúmero de pedidos: "))
	for i in range(1, n + 1):
		codigo = int(raw_input("Código do produto %d: " % i))
		quantidade = int(raw_input("Quantidade de itens do pedido %d: " % i))
		codigos.append(codigo)
		pedidos.append(cardapio[codigo][0])
		precos.append(cardapio[codigo][1])
		l.append(quantidade)
	print "\n#  Código	Pedido		     Preço  	Unidades    Total unitário"
	for i in range(len(precos)):
		total_unidade = precos[i] * l[i]
		t.append(total_unidade)
		print "%d   %d  	%s	     R$ %.1f	   %s	     R$ %.2f" % (i + 1, codigos[i],pedidos[i], precos[i], l[i], total_unidade)
	print "\nNúmero de pedidos: %d\nQuantidade de itens: %d\n\nTotal geral do pedido: R$ %.2f" % (n, len(pedidos), sum(t))
