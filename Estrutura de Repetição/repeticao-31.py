#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# a. Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
qtde_itens = int(raw_input("Quantidade de itens: "))
precos = []
for i in range(1, qtde_itens + 1):
	preco = float(raw_input("Preço do produto %d: R$ " % i))
	precos.append(preco)
print "Total: R$ %.2f" % sum(precos)
dinheiro = float(raw_input("Dinheiro: R$ "))
while dinheiro < sum(precos):
	print "Não é o suficiente."
	dinheiro = float(raw_input("Dinheiro: R$ "))
else:
	troco = dinheiro - sum(precos)
	print "\nLojas Tabajara"
	for i in range(qtde_itens):
		print "Produto %d: R$ %.2f" % (i + 1, precos[i])
	print "Dinheiro: R$ %.2f\nTroco: R$ %.2f" % (dinheiro, troco)
