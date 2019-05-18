from math import sqrt

def menu():
    while True:
        try:
            entrada = int(input("Digite uma das opções:\n1 - Leitura da matriz adjacência\n2 - Leitura da matriz dos pesos\n\n0 - Sair\n\nEntrada: "))
        except:
            print("\nEntrada inválida\n")
            continue
        if entrada > 2 or entrada < 0:
            print("\nEntrada inválida\n")
            continue
        break

    if entrada == 0:
        quit()
    elif entrada == 1:
        adjacencia()
    elif entrada == 2:
        peso()

def leituraAdjacencia():
    try: # caso ocorra um erro (só possível caso a matriz esteja vaiza ou não esteja inserida corretamente) executa o except
        with open("A.txt", "r") as file:
            # lê todos os elementos do arquivo, substitui as quebras de linha por espaço e separa os itens por espaço
            # '[-1]' ignora o último caracter do arquivo, pois seria uma quebra de linha que foi substituida
            grafo = file.read().replace("\n", " ")[:-1].split(" ")
            # quantidade de linhas (que é igual ao de colunas) vai ser a raiz quadrada da quantidade de elementos
            tamanho = int(sqrt(len(grafo)))
            # converte todos os itens pra inteiro (padrão é string)
            # separa os itens em listas do tamanho da quantidade de colunas e adiciona cada uma em 'grafo', formando uma matriz
            grafo = [[int(grafo[i]) for i in range(0, len(grafo))][0+(i*tamanho):tamanho+(i*tamanho)] for i in range(0, tamanho)]
        return grafo
    except:
        print("O arquivo da matriz, 'A.txt', está vazio ou não possui informações válidas. Por favor insira os dados e inicie o programa novamente")
        quit()

def verificaSimples(matrizAdjacencia):
    ehSimples = True
    motivos = [] # lista que vai salvar motivos de não ser simples, caso seja o caso

    for linha in range(0, len(matrizAdjacencia)):
        # como a matriz é espelhada diagonalmente só há a necessidade de verificar uma metade, incluindo a diagonal principal
        # para isso, basta somar o número da linha na posição inicial da coluna
        for coluna in range((0+linha), len(matrizAdjacencia[linha])):
            # verifica laços, verificando se trata-se do mesmo vértica na linha e coluna
            if((linha == coluna) and (matrizAdjacencia[linha][coluna] > 0)):
                ehSimples = False
                motivos.append("Há %d laço(s) no vértice v%d" %(matrizAdjacencia[linha][coluna], (linha+1)))
            # verifica se há mais de uma aresta entre dois vértices
            elif(matrizAdjacencia[linha][coluna] > 1):
                ehSimples = False
                motivos.append("Há arestas múltiplas entre v%d e v%d" %(linha+1, coluna+1))

    if ehSimples:
        print("\nO grafo é simples, pois não possui arestas múltiplas ou laços")
    else:
        print("\nO grafo não é simples\n\nMotivos: ")
        for i in motivos: # percorre a lista de motivos e printa eles
            print(i)

    print("")

    # retorna o resultado pra ser usado na função de verificar se é completo
    return ehSimples

def verificaGraus(matrizAdj):
    lista_laços = []
    lista_ncrescente = [0 for lines in matrizAdj] # linhas populadas com zeros
    for contador, linhas in enumerate(matrizAdj): # contadas linhas e colunas
        for indices, itens in enumerate(linhas):
            if contador == indices and itens != 0: # Salvo numa lista de laços as posições onde ocorrem laços (vértice possui ligação com si mesmo)
                lista_laços.append((contador, itens))

    if len(lista_laços) == 0: # Se a lista de laços for vazia, simplesmente é realizada a soma e logo depois, o rearranjo para obter os graus
        lista_ncrescente = sorted([sum(linhas) for linhas in matrizAdj], reverse=True)
    else:
        for laços in lista_laços:
            lista_ncrescente[laços[0]] = laços[1] # quantidade de laços é somada ao numero de graus
        for linhas in enumerate(matrizAdj):
            lista_ncrescente[linhas[0]] += sum(linhas[1])
        lista_ncrescente = sorted(lista_ncrescente, reverse=True)
    if (sum(lista_ncrescente) % 2) != 0: # Se par, uma lista de graus válida será retornada
        return False
    else:                               # Se impar, a função retorna falso
        print("A sequência de graus do grafo é: ", lista_ncrescente, "\n")

    return lista_ncrescente

def verificaArestas(matrizAdjacencia):
    quantidadeArestas = 0
    for linha in range(0, len(matrizAdjacencia)):
        for coluna in range((0+linha), len(matrizAdjacencia[linha])):
            quantidadeArestas += matrizAdjacencia[linha][coluna]

    print("O grafo possui %d arestas\n" %(quantidadeArestas))

def verificaCompleto(matrizAdjacencia):
    contador = 0
    for i, linhas in enumerate(matrizAdjacencia):
        if linhas[i] == 0 and (0 not in linhas[:i] and 0 not in linhas[i+1:]): # Uma vez que o grafo já se caracteriza como simples, todos os elementos da diagonal principal são somados, se o resultado for 0, o grafo é completo
            contador += linhas[i]
        else:
            contador += 1
    return contador == 0

def verificaEuler(listagraus):
    for elemento in listagraus:
        if (elemento % 2) == 0:
            continue
        else:
            print("\nO grafo não é Euleriano")
            return 0
    print("\nO grafo é Euleriano")

def adjacencia():
    matrizAdjacencia = leituraAdjacencia()
    ehSimples = verificaSimples(matrizAdjacencia)
    listagraus = verificaGraus(matrizAdjacencia)
    verificaArestas(matrizAdjacencia)
    # a função de verificaSimples é chamada dentro de verificaCompleto, já que seu return será utilizado
    if ehSimples:
        if(verificaCompleto(matrizAdjacencia)):
            print("O grafo é completo")
        else:
            print("O grafo é simples e não completo")
    else:
        print("O grafo não é completo")

    verificaEuler(listagraus)
    print("\n")

def leituraPeso():
    try: # caso ocorra um erro (só possível caso a matriz esteja vaiza ou não esteja inserida corretamente) executa o except
        with open("P.txt", "r") as file:
            # lê todos os elementos do arquivo, substitui as quebras de linha por espaço e separa os itens por espaço
            # '[-1]' ignora o último caracter do arquivo, pois seria uma quebra de linha que foi substituida
            grafo = file.read().replace("\n", " ")[:-1].split(" ")
            # quantidade de linhas (que é igual ao de colunas) vai ser a raiz quadrada da quantidade de elementos
            tamanho = int(sqrt(len(grafo)))
            # converte todos os itens pra inteiro (padrão é string)
            # separa os itens em listas do tamanho da quantidade de colunas e adiciona cada uma em 'grafo', formando uma matriz
            grafo = [[int(grafo[i]) for i in range(0, len(grafo))][0+(i*tamanho):tamanho+(i*tamanho)] for i in range(0, tamanho)]
        return grafo
    except:
        print("O arquivo da matriz, 'P.txt', está vazio ou não possui informações válidas. Por favor insira os dados e inicie o programa novamente")
        quit()

def peso():
    matrizPeso = leituraPeso()

menu()
