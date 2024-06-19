#pip install googletrans==4.0.0-rc1

from googletrans import Translator

def local_translate(text, target_lang='kn', source_lang='en'):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

# Example usage
translated_text = local_translate("Hello, how are you?", 'kn', 'en')
print(translated_text)
