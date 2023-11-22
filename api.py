from googletrans import Translator, LANGUAGES, LANGCODES
import json

translator = Translator()
langs = LANGUAGES
lang_codes = LANGCODES
# converting to json
json_lang = json.dumps(langs)
# print(json_lang)
src = langs['en']
dest = langs['ja']

text1 = "Hello, My name is Tungon Dugi"
translated_text = translator.translate(text1, dest=dest, src=src)
# print(translated_text.text)
# print(translated_text.pronunciation)
# # print(type(src))
for k, v in langs.items():
    print("{}: {}".format(k, v))