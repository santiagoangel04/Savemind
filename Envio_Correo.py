from datetime import date
from email.message import EmailMessage as sender_email
import smtplib
from http import HTTPStatus as responseStatus
import secrets as token
import time
import os as sys
from dotenv import load_dotenv

class Send_Email:
    def __init__(self,email:str) -> None:
        self.email = email

    load_dotenv()
    def tokenEmail(self):
        authToken = ""
        for i in range(6):
            authToken += str(token.choice((0,1,2,3,4,5,6,7,8,9))) 
        time_expiration = 300
        time_creation_token = time.time()
        expiration = time_creation_token + time_expiration
        response = responseStatus.OK
        print(response)
        return authToken,expiration    
    
    def sendEmail(self,autToken:int):
        remitente = "savemindorgco@gmail.com"
        destinatario = self.email
        mensaje = f"Tu codigo de verificacion es: {autToken}, tienes un tiempo de 5 minutos antes de que este pierda validez"
        email = sender_email()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Codigo de verificación"
        email.set_content(mensaje)
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente,sys.getenv("KEY_APP_GMAIL"))
        smtp.sendmail(remitente,destinatario,email.as_string())
        smtp.quit()

    def autenticator_email(self,token_send,token_recive,expiration_time):
        while True:
            if (token_send == token_recive) and not (expiration_time < time.time()):
                #se registra el usuario en la dba
                print("Usuario registrado")
                return True
            elif token_send != token_recive:
                print("Token no valido")
                return False
            else:
                print("El tiempo a expirado")
                return False


