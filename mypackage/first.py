from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        dest = dest.lower()
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
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
        lang_lower = lang.lower()
        if lang_lower in LANGUAGES:
            return LANGUAGES[lang_lower]
        for code, name in LANGUAGES.items():
            if name.lower() == lang_lower:
                return code
        return f"Мову або код мови '{lang}' не знайдено"
    except Exception as e:
        return f"Помилка: {str(e)}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        if out == "screen":
            if text:
                table = "N\tLanguage\tISO-639 code\tText\n"
                table += "-" * 50 + "\n"
                for i, (code, lang) in enumerate(LANGUAGES.items()):
                    translation = translator.translate(text, src="auto", dest=code)
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\t\t\t\t{translation.text}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\t\t\t\t{translation.text}\n"
                print(table)
                return "OK"
            else:
                table = "N\tLanguage\tISO-639 code\n"
                table += "-" * 35 + "\n"
                for i, (code, lang) in enumerate(LANGUAGES.items()):
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\n"
                print(table)
                return "OK"
        elif out == "file":
            if text:
                with open("langlistgtrans.txt", "w", encoding="utf-8") as file:
                    file.write("N\tLanguage\tISO-639 code\tText\n")
                    file.write("-" * 50 + "\n")
                    for i, (code, lang) in enumerate(LANGUAGES.items()):
                        translation = translator.translate(text, src="auto", dest=code)
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\t\t{translation.text}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\t\t{translation.text}\n")
                return "OK"
            else:
                with open("langlistgtrans.txt", "w", encoding="utf-8") as file:
                    file.write("N\tLanguage\tISO-639 code\n")
                    file.write("-" * 35 + "\n")
                    for i, (code, lang) in enumerate(LANGUAGES.items()):
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\n")
                return "OK"
        else:
            return "Неправильний параметр 'out'"
    except Exception as e:
        return str(e)