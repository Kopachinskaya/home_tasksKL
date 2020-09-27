alph = 'абвгндеёжзийклмнопрстуфхцчшщъыьэюя'
word = input('Введите слово: ').lower()
t = "Используйте только кириллические символы!"

for i, symb in enumerate(word):
    if symb in alph:
        if (i+1) % 2 == 0:
            if symb != 'к' and symb != 'а':
                print(symb)
            else:
                None
    else:
        print(t)
        break

        
