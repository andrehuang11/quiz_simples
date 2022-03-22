#contagem de quantas respostas o usuário acertou
pontuação = 0
#contagem do número de vezes que a função "perguntas" foi chamada
contagem = 0

def perguntas(pergunta, resposta):
    #soma 1 na contagem cada vez que essa função é chamada na main
    global contagem
    contagem += 1
    #loop que continua até o usuário responder um número
    while True:
        try:
            RESPOSTA = int(input(pergunta))
        except ValueError:
            print("DIGITE UM NÚMERO INTEIRO!")
            continue
        else:
            break
    if RESPOSTA != resposta:
        print(f"Errou! A resposta correta é: {resposta}")
    else:
        print("Acertou!")
        #soma 1 na contagem da pontuação cada vez que o usuário acerta a resposta
        global pontuação
        pontuação += 1

def main():
    print("Bem vindo")
    #lista de todas as respostas possíveis
    sim = ["ss","s","sim"]
    nao = ["nn","n","não","nao","ñ"]
    sim_nao = sim + nao

    #loop que continua perguntando até a obter uma resposta válida
    while True:
        jogando = input("Quer jogar um quiz? ").lower()
        if jogando not in sim_nao:
            print("DIGITE UMA RESPOSTA VÁLIDA: SIM OU NÃO?")
        else:
            break
    #se a resposta for nao o programa fecha
    if jogando in nao:
        print("Ok, até mais!")
        return

    print("Ok, vamos começar!")
    
    #adicione aqui as perguntas para o quiz
    perguntas("Quanto é 1 + 1? ", 2)
    perguntas("Quanto é 2 + 2? ", 4)

    #se o número de respostas certas for igual ao número de perguntas, o programa vai considerar que o usuário acertou todas as perguntas
    if pontuação == contagem:
        print(f"Parabens vc acertou todas as {pontuação} questões ")
    #se o número de respostas certas for diferente do número de perguntas, o programa vai dizer ao usuário quantas perguntas ele acertou
    else:
        print(f"vc acertou um total de {pontuação} questão(ões)")

main()
#código para o cmd do windows não fechar instantaneamente após o fim do programa
input("Pressione enter para encerrar o programa. ")
        

