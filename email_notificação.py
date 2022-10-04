from email.utils import localtime
import smtplib
import time


def notifica(valor, barato):
    mes, dia, hora, minuto, _ = time.localtime()[1:6]
    mensagem = f"""Subject: Promoção de Café

                                                
    Café está muito Barato, Café {barato} ${valor}!!!        
            COMPRE LOGO!!!                           
    Data De Atualização : Dia {dia}/{mes} ás {hora}:{minuto}   
                                            

        """.encode(
        "utf-8"
    )
    destinario = ["@example.com"]
    mail, senha = "@example.com", "password"
    smtpObj = smtplib.SMTP(
        "smtp-mail.outlook.com", 587
    )  # porta válida para enviar e-mail apartir do outlook
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(mail, senha)
    smtpObj.sendmail(mail, destinario, mensagem)
    smtpObj.quit()
    return print("Enviando Mensagem...")
