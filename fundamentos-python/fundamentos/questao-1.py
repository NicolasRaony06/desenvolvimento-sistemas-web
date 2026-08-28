def descreverLista(lista : list):
    lista.sort()

    media = 0
    for i in lista:
        media += i

    media /= len(lista)

    return [lista[-1], lista[1], media]


lista = [1,2,3,4,5,6,7,8,10,9]

print(descreverLista(lista))



