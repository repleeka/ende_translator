from googletrans import Translator, LANGUAGES
import json

translator = Translator()
languages = LANGUAGES

# converting to json
json_lang = json.dumps(languages)
# print(json_lang)
src = languages['en']
dest = languages['ja']

text1 = "Hello, My name is Tungon Dugi"
translated_text = translator.translate(text1, dest=dest, src=src)
print(translated_text.text)
print(translated_text.pronunciation)
# print(type(src))
