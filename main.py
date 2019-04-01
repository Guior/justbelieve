from sequencia_graus import * # importada função para contagem e checagem de graus

def leitura():
    # abre o arquivo 'matrizAdjacencia.txt' e salva na variável file
    with open("matrizAdjacencia.txt", "r") as file:
        # file.readlines() lê percorre todas as linhas do arquivo, e cada linha é salva, durante a iteração, na variável linhas
        # [:-1] ignora o '\n' (quebra de linha) da linha em questão.
        # '.split()' separa a linha por espaço e salva os itens em uma lista, cada lista é salva em 'grafo', formando uma matriz
        grafo = [linhas[:-1].split(" ") for linhas in file.readlines()]
        # percorre todos os elementos de cada coluna da matriz grafo, através da checagem do seu tamanho (len(grafo)) e converte seus elementos pra inteiro
        # eles elementos vão ser salvos em uma lista única e temporária (indicado através do primeiro '[]')
        # '[0+(i*len(grafo)):len(grafo)+(i*len(grafo))] for i in range(0, len(grafo))' vai gerar listas a partir de intervalos referentes ao tamanho das linhas e colunas
        grafo = [[int(grafo[i][j]) for i in range(0, len(grafo)) for j in range(0, len(grafo))][0+(i*len(grafo)):len(grafo)+(i*len(grafo))] for i in range(0, len(grafo))]
    return grafo

def verificaSimples(matrizAdjacencia):
    ehSimples = True
    motivos = []

    for linha in range(0, len(matrizAdjacencia)):
        for coluna in range((0+linha), len(matrizAdjacencia[linha])):
            if((linha == coluna) and (matrizAdjacencia[linha][coluna] > 0)):
                ehSimples = False
                motivos.append("Há %d laço(s) no vértice v%d" %(matrizAdjacencia[linha][coluna], (linha+1)))
            elif(matrizAdjacencia[linha][coluna] > 1):
                ehSimples = False
                motivos.append("Há arestas múltiplas entre v%d e v%d" %(linha+1, coluna+1))

    if ehSimples:
        print("O grafo é simples, pois não possui arestas múltiplas ou laços\n")
    else:
        print("O grafo não é simples\n\nMotivos: ")
        for i in motivos:
            print(i)
        print("\n")

    return ehSimples

def verificaGraus(matrizAdjacencia):
    pass

def verificaArestas(matrizAdjacencia):
    quantidadeArestas = 0
    for linha in range(0, len(matrizAdjacencia)):
        for coluna in range((0+linha), len(matrizAdjacencia[linha])):
            quantidadeArestas += matrizAdjacencia[linha][coluna]

    print("O grafo possui %d arestas\n\n" %(quantidadeArestas))

def verificaCompleto(matrizAdjacencia, ehSimples):
    pass

def main():
    matrizAdjacencia = leitura()
<<<<<<< HEAD
    verificaSimples(matrizAdjacencia)
    verificaGraus(matrizAdjacencia)
    verificaCompleto(matrizAdjacencia, verificaArestas(matrizAdjacencia))
=======
    print(matrizAdjacencia)
    contadorGraus(matrizAdjacencia)
>>>>>>> 9783256e0e383cec621261e49a71d4d629571cf4

main()
