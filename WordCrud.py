from config.dbaSavemind import DbaSaveMind 
from translateWord import TranslateWord as traductor

class crudSaveMind(DbaSaveMind):
    """
    This class represents the CRUD operations for saving words in SaveMind.

    Attributes:
        _from_languaje (str): The language code of the word to be translated from.
        _to_languaje (str): The language code of the word to be translated to.
        _word (str): The word to be saved.
        _statusSaved (int): The status of the saved word.
        _context (str): The context of the word.

    Methods:
        Save_Word(id_user): Saves the word in the database.
    """
    #getDataWords = lambda: crudSaveMind.readAll()

    def __init__(self, languaje: list, wordTosave: str, status_save: int = 0, context: str = "") -> None:
        super().__init__()
        self._from_languaje, self._to_languaje = languaje
        self._word = wordTosave
        self._statusSaved = status_save
        self._context = context

    # Setter and getters
    @property
    def from_languaje(self):
        return self._from_languaje

    @from_languaje.setter
    def setter_from_languaje(self, from_languaje):
        self._from_languaje = from_languaje
        return self._from_languaje

    @property
    def to_languaje(self):
        return self._to_languaje

    @to_languaje.setter
    def setter_from_languaje(self, to_languaje):
        self._to_languaje = to_languaje
        return self._to_languaje

    @property
    def word(self):
        return self._word

    @word.setter
    def setter_word(self, word):
        self._word = word
        return self._word

    @property
    def status_save(self):
        return self._statusSaved

    @status_save.setter
    def setter_status_save(self, save):
        self._statusSaved = save
        return self._statusSaved

    @property
    def context(self):
        return self._context

    @context.setter
    def setter_context(self, new_context):
        self._context = new_context
        return self.context

    def __str__(self) -> str:
        return f"{super().__str__(),self._to_languaje,self._from_languaje,self._word,self._statusSaved}"

    def Save_Word_English(self, id_user: int):
        """
        Saves an English word and its translation to the database.

        Args:
            id_user (int): The ID of the user saving the word.

        Returns:
            None
        """
        t = traductor(self._word)
        word_translated = t.Spanish_to_English()
        self.save(id_user, self.from_languaje, self.to_languaje, self.word, word_translated, self.context)
        
    def Save_Word_Español(self, id_user: int):
        """
        Saves a word in Spanish along with its translation to English.

        Args:
            id_user (int): The ID of the user saving the word.

        Returns:
            None
        """
        t = traductor(self._word)
        word_translated = t.English_To_Spanish()
        self.save(id_user, self.from_languaje, self.to_languaje, self.word, word_translated, self.context)


    def getDataWords(self,id):
        data = self.readAll(id)
        for dataword in range(len(data)):
            print(
                f"""
                Id palabra: {data[dataword][0]}
                Idioma de entrada e Idioma de salida: {data[dataword][2]}, {data[dataword][3]}
                Palabra de entrada: {data[dataword][4]}
                Palabra de salida: {data[dataword][5]}
                contexto: {data[dataword][6]}
                """
            )
