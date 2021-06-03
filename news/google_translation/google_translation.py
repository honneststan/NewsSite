from google_trans_new import google_translator


def LanguageConversionGTN(content):
    translatorGTN = google_translator()
    return translatorGTN.translate(content, lang_tgt='en')


def ArticleConversion(nepali_article):
    english_article = LanguageConversionGTN(nepali_article)
    return english_article
