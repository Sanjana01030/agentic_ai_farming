from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from deep_translator import GoogleTranslator


# Thanglish -> Tamil
def thanglish_to_tamil(text):

    try:
        tamil = transliterate(text, sanscript.ITRANS, sanscript.TAMIL)
        return tamil
    except:
        return text


# Tamil -> English
def tamil_to_english(text):

    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except:
        return text


# English -> Tamil
def english_to_tamil(text):

    try:
        return GoogleTranslator(source="en", target="ta").translate(text)
    except:
        return text
        