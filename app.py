from UsersRegister import Userregister as register
import re
from UsersLogin import userLogin as login
from WordCrud import crudSaveMind as wordSave
import os
import time
from Envio_Correo import Send_Email as tokenEmail
class App:
    """
    This class represents an application with various functionalities such as user registration, login, and word translation.
    """

    displayClean = lambda: os.system('cls')

    def verificadorPasswordAndEmail(self):
        #[^@]+: Cualquier carácter que no sea "@", al menos una vez.
        #@: El carácter "@", que debe estar presente.
        #[^@]+: Cualquier carácter que no sea "@", al menos una vez.
        #\.: El carácter "." (se debe escapar con ""), que debe estar presente.
        #[^@]+: Cualquier carácter que no sea "@", al menos una vez.
        countPasswo = 0
        password = self.passwordDef()
        if len(password) >= 16:        
            if re.search(r"[a-z]",password):
                countPasswo+=1
            else:
                print("contraseña no contiene letras minusculas")
            if re.search(r"[A-Z]",password):
                countPasswo+=1
            else:
                print("contraseña no contiene letras Mayusculas")
            if re.search(r"\d",password):
                countPasswo+=1
            else:
                print("contraseña no contiene digitos")
            if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                countPasswo+=1
            else:
                print("contraseña no contiene caracteres especiales")
        else:
            print("contraseña no contiene 16 caracteres, esta contiene -> ",len(password))
            countPasswo = 0

        return password if countPasswo == 4 else self.verificadorPasswordAndEmail()

    def registrarNewUser(self):
        App.displayClean()
        name = input("Ingrese su Nombre \n\r")
        lastname = input("Ingrese su Apellido \n\r")
        number = int(input("Ingrese su Telefono \n\r"))
        email = input("Ingrese su email \n\r")
        birthday = input("Ingrese su fecha de nacimiento, esto de la siguiente manera /yyyy-mm-d/ \n\r")
        password = self.verificadorPasswordAndEmail()
        if self.enviarToken(email): 
            newUser = register(name,lastname,number,email,birthday,password)
            newUser.registroUser()
        #aqui antes de guardar debemos enviar un numero de 4 digitos por correo para la autenticacion del usuario

    def passwordDef(self):
        password = input("Ingrese una contraseña \n\r")
        print("Escriba de nuevo su contraseña")
        passwordAgain = input()
        if password == passwordAgain:
            return passwordAgain
        else:
            print("Las Contraseñas no coinciden \n\r")
            self.passwordDef()

    def LoginUser(self):
        App.displayClean()
        email = email = input("Ingrese su email \n\r")
        password = input("Ingrese su password \n\r")
        userLogin = login(email,password)
        infoUser = userLogin.traerNameWelcome()
        return userLogin.checkPasswordAndEmail(),infoUser
    
    def menuWord(self,idUser:int):
        App.displayClean()
        print(
            """
            Menu:
            1) Tradducir palabra y guardar
            2) Ver lista de palabras Guardadas
            3) Eliminar palabra
            4) modificar contexto
            5) Salir
            """
        )
        print("Indique la opcion deseada")
        opcion = int(input())
        if opcion == 1:
            App.displayClean()
            print(
                """
                1) Español a Ingles
                2) Ingles a Español
                """
            )
            opcionLanguaje = int(input())
            if opcionLanguaje == 1:
                App.displayClean()
                palabra = input("Ingrese la palabra que desea traducir: \n\r")
                contexto = input("Escriba el contexto de manera que usted pueda entender y recordar esta palabra: \n\r")
                word_Save_User = wordSave(['es','en'],palabra,1,contexto)
                word_Save_User.Save_Word_English(idUser)
                self.menuWord(idUser)
            else:
                App.displayClean()
                palabra = input("Ingrese la palabra que desea traducir: \n\r")
                contexto = input("Escriba el contexto de manera que usted pueda entender y recordar esta palabra: \n\r")
                word_Save_User = wordSave(['es','en'],palabra,1,contexto)
                word_Save_User.Save_Word_Español(idUser)
                self.menuWord(idUser)

        elif opcion == 2:
            wordSave(['es','en'],"prueba",1,"").getDataWords(idUser)#debo poner crear un nuevo objeto para poder acceder al metodo
            time.sleep(10)
            self.menuWord(idUser)
        elif opcion == 3:
            App.displayClean()
            print("Para poder eliminar la palabra ingrese el id: \n\r")
            idWord = int(input())
            wordSave(['es','en'],"prueba",1,"").delete(idWord,idUser)
            self.menuWord(idUser)
        elif opcion == 4:
            App.displayClean()
            print("Ingrese el id a modificar ")
            idWord = int(input())
            print("Ingrese el nuevo contexto a modificar")
            contexto = input()
            wordSave.update(idWord,contexto)
            self.menuWord()
        else:
            self.principalEjecution()
    
    @staticmethod
    def principalEjecution():
        app = App()
        print("Desea regsitrarse o ya tiene cuenta: ")
        print(
            """
            1. Registrarse
            2. Iniciar Sesion
            """
        )
        opcion = int(input(">> Ingrese una opcion \n\r"))
        if opcion == 1:
            app.registrarNewUser()
        else:
            verid, infoUser= app.LoginUser()
            id =  int(verid[0])
            while verid[1] != 200:
                if verid[0] == "Email":
                    print("Para poder ingresar debe registrarse")
                    app.registrarNewUser()
                elif verid[0] == "Password":
                    verid=app.LoginUser()
                    verid=verid[0]
            print(f"Bienvenido {infoUser[0][0]} {infoUser[0][1]} {id}")
            app.menuWord(id)
    @staticmethod
    def enviarToken(email:str):
        token_email = tokenEmail(email)
        token = token_email.tokenEmail()
        token_email.sendEmail((int(token[0])))
        tokenR = int(input("Ingrese el token enviado para poder ser registrado: "))
        responseToken=token_email.autenticator_email((int(token[0])),tokenR,token[1])
        return responseToken
    
    
"""a = App()

a.menuWord(1)"""