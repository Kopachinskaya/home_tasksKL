import os
import string

def files():
    lst = os.listdir('.')
    folds = []
    files = []
    for name in lst:
        if '.' not in name:
            folds.append(name)
        else:
            files.append(name)
            
#папки, название которых состоит из более чем одного слова.
    i = 0
    for fold in folds:
        if len(fold.split()) > 1:
            i += 1
    print('Кол-во папок, название которых состоит из более чем одного слова - ',i)
    
#файлы, не содержащих цифр в названии
    files_numb = []
    for file in files:
        for symb in file:
            if symb in string.digits:
                files_numb.append(file)
    numbless_files = set(files) - set(files_numb)
    print('Кол-во файлов, не содержащих цифр в названии - ', len(set(numbless_files)))
    
#файлы, название которых состоит только из латинских символов
    not_latin = []
    for file in numbless_files:
        for symb in file.replace('.','').replace(' ',''):
            if symb not in string.ascii_letters or symb in string.punctuation:
                not_latin.append(file)
    files_latin = set(numbless_files) - set(not_latin)
    print('Кол-во файлов, название которых состоит только из латинских символов - ',len(set(files_latin)),'\n')

    print ('Папки:', set(folds),'\nФайлы:', set(files),'\n')
    return 0

def main():
    return files()
    

if __name__ == '__main__':
    main()
