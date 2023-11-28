from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        dest = dest.lower()
        translator = GoogleTranslator(source=src, target=dest)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        from langdetect import detect_langs
        detected_langs = detect_langs(text)

        if set == "lang":
            return detected_langs[0].lang
        elif set == "confidence":
            return detected_langs[0].prob
        elif set == "all":
            return f"Мова: {detected_langs[0].lang}, Коефіцієнт довіри: {detected_langs[0].prob}"
        else:
            return "Неправильний параметр 'set'"
    except Exception as e:
        return f"Помилка визначення мови та коеф. довіри: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        translator = GoogleTranslator()
        supported_languages = translator.get_supported_languages(as_dict=True)

        for code, language in supported_languages.items():
            if language.lower() == lang.lower():
                return code

        lang = lang.lower()
        if lang in supported_languages:
            return supported_languages[lang]

        return f"Мову або код мови '{lang}' не знайдено"
    except Exception as e:
        return f"Помилка: {str(e)}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        translator = GoogleTranslator()
        supported_languages = translator.get_supported_languages(as_dict=True)

        if out == "screen":
            if text:
                table = "N\tLanguage\tISO-639 code\tText\n"
                table += "-" * 50 + "\n"
                for i, (lang, code) in enumerate(supported_languages.items()):
                    detected_lang = detect(text)
                    translation = GoogleTranslator(source=detected_lang, target=code).translate(text)
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\t\t\t\t{translation}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\t\t\t\t{translation}\n"
            else:
                table = "N\tLanguage\tISO-639 code\n"
                table += "-" * 35 + "\n"
                for i, (lang, code) in enumerate(supported_languages.items()):
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\n"
            print(table)
            return "Ok"
        elif out == "file":
            if text:
                with open("langlistdeeptr.txt", "w", encoding="utf-8") as file:
                    file.write("N\tLanguage\tISO-639 code\tText\n")
                    file.write("-" * 50 + "\n")
                    for i, (lang, code) in enumerate(supported_languages.items()):
                        detected_lang = detect(text)
                        translation = GoogleTranslator(source=detected_lang, target=code).translate(text)
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\t\t{translation}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\t\t{translation}\n")
                    return "Ok"
            else:
                with open("langlistdeeptr.txt", "w", encoding="utf-8") as file:
                    file.write("N\tLanguage\tISO-639 code\n")
                    file.write("-" * 35 + "\n")
                    for i, (lang, code) in enumerate(supported_languages.items()):
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\n")
                    return "Ok"
        else:
            return "Invalid 'out' parameter"
    except Exception as e:
        return str(e)