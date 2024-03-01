from config.dbaUsers import User_save_mind as dba_user
import re
from datetime import date
from dateutil import parser
import bcrypt
from http import HTTPStatus as statusResponse

#from Envio_Correo import Send_Email as newUser

class Userregister(dba_user):
    """
    Represents a user registration.

    Args:
        name (str): The user's name.
        lastname (str): The user's last name.
        number (int): The user's phone number.
        email (str): The user's email address.
        birthday (date): The user's birthday.
        password (str): The user's password.

    Attributes:
        __nam (str): The user's name.
        __lastNam (str): The user's last name.
        __number (int): The user's phone number.
        __email (str): The user's email address.
        __birt (date): The user's birthday.
        __passw (str): The user's password.
    """

    def __init__(self, name: str, lastname: str, number: int, email: str, birthday: date, password: str) -> None:
        super().__init__()
        self.__nam = name
        self.__lastNam = lastname
        self.__number = number
        self.__email = email 
        self.__birt = birthday
        self.__passw = password

    #la comprobaciones de veracidad se deben hacen en otro archivo o al momento de crear el main        

    #getter and setter
    @property
    def name(self):
        return self.__nam
    @name.setter
    def nameSetter(self,name):
        self.__nam = name
        return self.name
        
    @property
    def lastNam(self):
        return self.__lastNam
    @lastNam.setter
    def lastNamSetter(self,lastname):
        self.__lastNam = lastname
        return self.lastNam

    @property
    def number(self):
        return self.__number
    @number.setter
    def numberSetter(self,number):
        if len(number) != 10:
            return "vuelva a escribir su numero", self.numberSetter
        else:
            self.__number = number
        return self.number
    
    @property
    def email(self):
        return str(self.__email)
    @email.setter
    def emailSetter(self,email):
        veri_email = re.search("@,*.com$",email)
        if veri_email:
            self.__email = email
        else:
            return "Correo incorrecto", self.emailSetter
    
    @property
    def birthay(self):
        return self.__birt
    @birthay.setter
    def birthaySetter(self,birthay):
        try:
            fecha_date = parser.parse(birthay).date()
            self.__birt = fecha_date
        except ValueError as e:
            print(f"Error: {e}")
            self.birthaySetter
            
    @property
    def password(self):
        return self.__passw
    @password.setter
    def passwordSetter(self, password):
        password_encode = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_encode,salt)
        self.__passw = password_hash
    
    def registroUser(self):
        self.passwordSetter = self.__passw
        self.saveUser(self.name,self.lastNam,self.number,self.email,self.birthay,self.password)
        #envio de token
        return statusResponse.CREATED
        