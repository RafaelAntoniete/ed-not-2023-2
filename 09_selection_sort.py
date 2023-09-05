def selection_sort(lista):
    """
        ALGORITMO DE ORDENAÇÃO SELECTION SORT

        Isola (seleciona) o primeiro elemento da lista e, em seguida, 
        encontra o menor valor no restante da lista. Se o valor
        encontrado for menor que o valor previamente selecionado,
        efetua a troca entre eles. Continuando, seleciona o segundo
        elemento da lista, buscando pelo menor valor das posições
        subsequentes. Faz a troca entre os dois valores, se necessário.
        O processo se repete até que o penultimo elementoda lista seja
        isolado, comparado com o ultimo e feita a troca entre eles, se
        for o caso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # loop que vai da primeira até a PENULTIMA posição
    for pos_sel in range(len(lista) - 1):
        passd += 1

        #Inicia supondo que a posição do menor valordo resto da lista
        # é aquela imediatamente subsequente à posição selecionada
        pos_menor = pos_sel + 1

        # Percorre novamente a lista, da poição seguinte à pos_menor
        # até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor encontrado na posição pos for MENOR do que o
            # valor da posição pos_menor, então atualiza pos_menor para
            # a posição de pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # Neste ponto, ja´terminamos de poercorrer o restante da lista e
        # já sabemos a posição do menor elemento que há nele. Comparamos,
        # então, os valores das posições pos_menor e pos_sel e, se o
        # primeiro for MENOR que o segundo, fazemos a troca entre eles.
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

############################################################################################
# Caso Intermediário
# nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

# Melhor caso
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pior caso
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print("ANTES: ", nums)
selection_sort(nums)
print("DEPOIS: ", nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

import sys
sys.dont_write_bytecode = True #Impede a criação do cache

#Importando a lista de nomes
from data.nomes_desord import nomes
from time import time

# nomes10000 = nomes[:10000]

hora_ini = time()
selection_sort(nomes)
hora_fim = time()
print(nomes)    # Lista após ordenação
print(f"Tempo gasto {(hora_fim - hora_ini) * 1000}ms\n")