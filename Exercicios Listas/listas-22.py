#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 22. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles. Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza
# necessita troca do cabo ou conector
# quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100
# Situação                                 Quantidade      Percentual
# 1 - necessita da esfera                      40             40%
# 2 - necessita de limpeza                     30             30%
# 3 - necessita troca do cabo ou conector      15             15%
# 4 - quebrado ou inutilizado                  15             15%
mouse = 0
defeitos = ["Necessita da esfera", "Necessita de limpeza", "Necessita troca do cabo ou conector", "Quebrado ou inutilizado"]
ndefeitos = []
print "Tipo do defeito igual a zero encerra o programa\n\nEscolha um dos tipos de defeito abaixo"
for i in range(len(defeitos)):
	print "%d - %s" % (i + 1, defeitos[i])
	ndefeitos.append(0)
while True:
	tipo = int(raw_input("Tipo de defeito do mouse: "))
	if tipo == 0:
		break
	else:
		if tipo < 1 or tipo > len(defeitos):
			print "Voto não computado."
		else:
			ndefeitos[tipo - 1] += 1
			mouse += 1
		print ndefeitos
nmouses = mouse + 0.0
print "\nRelatório:\n\nQuantidade de mouses: %d\nSituação				Quantidade	%%" % (mouse)
for i in range(len(defeitos)):
	perc = (ndefeitos[i] / nmouses) * 100
	print "%s%s         %.1f" % (defeitos[i].ljust(35), str(ndefeitos[i]).rjust(11), perc)
print "\n%s foi o problema mais frequente nos mouses.\n\n%s foi o problema menos frequente nos mouses." % (defeitos[ndefeitos.index(max(ndefeitos))], defeitos[ndefeitos.index(min(ndefeitos))])
