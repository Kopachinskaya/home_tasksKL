while True:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье чтисло: "))

    if a + b == c:
        print("Ничего себе! " + str(a) +" + " + str(b) +" = "+ str(c) + "!")
    
    elif a * b == c:
        print("Ничего себе! Если " + str(a) +" умножить на " + str(b) +" получится "+ str(c) + "!")

    elif a / b ==c:
        print("Ничего себе! Если " + str(a) +" : " + str(b) +" = "+ str(c) + "!")
        
    elif a // b ==c:
        print("Ничего себе! Если " + str(a) +" поделить на " + str(b) +" в остатке получится "+ str(c) + "!")

    else:
        print("These are just some nice numbers!")
            

        
        
    
