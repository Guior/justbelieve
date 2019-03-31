def leitura():
    file = open("matrizAdjacencia.txt", "r")
    matrizAdjacencia = []
    temp = []
    for i in file.readlines():
        for j in range(0, 4):
            temp.append(int(i[:-1].split(" ")[j]))
        matrizAdjacencia.append(temp)
        temp = []
    return matrizAdjacencia

def main():
    matrizAdjacencia = leitura()

main()
