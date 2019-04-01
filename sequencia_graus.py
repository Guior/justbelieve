def contadorGraus(matrizAdj):
    lista_laços = []
    lista_ncrescente = [0 for lines in matrizAdj]
    for contador, linhas in enumerate(matrizAdj): # contadas linhas e colunas
        for indices, itens in enumerate(linhas):  
            if contador == indices and itens != 0: # Salvo numa lista de laços as posições onde ocorrem laços (vértice possui ligação com si mesmo)
                lista_laços.append((contador, itens)) 
    
    if len(lista_laços) == 0: # Se a lista de laços for vazia, simplesmente é realizada a soma e logo depois, o rearranjo para obter os graus
        print("O grafo não contém laços\n")
        lista_ncrescente = sorted([sum(linhas) for linhas in matrizAdj], reverse=True) 
    else:
        for laços in lista_laços: 
            print("O grafo contém laços na(s) posição/posições %d %d da matriz de adjacência" % (laços[0]+1, laços[0]+1)) # É somado 1 ao valor de linha por ser mais conveniente
            lista_ncrescente[laços[0]] = laços[1] # quantidade de laços é somada ao numero de graus
        for linhas in enumerate(matrizAdj):
            lista_ncrescente[linhas[0]] += sum(linhas[1])
        lista_ncrescente = sorted(lista_ncrescente, reverse=True)
    if (sum(lista_ncrescente) % 2) != 0: # Se par, uma lista de graus válida será retornada
        return False
    else:                               # Se impar, a função retorna falso
        return lista_ncrescente

    
