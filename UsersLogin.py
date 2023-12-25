from config.dbaUsers import User_save_mind as dba_user
import bcrypt as hash
from http import HTTPStatus as statusResponse


class userLogin(dba_user):
    def __init__(self,email:str,password:str) -> None:
        super().__init__()
        self.__passwordLogin = password.encode("utf-8")
        self.__emailLogin = email
    
    @property
    def email(self):
        return self.__emailLogin
    @email.setter
    def emailSetter(self,email):
        self.__emailLogin = email
        return self.email

    @property
    def password(self):
        return self.__passwordLogin
    @password.setter
    def passwordSetter(self,password):
        passwordLogin = password.encode("utf-8")
        salt = hash.gensalt()
        passwordHashLogin = hash.hashpw(passwordLogin,salt)
        self.__passwordLogin = passwordHashLogin

    def checkPasswordAndEmail(self):
        passwordHash = self.autPassword(self.email)
        if hash.checkpw(self.password,passwordHash):
            id = self.traer_user_foreign_key(self.email)
            return True, id,statusResponse.OK
        else: 
            print("Las contraseñas no coinciden")
            return False,statusResponse.CONFLICT
    
    def leerInfo(self):
        return self.readInformation(self.email)
    

a = userLogin("eyerforeversam@gmail.com","123456789Aa@")
print(a.checkPasswordAndEmail())