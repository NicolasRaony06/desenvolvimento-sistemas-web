import re   

def descreverString(texto : str):
    vogais = re.findall("[aeiouAEIOU]", texto)

    texto_invertido = []
    for i in texto:
        texto_invertido.insert(0, i)

    texto_invertido = ''.join(texto_invertido)

    return [len(vogais), texto_invertido, texto.lower() == texto_invertido.lower()]


texto = "Osso"
print(descreverString(texto))