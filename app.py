from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES, LANGCODES
import json

app = Flask(__name__)

langs = LANGUAGES
lang_codes = LANGCODES

# app routes

@app.route('/')
def index():
    title = "Home"
    return render_template('home.html', title=title)


@app.route('/about')
def about():
    title = "About"
    return render_template("about.html", title=title)


@app.route('/pricing')
def pricing():
    title = "Pricing"
    return render_template("pricing.html", title=title)


@app.route('/subscribe')
def subscribe():
    title = "Newsletter"
    return render_template('subscribe.html', title=title)


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    title = "Translator"
    translator = Translator()
    src = 'en'
    dest = 'ja'
    src_text = request.form.get('textToTranslate')
    if not src_text:
        return render_template('translator.html', title=title)
    else:
        # translating the text
        dest_text = translator.translate(src_text, dest=dest, src=src).text
        dest_pronunciation = translator.translate(
            src_text, dest=dest, src=src).pronunciation
        return render_template('translator.html', dest_text=dest_text, dest_pronunciation=dest_pronunciation, title=title)