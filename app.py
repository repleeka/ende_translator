from flask import Flask, render_template, request, make_response
from googletrans import Translator, LANGUAGES
app = Flask(__name__)


@app.route('/')
def index():
    title = "Home"
    return render_template('home.html', title=title)


@app.route('/about')
def about():
    title = "About"
    return render_template("about.html", title=title)


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    # Set the page title
    title = "Translator"

    # Get the list of supported languages
    langs = LANGUAGES

    # Create the Google Translate API translator object
    translator = Translator()

    # Retrieve the value of the 'selected_src_language' cookie from the request,
    # defaulting to 'en' if the cookie is not present
    active_src_language = request.cookies.get(
        'selected_src_language', default='en')

    # Retrieve the value of the 'selected_dest_language' cookie from the request,
    # defaulting to 'ja' if the cookie is not present
    active_dest_language = request.cookies.get(
        'selected_dest_language', default='ja')

    if request.method == "POST":

        # Get the source language code from the form
        src_code = request.form.get('src_language')

        # Get the text to translate from the form
        src_text = request.form.get('textToTranslate')

        # Get the destination language code from the form
        dest_code = request.form.get('dest_language')

        # Translate the text using the codes
        dest_text = translator.translate(
            src_text, dest=dest_code, src=src_code).text

        # Get the pronunciation for the translated text
        dest_pronunciation = translator.translate(
            src_text, dest=dest_code, src=src_code).pronunciation

        # Set the selected language in a cookie that expires in 30 days (you can adjust the expiration)
        resp = make_response(render_template(
            'translator.html',
            langs=langs,
            dest_text=dest_text,
            dest_pronunciation=dest_pronunciation,
            title=title,
            src_text=src_text,
            active_src_language=src_code,
            active_dest_language=dest_code
        ))
        # Set the source language cookie with a value of src_code and a maximum age of 30 days
        resp.set_cookie('selected_src_language', value=src_code,
                        max_age=30*24*60*60)  # 30 days expiration

        # Set the destination language cookie with a value of dest_code and a maximum age of 30 days
        resp.set_cookie('selected_dest_language', value=dest_code,
                        max_age=30*24*60*60)  # 30 days expiration

        # Return the response object to render the 'translator.html' page with translated text and other details
        return resp

    else:
        # Handle the GET request, render the page
        return render_template(
            'translator.html',
            title=title,
            langs=langs,
            active_src_language=active_src_language,
            active_dest_language=active_dest_language
        )
