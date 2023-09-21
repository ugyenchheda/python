from googletrans import Translator, constants
from pprint import pprint

translation = translator.translate("Hola Mundo")

print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


from translate import Translator

translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print(translation)
