from translate import Translator #La clase translator es la unica que no pedirauna api key

#forma de creacion del translate
"""
tranlation = Translator(to_lang="es",from_lang="en")
response = tranlation.translate("hello world")
print(response)
"""
class TranslateWord:
    def __init__(self,wordTotranslate):
        self.word_to_translate = wordTotranslate

    def __str__(self) -> str:
        return self.word_to_translate
    

    def English_To_Spanish(self):
        """
        This function can be translate anyword from english to spanish,
        the function not receive parameters
        """
        traductor = Translator(to_lang='es',from_lang='en')
        return traductor.translate(self.word_to_translate)#significa que el resultado es la traduccion de ingles a espanol

    def Spanish_to_English(self):
        """
        This function can be translate anyword from spanish to english,
        the function not receive parameters
        """
        traductor = Translator(to_lang='en',from_lang='es')
        return traductor.translate(self.word_to_translate)
    
    #here would be more functions with other translations

