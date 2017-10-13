#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sorteio import Dados
nome = cpf = endereco = bairro = cidade = estado = " "
dados_pessoais = []
possiveis_premios = []
sorteio = {}
n = opcao = 0
print Dados(nome, cpf, endereco, bairro, cidade, estado).descricao()
print "\nOpções:\n1 - Sair do programa\t2 - Cadastrar dados dos participantes"
opcao = int(raw_input("Opção: "))
if opcao == 1:
	Dados(nome, cpf, endereco, bairro, cidade, estado).sair()
elif opcao == 2:
	Dados(nome, cpf, endereco, bairro, cidade, estado).cadastro()
	identificacao = Dados(nome, cpf, endereco, bairro, cidade, estado)
	print "Opções:\n1 - Sair\n2 - Visualizar dados dos participantes\n3 - Alteração de dados\n4 - Excluir dados\n5 - Fazer o sorteio\n6 - Gerar arquivo"
	opcao = int(raw_input("Opção: "))
	if opcao == 1:
		Dados(nome, cpf, endereco, bairro, cidade, estado).sair()
	elif opcao == 2:
		print "\nVocê escolheu: 2 - Visualizar dados dos participantes.\nOpções:\n1 - Individualmente\t2 - Todos os participantes"
		opcao = int(raw_input("Opção: "))
		if opcao == 1:
			Dados(nome, cpf, endereco, bairro, cidade, estado).individual()
		elif opcao == 2:
			Dados(nome, cpf, endereco, bairro, cidade, estado).todos_os_participantes()
		else: print "Inválido"
	elif opcao == 3:
		Dados(nome, cpf, endereco, bairro, cidade, estado).altera_dados()
	elif opcao == 4:
		Dados(nome, cpf, endereco, bairro, cidade, estado).exclui_dados()
	elif opcao == 5:
		Dados(nome, cpf, endereco, bairro, cidade, estado).fazer_o_sorteio()
	elif opcao == 6:
		Dados(nome, cpf, endereco, bairro, cidade, estado).gerar_arquivo()
