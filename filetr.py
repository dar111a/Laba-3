from googletrans import Translator
from langdetect import detect
import os


def read_config_file(config_filename):
    config = {}
    with open(config_filename, 'r') as config_file:
        for line in config_file:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()
    return config


def translate_text(text, language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=language).text
        return translation, None
    except Exception as e:
        return None, str(e)


def add_language_code_to_filename(filename, language):
    filename_parts = os.path.splitext(filename)
    filename_without_extension = filename_parts[0]
    file_extension = filename_parts[1]
    filename_with_language = f"{filename_without_extension}_{language}{file_extension}"
    return filename_with_language


def main():
    config = read_config_file('config.txt')

    input_filename = config.get('input_filename')
    output_filename = config.get('output_filename')
    max_chars = int(config.get('max_chars'))
    max_words = int(config.get('max_words'))
    max_sentences = int(config.get('max_sentences'))
    language = config.get('language')
    output_destination = config.get('output_destination')

    print(f"Ім'я файлу: {input_filename}")

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            text = input_file.read()
            print(f"Розмір файлу: {len(text)} байтів")
            print(f"Символів: {len(text)}")
            print(f"Слів: {len(text.split())}")
            print(f"Речень: {len(text.split('.'))}")

            detected_language = detect(text)
            print(f"Визначена мова: {detected_language}")

            chars_exceeded = len(text) > max_chars
            words_exceeded = len(text.split()) > max_words
            sentences_exceeded = len(text.split('.')) > max_sentences

            if chars_exceeded or words_exceeded or sentences_exceeded:
                if chars_exceeded:
                    print("Перевищено обмеження по символах.")
                if words_exceeded:
                    print("Перевищено обмеження по словах.")
                if sentences_exceeded:
                    print("Перевищено обмеження по реченнях.")
                return

            print("Переклад тексту...")
            translation, error = translate_text(text, language)

            if error is not None:
                print(f"Під час перекладу сталася помилка: {error}")
                return

            print(f"Мова: {language}")

            if output_destination == 'console':
                print("Результат перекладу:")
                print(translation)
            elif output_destination == 'file':
                if output_filename is not None:
                    output_filename_with_language = add_language_code_to_filename(output_filename, language)
                    with open(output_filename_with_language, 'w', encoding='utf-8') as output_file:
                        output_file.write(translation)
                    print("Переклад збережено у вихідний файл.")

            print("Ok")

    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Під час виконання сталася помилка: {str(e)}")


if __name__ == '__main__':
    main()
