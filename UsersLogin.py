from config.dbaUsers import User_save_mind as dba_user
import bcrypt as hash
from http import HTTPStatus as statusResponse


class userLogin(dba_user):
    """
    Represents a user login object.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.

    Methods:
        emailSetter(email): Sets the email address of the user.
        passwordSetter(password): Sets the password of the user.
        checkPasswordAndEmail(): Checks if the provided password and email match the stored credentials.
        leerInfo(): Reads the information associated with the user's email.
    """

    def __init__(self, email: str, password: str) -> None:
        super().__init__()
        self.__passwordLogin = password.encode("utf-8")
        self.__emailLogin = email
    
    @property
    def email(self):
        return self.__emailLogin
    
    @email.setter
    def emailSetter(self, email):
        self.__emailLogin = email
        return self.email

    @property
    def password(self):
        return self.__passwordLogin
    
    @password.setter
    def passwordSetter(self, password):
        passwordLogin = password.encode("utf-8")
        salt = hash.gensalt()
        passwordHashLogin = hash.hashpw(passwordLogin, salt)
        self.__passwordLogin = passwordHashLogin

    def checkPasswordAndEmail(self):
        """
        Checks if the provided password and email match the stored credentials.

        Returns:
            If the credentials match, returns the user's ID and a status response of OK.
            If the credentials do not match, returns a status response of CONFLICT.
            If no user is registered with the provided email, returns a message indicating that.
        """
        data = self.traer_user_foreign_key(self.email)
        
        if data != None:
            passwordHash = data[1].encode("utf-8")
            if hash.checkpw(self.password, passwordHash):
                return data[0], statusResponse.OK.value
            else: 
                print("Las contraseñas no coinciden")
                return "Password", statusResponse.UNAUTHORIZED.value
        else:
            print("No existe usuario registrado con tal caracteristica")
            return "Email", statusResponse.UNAUTHORIZED.value
    
    def traerNameWelcome(self):
        data = self.readInformation(self.email)
        return data

