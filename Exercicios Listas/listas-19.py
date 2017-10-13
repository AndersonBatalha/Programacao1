#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
opcao = 0
votos = []
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
print "\nResponda a enquete: Qual o melhor Sistema Operacional para uso em servidores?\nOpções:\n"
for i in range(len(opcoes)):
	print "%d - %s" % (i + 1, opcoes[i])
	votos.append(0)
while True:
	opcao = int(raw_input("Opção: "))
	if opcao < 0 or opcao > len(opcoes): print "Voto não computado."
	else:
		if opcao == 0:
			print votos
			break
		else:
			votos[opcao - 1] += 1
			print votos
print "\nSistema Operacional		Votos		Percentual(%)\n-------------------		-----	       ---"
percentual = []
for i in range(len(opcoes)):
	soma = sum(votos) + 0.0
	print "%19s %15d %14.1f %%" % (opcoes[i], votos[i], ((votos[i] / soma) * 100))
	perc = (votos[i] / soma) * 100
	percentual.append(perc)
print "-------------------             -----\nTotal  				%d\n\nResultado:\nO Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.1f %% dos votos." % (sum(votos), opcoes[votos.index(max(votos))], votos[votos.index(max(votos))], percentual[percentual.index(max(percentual))])
