import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def get_watson_translator():
    """Set up translator instance"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)
    return language_translator

def english_to_french(english_text):
    """Change English to French"""
    #write the code here
    translator = get_watson_translator()
    try:
        french_text = translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
    except:
        return None
    return french_text


def french_to_english(french_text):
    """Change French to English"""
    #write the code here
    translator = get_watson_translator()
    try :
        english_text = translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
    except:
        return None
    return english_text
