from random import randint 
num = randint(1,10)
tentativas = None
user_input = None
dif = int(input("\nDigite a dificuldade:\n[1]Fácil : 8 tentativas\n[2]Médio : 5 tentativas\n[3]Difícil : 3 tentativas\n\n"))

if dif == 1:
    tentativas = 8
elif dif == 2:
    tentativas = 5
else:
    tentativas = 3

for i in range(tentativas):
    user_input = int(input("Pense em um número: "))
    if  user_input == num:
        print("[!]Vocẽ acertou! em ", i + 1, " tentativas!")
        break
    else:
        if user_input < num:
            print("[x]Voce errou, o número secreto é maior! Tente novamente!\n[!]Tentativas restantes:", tentativas -1 - i, "\n")
        else:
            print("[x]Voce errou, o número secreto é menor! Tente novamente!\n[!]Tentativas restantes:", tentativas -1 - i, "\n")
