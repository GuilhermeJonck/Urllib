import urllib.request

especial = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
texto2 = especial.read().decode("utf8")
inicio2 = texto2.find(">$") + 2
fim2 = texto2.find("<", inicio2)
precoEspecial = texto2[inicio2:fim2]

print(precoEspecial)
