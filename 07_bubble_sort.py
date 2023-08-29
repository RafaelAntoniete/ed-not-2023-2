def bubble_sort(lista):
    """
        ALGORITMO DE ORDENAÇÃO BUBBLE SORT
        Percorre a lista a ser ordenada em sucessivas e passadas,
        trocando entre si dois elementos adjacentes sempre que 
        o seundo for MENOR que o primeiro. Efetua tantas
        passadas quanto necessárias, até que, na última delas, 
        nenhuma troca tenha sido realizada.
    """
    # Loop eterno, não sabemos de antemão quantas passadas
    # serão necessárias
    while True:
        # Controla se houve trocas na passada
        trocou = False

        # Percurso dalista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        for pos in range(len(lista) - 1):

            # Se o número que está à frente da lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos), 
            # faz a TROCA
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True  # Houve troca na passada

        if not trocou:      # Não houve troca na passada
            break           # Interrompe o loop eterno