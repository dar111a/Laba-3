from mypackage.first import CodeLang, TransLate, LangDetect, LanguageList

text_to_translate = "Добрий день"
print("Переклад тексту 'Добрий день' на англ. мову:")
translated_text = TransLate(text_to_translate, "auto", "en")
print(f"| Текст для перекладу | Результат перекладу |")
print(f"|-----------------------|----------------------|")
print(f"| {text_to_translate:^21} | {translated_text:^20} |")

print("\nВизначення мови та коеф. довіри тексту 'Добрий день':")
lang_detection_result = LangDetect(text_to_translate, "all")
print(f"| Текст для визначення | Результат визначення |")
print(f"|-----------------------|----------------------|")
print(f"| {text_to_translate:^21} | {lang_detection_result:^20} |")

print("\nНазва мови коду 'uk':")
lang_name = CodeLang("uk")
print(f"| Код мови | Назва мови |")
print(f"|----------|------------|")
print(f"|    uk    | {lang_name:^10} |")

print("\nКод мови 'ukrainian':")
lang_code = CodeLang("ukrainian")
print(f"| Назва мови | Код мови |")
print(f"|------------|----------|")
print(f"| {lang_code:^11} |   ukr    |")

print("\nСписок мов у консолі:")
print(f"|----- |--------------|--------------|")
LanguageList("screen")

print("\nСписок мов у файлі:")

LanguageList("file", text_to_translate)
