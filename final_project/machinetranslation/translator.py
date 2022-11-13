import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import urllib

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def translation(text, model_id):
    if text == '':
        return 'Text for translation is missing'
    translation = language_translator.translate(
        text=text,
        model_id=model_id).get_result()
    return translation['translations'][0]['translation']

def english_to_french(english_text):
    return translation(english_text, 'en-fr')

def french_to_english(french_text):
    return translation(french_text, 'fr-en')