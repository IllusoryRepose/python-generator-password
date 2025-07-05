import secrets
import string
import argparse

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def generate_password(length=16, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    if not characters:
        return "Ошибка: Должен быть выбран хотя бы один набор символов."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def shaurma():
    parser = argparse.ArgumentParser(description="Генератор случайных паролей")
    parser.add_argument("-l", "--length", type=int, default=16, help="Длина пароля (по умолчанию: 16)")
    parser.add_argument("--no-letters", action="store_false", dest="use_letters", help="Не включать буквы")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Не включать цифры")
    parser.add_argument("--no-symbols", action="store_false", dest="use_symbols", help="Не включать символы")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_letters=args.use_letters,
        use_digits=args.use_digits,
        use_symbols=args.use_symbols
    )

    print("Ваш пароль:", password)

if __name__ == "__main__":
    shaurma()
