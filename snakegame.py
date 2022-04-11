import googletrans
from googletrans import Translator

print(googletrans.LANGCODES)

translator = Translator()

text = input("Text which want to translate: ")
language = input("What language to translate: ")

result = translator.translate(text, dest=language)

print(f"Original ({result.src}) : {result.origin}")
print(f"Translated ({result.dest}) : {result.text}")