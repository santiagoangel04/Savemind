from ..config.dbaUsers import User_save_mind
import re
from datetime import date
from dateutil import parser
import bcrypt
import secrets as token

class User(User_save_mind):
    def __init__(self,name:str,lastname:str,number:int,email:str,birthday:date,password:str) -> None:
        super().__init__()
        self.__nam = name
        self.__lastNam = lastname
        self.__number = number
        self.__email = email
        self.__birt =birthday
        self.__passw = password

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
        return self.__email
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
        if len(password) >= 16:
            password_encode = password.encode('utf-8')
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password_encode,salt)
            self.__passw = password_hash

    def tokenGenerator():
        digits = token.choice((0,1,2,3,4,5,6,7,8,9))
        print(digits)

    def autenticator_email(self):
        pass
    




a = User()
a.tokenGenerator()