import re

def get_capital():
    with open('Соединённые Штаты Америки — Википедия.html', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
        card = []
        for line in text:
            if re.search('(<span)\s(([a-z])+(-))+(id="P36")', line):
                card.append(line)
        for word in card:
            res = re.search('(")([а-яА-Я]+)(")', word)
            if res:
                return 'Столица государства - ' + res.group(2)


def get_time_zone():
    with open('Москва — Википедия.html', 'r', encoding = 'utf-8') as f:
        text = f.readlines()
        card = []
        for line in text:
            if re.search('(<span)\s(([a-z])+(-))+(id="P421")', line):
                card.append(line)
        for word in card:
            res = re.search('(\")(([A-Z])+(\+)([0-9])(\:)([0-9])+)(\")', word)
            if res:
                return 'Часовой пояс: ' + res.group(2)



with open('Высшая школа экономики — Википедия.html', 'r', encoding = 'utf-8') as f:
    text = f.readlines()
        
def get_indx(text):
        for i, line in enumerate(text):
            if re.search('<th.+>П[а-я]+ли<.+',str(line)):
                i += 0
                return i

def get_lecturers(get_index):
    for indx, line in enumerate(text):
        if str(get_indx(text)+2) in str(indx):
            my_line = line
            res = re.search('(^[0-9]+)', my_line)
            if res:
                return 'Количество преподавателей в вузе ' + res.group(1)

    

info = get_capital() + '\n' + get_time_zone() + '\n' + get_lecturers(get_indx(text))

f = open('info.txt', 'w')
f.write(info)
f.close()






