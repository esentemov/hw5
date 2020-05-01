print("Программа проверяет, является ли введенный вами текст палиндромом")

while True:
    txt = input("Введите текст: ")
    if txt == 'stop':
        break
    a = txt[::-1]
    if txt == a:
        print("Это палиндром")
    else:
        print("Это не палиндром")
