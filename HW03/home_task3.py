alph = 'абвгндеёжзийклмнопрстуфхцчшщъыьэюя'
while True:
    word = input('Введите слово: ')
    if not word:
        break
    else:
        word = word.strip('.,"!?/')
        word = word.lower()
        for i, symb in enumerate(word):
            if symb in alph:
                while i < len(word)//2:
                    print(symb)
                    break
            else:
                print("Используйте только кириллические символы!")
                break
