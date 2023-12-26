import sentencepiece as spm
import nltk
import ctranslate2
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    title = "Home"
    return render_template('home.html', title=title)


@app.route('/about')
def about():
    title = "About"
    return render_template("about.html", title=title)


def trans(source, translator, sp_source_model, sp_target_model):
    """Use CTranslate model to translate a sentence
        Args:
            source (str): Source sentences to translate
            translator (object): Object of Translator, with the CTranslate2 model
            sp_source_model (object): Object of SentencePieceProcessor, with the SentencePiece source model
            sp_target_model (object): Object of SentencePieceProcessor, with the SentencePiece target model
        Returns:
            Translation of the source text
    """
    source_sentences = nltk.sent_tokenize(source)
    source_tokenized = sp_source_model.encode(
        source_sentences, out_type=str)
    translations = translator.translate_batch(source_tokenized)
    translations = [translation[0]["tokens"]
                    for translation in translations]
    translations_detokenized = sp_target_model.decode(translations)
    translation = " ".join(translations_detokenized)

    return translation


# [Modify] File paths here to the CTranslate2 SentencePiece models.
ct_model_path = "ende_ct2"
sp_source_model_path = "models/sentencepiece.model"
sp_target_model_path = "models/sentencepiece.model"

# Create objects of CTranslate2 Translator and SentencePieceProcessor to load the models
translator = ctranslate2.Translator(
    ct_model_path, "cpu")    # or "cuda" for GPU
sp_source_model = spm.SentencePieceProcessor(sp_source_model_path)
sp_target_model = spm.SentencePieceProcessor(sp_target_model_path)


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    # ct2-opennmt-py-converter --model_path model.pt --output_dir ct2_model

    title = "English to German Translator"

    if request.method == "POST":
        user_input = request.form.get('textToTranslate')
        if not user_input:
            error = "Please enter text to translate."
            return render_template('translator.html', title=title, error=error)
        try:
            translation = trans(user_input, translator,
                                sp_source_model, sp_target_model)
            return render_template('translator.html', translation=translation, title=title, user_input=user_input)
        except Exception as e:
            error = "Translation error: {}".format(e)
            return render_template('translator.html', error=error, title=title)
    return render_template('translator.html', title=title)
