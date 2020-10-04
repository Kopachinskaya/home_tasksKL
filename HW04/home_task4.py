arr = []
while True:
    word = input("Введите слолво: ")
    if not word:
        break
    arr.append(word.strip(' '))
for word in arr:
    i = arr.index(word)
    i+=1
    letters = []
    for letter in word:
        letters.append(letter)
        new_word = ''.join(letters[i:])
        
    print(new_word)
    
