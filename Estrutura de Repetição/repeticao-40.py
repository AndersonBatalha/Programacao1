#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999).
# Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
cidades = []
veiculos = []
acidentes = []
menos_de_2000 = []
for i in range(1, 6):
	cidade = raw_input("\nNome da cidade %d: " % i)
	nveiculos = int(raw_input("Número de veículos de passeio na cidade %d (em 1999): "))
	nacidentes = int(raw_input("Número de acidentes de trânsito com vítimas na cidade %d (em 1999): "))
	cidades.append(cidade)
	veiculos.append(nveiculos)
	acidentes.append(nacidentes)
for nveiculos in veiculos:
	if nveiculos < 2000:
		menos_de_2000.append(nveiculos)
print "\nÍndice de acidentes\nMaior: %d\tCidade: %s\nMenor: %d\tCidade: %s\nMédia de veículos nas cidades: %d\nMédia de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: %.2f" % (max(acidentes), cidades[acidentes.index(max(acidentes))], min(acidentes), cidades[acidentes.index(min(acidentes))], sum(veiculos) / len(veiculos), sum(menos_de_2000) / len(menos_de_2000))
