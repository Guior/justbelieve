from sequencia_graus import * # importada função para contagem e checagem de graus

def leitura():
    file = open("matrizAdjacencia.txt", "r")
    grafo = file.readlines()
    matrizAdjacencia = []
    temp = []
    for i in grafo:
        for j in range(0, len(grafo)):
            temp.append(int(i[:-1].split(" ")[j]))
        matrizAdjacencia.append(temp)
        temp = []
    print(matrizAdjacencia)
    return matrizAdjacencia

def main():
    matrizAdjacencia = leitura()
    print(matrizAdjacencia)
    contadorGraus(matrizAdjacencia)

main()
