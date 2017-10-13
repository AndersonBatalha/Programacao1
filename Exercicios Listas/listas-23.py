#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 23. A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado    % do uso
# 1    alexandre          434,99 MB        16,85%
# 2    anderson          1187,99 MB        46,02%
# 3    antonio            117,73 MB         4,56%
# 4    carlos              87,03 MB         3,37%
# 5    cesar                0,94 MB         0,04%
# 6    rosemary           752,88 MB        29,16%
# Espaço total ocupado: 2581,57 MB Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
a = open("usuarios.txt")
arq = open("relatorio.txt", "w")
nomes = []
espacos = []
consumo = []
l = []
p = []
s = []
lista = []
for linha in a:
	(nome, espaco) = linha.split("\n")
	nome = linha[0:9]
	espaco = linha[16:]
	nomes.append(nome)
	espacos.append(espaco)
arq.write("ACME Inc.			Uso do espaço em disco pelos usuários\n-------------------------------------------------------------\nNr.  Usuário        Espaço utilizado    % do uso\n")
print "ACME Inc.               Uso do espaço em disco pelos usuários\n-------------------------------------------------------------\nNr.  Usuário        Espaço utilizado    % do uso"
for i in range(len(nomes)):
	mb = int(espacos[i]) / 1024 / 1024.0
	l.append("%.2f" % mb)
	lista.append(mb)
	consumo.append(float(l[i]))
	perc = (lista[i] / sum(lista)) * 100
	media = sum(lista) / len(lista)
	s.append("%.2f" % perc)
	p.append(float(s[i]))
	a = str(i).rjust(2)
	b = str(consumo[i])
	c = str(p[i])
	print "%s %s %s MB %s %%" % (int(a) + 1, nomes[i].rjust(12), b.rjust(12), c.rjust(14))
	arq.write("%s %s %s MB %s %%\n" % (int(a) + 1, nomes[i].rjust(12), b.rjust(12), c.rjust(14)))
arq.write("\nEspaço total ocupado: %.2f MB\tEspaço médio ocupado: %.2f MB\n\nUsuário com maior consumo: %s\nUsuário com menor consumo: %s" % (sum(lista), media, nomes[lista.index(max(lista))], nomes[lista.index(min(lista))]))
print "\nEspaço total ocupado: %.2f MB\tEspaço médio ocupado: %.2f MB\n\nUsuário com maior consumo: %s\nUsuário com menor consumo: %s" % (sum(lista), media, nomes[lista.index(max(lista))], nomes[lista.index(min(lista))])
arq.close()
