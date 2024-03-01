from mysql import connector as conect
from mysql.connector import Error
from http import HTTPStatus as responseStatus

import os as sys
from dotenv import load_dotenv
load_dotenv()
#tabala savemaind
class DbaSaveMind:
    """
    This class represents the database access object for the SaveMind application.
    It provides methods to perform CRUD operations on the 'savewords' table.
    """

    def __init__(self) -> None:
        try:
            self.conect= conect.connect(
                host = 'localhost',#direccion dba
                user = 'root',
                password = sys.getenv("PASSWORD_DBA"),
                database = 'savemindwhioutframework',
                port = '3307'
            )
            print(f"conexion exitosa {responseStatus.ACCEPTED} \r\n")
        except Error as error:
            print(f"ocurrio un error {responseStatus.BAD_REQUEST} -> {error}")

    def __str__(self) -> str:
        return f"conexion establecida {responseStatus.OK}"
    

    #create
    def save(self,id_user:int,languagein: str,languageout, wordsave: str, translateWord: str,context: str = "", status_Save: int = 0):
        """
        Saves a new record in the 'savewords' table.

        Args:
            id_user (int): The ID of the user.
            languagein (str): The input language.
            languageout (str): The output language.
            wordsave (str): The word to be saved.
            translateWord (str): The translated word.
            context (str, optional): The context of the word. Defaults to "".
            status_Save (int, optional): The status of the save operation. Defaults to 0.
        """
        cursor = self.conect.cursor()
        SENTENCIA = "INSERT INTO savemindwhioutframework.savewords(id_user,from_word, to_word, word,translateWord, context_word_use,status) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        VALOR = (id_user,languagein,languageout,wordsave,translateWord,context,status_Save)
        cursor.execute(SENTENCIA,VALOR)
        self.conect.commit()
    
    #delete
    def delete(self, id:int, idUser:int):
        """
        Deletes a record from the 'savewords' table.

        Args:
            id (int): The ID of the record to be deleted.

        Returns:
            str: A message indicating the completion of the deletion.
        """
        cursor = self.conect.cursor()
        SENTENCIA = "DELETE FROM savemindwhioutframework.savewords WHERE id = %s and id_user = %s"
        VALOR = (id,idUser,)
        cursor.execute(SENTENCIA,VALOR)
        self.conect.commit()
        return f"Eliminacion completa {responseStatus.ACCEPTED}"

    def update(self,id:int,status:int):
        """
        Updates the status of a record in the 'savewords' table.

        Args:
            id (int): The ID of the record to be updated.
            status (int): The new status value.

        Returns:
            int: The HTTP status code indicating the success of the update operation.
        """
        try:
            cursor = self.conect.cursor()
            SENTENCIA = "UPDATE savemindwhioutframework.savewords SET context_word_use = %s WHERE id = %s"
            VALOR = (status,id)
            cursor.execute(SENTENCIA,VALOR)
            self.conect.commit()
            return responseStatus.CREATED
        except Error as error:
            print(f"paso un error->{error} \n {responseStatus.CONFLICT}")    

    #bring information
    def readAll(self,idUser):
        """
        Retrieves all records from the 'savewords' table.

        Returns:
            list: A list of records from the 'savewords' table.
        """
        try:
            cursor = self.conect.cursor()
            SENTENCIA = "SELECT * FROM savemindwhioutframework.savewords where id_user = %s"
            VALOR = (idUser,)
            cursor.execute(SENTENCIA,VALOR)
            data = cursor.fetchall()
            if data != []:
                return data
            else:
                return responseStatus.NO_CONTENT
        except Error as error:
            print(f"Ocurrio un error {responseStatus.NOT_FOUND} -> {error}")

    #necesitaria uno que me trajiera solo un registro de la dba

DbaSaveMind().delete(1,1)