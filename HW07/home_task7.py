
import random

def noun():
    with open ('nouns.txt', 'r', encoding = 'utf-8') as file:
        nouns = file.read().split()
        clean_nouns = []
        for noun in nouns:
            noun = noun.strip('.,"!?/<>-')
            clean_nouns.append(noun)
        
    return random.choice(clean_nouns)

def adj(word):
    with open ('adj.txt', 'r', encoding = 'utf-8') as file:
        adj = file.read().split()
        clean_adj = []
        for x in adj:
            x = x.strip('.,"!?/<>-')
            clean_adj.append(x)

        random_adj = random.choice(clean_adj)
        n = noun()
        cons = 'БВГДЖЗКЛМНПРСТФХЦЧШЩ'
        vow = 'АИУЫЭЬ'
        
        if list(n)[-1] in cons.lower():
            result = random_adj
        elif list(n)[-1] in vow.lower():

            result = ''.join(list(random_adj)[:-2]) + 'ая'
        else:
            result = ''.join(list(random_adj)[:-2]) + 'ое'
            
    return result + ' ' + str(n)

def verb(subj):

    with open ('verbs.txt', 'r', encoding = 'utf-8') as file:
        verb = file.read().split()
        clean_verbs = []
        for x in verb:
            x = x.strip('.,"!?/<>-')
            clean_verbs.append(x)
        
        random_verb = random.choice(clean_verbs)
        f = open('irr_verbs.txt', 'r', encoding = 'utf-8')
        irr_verbs = f.read().split()
        if list(random_verb)[-3] == 'и':
            result = ''.join(list(random_verb)[:-3]) + 'ит'
        elif random_verb in irr_verbs:
            result = ''.join(list(random_verb)[:-3]) + 'ит'
        else:
            result = ''.join(list(random_verb)[:-2]) + 'ет'
        f.close()
    return result

def imper_verb(subj):
    if list(subj)[-3] == 'а' or list(subj)[-3] == 'я' or list(subj)[-3] == 'о':
        result = ''.join(list(subj)[:-2]) + 'й'
    else:
        list(subj)[-2] == 'и' or list(subj)[-2] == 'е'
        result = ''.join(list(subj)[:-2]) + 'и'
    
    return result

def adv():
    with open ('adv.txt', 'r', encoding = 'utf-8') as file:
        adv = file.read().split()
        clean_adv = []
        for x in adv:
            x = x.strip('.,"!?/<>-')
            clean_adv.append(x)
        return random.choice(clean_adv)
    
        
def random_statement():
    sentence = adj(noun()).capitalize() + ' ' + verb(noun())+ ' ' + adv()+ '.'
    return sentence

def random_not_sent():
    sentence = adj(noun()).capitalize() + ' '  + 'не' + ' ' + verb(noun())+ ' ' + adv()+ '.'
    return sentence

def random_intr_sent():
    sentence = verb(noun()).capitalize()+ ' ' + 'ли' + ' ' + adj(noun()) + '?'
    return sentence

def random_if_sent():
    sentence = 'Если' + ' ' + adj(noun()) + ' ' + verb(noun())+ ' ' + adv()+ ','+\
               ' ' + 'то' + ' ' + adj(noun()) + ' ' + verb(noun())+ ' ' +\
               adv()+ '.'
    return sentence

def imper_sent():
    sentence = imper_verb(verb(noun())).capitalize() + ' ' + adv()+ "!"
    return sentence

def random_sentence():
    sents = [random_statement(),random_not_sent(),random_intr_sent(),random_if_sent(),imper_sent()]
    random.shuffle(sents)
    for sent in sents:
        print(sent)
    return 0

def main():
    return random_sentence()

if __name__ == '__main__':
    main()
    
