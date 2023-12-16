from mysql import connector as conect
from mysql.connector import Error 
from http import HTTPStatus as responseStatus 
from datetime import datetime as tiempo
from dotenv import load_dotenv 
import os as sys

load_dotenv()
#tabla user
class User_save_mind():
    """
    Represents a user in the SaveMind application.

    Attributes:
    - conect: The database connection object.
    """

    def __init__(self) -> None:
        try:
            self.conect= conect.connect(
                host = 'localhost',#direccion dba
                user = 'root',
                password = sys.getenv("PASSWORD_DBA"),
                database = 'savemind',
                port = '3307'
            )
            print(f"conexion exitosa {responseStatus.ACCEPTED} \r\n")
        except Error as error:
            print(f"ocurrio un error {responseStatus.BAD_REQUEST} -> {error}")

    def __str__(self) -> str:
        return f"conexion establecida {responseStatus.OK}"

    def saveUser(self,name:str,lastname:str,number:int,email:str,birthday:str,password:str):
        """
        Saves a user to the database.

        Parameters:
        - name: The user's name.
        - lastname: The user's last name.
        - number: The user's phone number.
        - email: The user's email address.
        - birthday: The user's birthday.
        - password: The user's password.
        """
        cursor = self.conect.cursor()
        SENTENCIA = "INSERT INTO savemind.user_savemind(name,lastname,number,email,password,birthday) VALUES(%s,%s,%s,%s,%s,%s)"
        VALOR = (name,lastname,number,email,password,birthday)
        cursor.execute(SENTENCIA,VALOR)
        self.conect.commit()

    def traer_user_foreign_key(self,email:str):
        """
        Retrieves a user from the database based on their email address.

        Parameters:
        - email: The user's email address.

        Returns:
        - dataUser: The user's data as a tuple.
        """
        cursor = self.conect.cursor()
        SENTENCIA = "SELECT id FROM savemind.user_savemind where email = %s"
        VALOR = (email)
        cursor.execute(SENTENCIA,VALOR)
        dataUser = cursor.fetchone()
        print(dataUser)
    
    #usuario info
    def readInformation(self,id):
        cursor = self.conect.cursor()
        SENNTENCIA = "SELECT name,lastname, number, email, birthday FROM savemind.user_savemind WHERE id = %s"
        VALOR = (id)
        cursor.execute(SENNTENCIA,VALOR)
        data = cursor.fetchone() 