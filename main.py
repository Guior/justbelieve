def leitura():
    file = open("matrizAdjacencia.txt", "r")
    matrizAdjacencia = []
    for i in file.readlines():
        matrizAdjacencia.append(i[:-1].split(" "))
    return matrizAdjacencia

def main():
    matrizAdjacencia = leitura()
    print(matrizAdjacencia)

main()
