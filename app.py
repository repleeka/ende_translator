from flask import Flask, render_template, request
from googletrans import Translator
import json

app = Flask(__name__)


@app.route('/')
def index():
    title = "Home"
    return render_template('index.html', title=title)


reversed_text = []


@app.route('/reverse', methods=['POST', 'GET'])
def reverse():
    title = "Reverse"
    text = request.form.get('textToTranslate')
    if not text:
        return render_template('index.html',  title=title)
    else:
        # appending and reversing the latest entry in the list
        reversed_text.append("{}".format(text[::-1]))
        return render_template('index.html', reversed_text=reversed_text, title=title)


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    title = "Translator"
    translator = Translator()
    src = 'en'
    dest = 'ja'
    src_text = request.form.get('textToTranslate')
    if not src_text:
        return render_template('index.html', title=title)
    else:
        # translating the text
        dest_text = translator.translate(src_text, dest=dest, src=src).text
        dest_pronunciation = translator.translate(
            src_text, dest=dest, src=src).pronunciation
        return render_template('index.html', dest_text=dest_text, dest_pronunciation=dest_pronunciation, title=title)


@app.route('/clear', methods=['POST', 'GET'])
def clear_list():
    title = "Clear"
    txt = reversed_text.clear()
    return render_template('index.html', txt=txt, title=title)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
