def contarNomesLista(lista : list):
    nomesDict = {}
    for i in lista:
        nomesDict[i] = lista.count(i)

    return {i: nomesDict[i] for i in nomesDict if nomesDict[i] > 1}

lista = ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana", "Carlos", "André"]

print(contarNomesLista(lista))