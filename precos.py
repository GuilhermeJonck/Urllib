import urllib.request


def valores():

    normal = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    texto = normal.read().decode("utf8")
    inicio = texto.find(">$") + 2
    fim = texto.find("<", inicio)
    precoNormal = texto[inicio:fim]

    especial = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto2 = especial.read().decode("utf8")
    inicio2 = texto2.find(">$") + 2
    fim2 = texto2.find("<", inicio2)
    precoEspecial = texto2[inicio2:fim2]

    return precoNormal, precoEspecial
