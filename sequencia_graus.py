def contadorGraus(matrizAdj):
    lista_laços = []
    for contador, linhas in enumerate(matrizAdj):
        for indices, itens in enumerate(linhas):
            if contador == indices and itens != 0:
                lista_laços.append((contador, indices))
    if len(lista_laços) == 0:
        print("O grafo não contém laços\n")
        lista_ncrescente = sorted([sum(linhas) for linhas in matrizAdj])
    else:
        for laços in lista_laços: 
            print("O grafo contém laços nas posição %d %d da matriz de adjacência", laços[0], laços[1])
        lista_ncrescente = sorted([sum(linhas[1]) + 1 if linhas[0] == lista_laços[0][0] else sum(linhas[1]) for linhas in enumerate(matrizAdj)], reverse=True)
    
    if (sum(lista_ncrescente) % 2) != 0:
        return False
    else:
        return lista_ncrescente

    
