with open("text.txt", encoding = "utf-8") as file:
    text = file.read()
    text = text.split('\n')
    
    lines = 0
    words = 0
    len_lines = []
    more_than_five = 0
    
    for line in text:
        line = line.split()
        lines += 1
        len_lines.append(len(line))
        
        if len(line) > 5:
            more_than_five += 1
        else:
            pass
        
        for word in line:
            word = word.strip('.,"!?/<>-')
            words += 1
            
            #print(word)
    #print(max(len_lines))
    #print(min(len_lines))
    #print(lines)
    #print(more_than_five)
    print("Среднее кол-во слов в строке: " + str(round(words//lines)))
    print("Самая короткая строка короче самой длинной в " + str(max(len_lines)//min(len_lines)) + " раз")
    print("Строки с числом слов больше 5: " + str(round(more_than_five / lines * 100)) + '%')
    
    

