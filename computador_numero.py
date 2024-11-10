def advinhar_numero ():

    print ('Pense um número entre 1 a 100 e o computador tentará advinhar.')

    print ('Para que o computador acerte o seu palpite, dê feedback de menor, maior ou correto para cada tentativa.')

    inicio = 1
    fim = 100
    tentativas = 0

    while True:
        palpite = (inicio + fim) // 2
        tentativas += 1
        print (f'Meu palpite é: {palpite}')

        feedback = input ('Dê um feedback sobre meu palpite: ')

        if feedback == 'correto':
            print ('Parabéns, você acertou!')
            break
        elif feedback == 'maior':
            inicio = palpite + 1
        elif feedback == 'menor':
            fim = palpite -1

advinhar_numero ()
        
