from datetime import date
from email.message import EmailMessage as sender_email
import smtplib
from http import HTTPStatus as responseStatus
import secrets as token
import time
import os as sys
from dotenv import load_dotenv

class Send_Email:
    def __init__(self, email: str) -> None:
        # Inicializa la clase con el email del destinatario
        self.email = email

    load_dotenv()  # Carga las variables de entorno desde el archivo .env

    def tokenEmail(self):
        """
        Genera un token de autenticación de 6 dígitos y establece un tiempo de expiración de 5 minutos.
        Retorna el token y su tiempo de expiración.
        """
        authToken = ""  # Variable para almacenar el token
        for i in range(6):
            # Genera cada dígito del token de forma aleatoria y lo añade a authToken
            authToken += str(token.choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
        
        time_expiration = 300  # Tiempo de expiración en segundos (5 minutos)
        time_creation_token = time.time()  # Momento de creación del token
        expiration = time_creation_token + time_expiration  # Calcula el tiempo de expiración
        response = responseStatus.OK  # Estado HTTP como respuesta de éxito
        print(response)  # Muestra el estado en la consola
        return authToken, expiration  # Retorna el token y el tiempo de expiración

    def sendEmail(self, autToken: int):
        """
        Envía un correo electrónico al destinatario con un mensaje que contiene el token de autenticación.
        """
        remitente = "savemindorgco@gmail.com"  # Dirección de correo del remitente
        destinatario = self.email  # Dirección de correo del destinatario
        mensaje = f"Tu codigo de verificacion es: {autToken}, tienes un tiempo de 5 minutos antes de que este pierda validez"  # Contenido del mensaje
        email = sender_email()  # Crea un objeto de mensaje de correo electrónico
        email["From"] = remitente  # Asigna el remitente al correo
        email["To"] = destinatario  # Asigna el destinatario al correo
        email["Subject"] = "Codigo de verificación"  # Asigna el asunto del correo
        email.set_content(mensaje)  # Asigna el contenido del mensaje
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")  # Conecta con el servidor de Gmail usando SSL
        smtp.login(remitente, sys.getenv("KEY_APP_GMAIL"))  # Inicia sesión usando la clave almacenada en variables de entorno
        smtp.sendmail(remitente, destinatario, email.as_string())  # Envía el correo electrónico
        smtp.quit()  # Cierra la conexión SMTP

    def autenticator_email(self, token_send, token_recive, expiration_time):
        """
        Verifica si el token proporcionado coincide con el token enviado y si aún no ha expirado.
        """
        while True:
            # Compara el token enviado y el recibido, y verifica si aún no ha expirado
            if (token_send == token_recive) and not (expiration_time < time.time()):
                # Si ambos son válidos, se registra el usuario en la base de datos
                print("Usuario registrado")
                return True
            elif token_send != token_recive:
                # Si los tokens no coinciden, muestra un mensaje de error
                print("Token no valido")
                return False
            else:
                # Si el token ha expirado, muestra un mensaje de expiración
                print("El tiempo a expirado")
                return False
