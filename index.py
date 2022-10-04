from email_notificação import notifica
from precos import valores
import time


def main():
    while True:

        normal, especial = valores()

        mes, dia, hora, minuto, segundo = time.localtime()[1:6]

        print(
            f"""
        Preço do Café Hoje >> {normal}
        Data da Consulta >>{dia}/{mes} ás {hora}H:{minuto}Min:{segundo}sec

        Preço do Café Oferta Especial Hoje >> {especial}
        Data da Consulta >>{dia}/{mes} ás {hora}H:{minuto}Min:{segundo}sec

        """
        )
        if float(especial) < 4.70:
            barato, valor = "especial", especial
            notifica(valor, barato)
            break
        elif float(normal) < 4.70:
            barato, valor = "normal", normal
            notifica(valor, barato)
            break

        time.sleep(2)


if __name__ == "__main__":
    main()
