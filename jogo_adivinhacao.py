from random import randint 

num = randint(1,10)
tentativas = 0
user_input = None

while tentativas < 3:
    user_input = int(input("Tente adivinhar o número: "))
    tentativas += 1
    if user_input == num:
        print("[$]Parabéns, você acertou!")
        exit()
    else:
        if tentativas == 3:
            print("[!]Poxa, você perdeu!")
            break
        if user_input < num:
            print("[x]Errou, o número secreto é maior. -> você ainda possui", 3 - tentativas, "Tentativa(s).\n")
        else:
            print("[x]Errou, o número secreto é menor. -> você ainda possui", 3 - tentativas, "Tentativa(s).\n")
        

