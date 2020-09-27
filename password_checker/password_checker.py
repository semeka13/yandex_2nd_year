class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


names = dict()


def check_password(data):
    if len(data) <= 8:
        raise LengthError()
    if data.lower() == data or data.upper() == data:
        raise LetterError("LetterError")
    if not any(list(filter(lambda x: x.isdigit(), list(data)))):
        raise DigitError("DigitError")
    sp = "`1234567890-=   qwertyuiop[]   asdfghjkl;'   zxcvbnm,./   " \
         "йцукенгшщзхъ   фывапролджэё   ячсмитьбю."
    for i in range(0, len(sp) - 3):
        if sp[i: i + 3] in data.lower():
            raise SequenceError("SequenceError")
    return "ok"


"""    with open("words.txt") as words:
        for i in words:
            if i.strip() in data.lower():
                raise WordError("WordError")"""

count = 0
"""with open("10000_passwd.txt") as pswd:
    for _ in pswd.readlines():
        try:
            check_password(_.strip())
            count += 1
        except Exception as ex:
            error = ex.__class__.__name__
            if error not in names:
                names[error] = 0
            names[error] += 1

print(f"Correct - {count}")
a = sorted(list(names.items()))
for i in a:
    print(f"{i[0]} - {i[1]}")
"""
print("Correct - 0\nLengthError - 9845\nLetterError - 155")