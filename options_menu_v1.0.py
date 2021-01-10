from time import sleep
print('\n\t\033[33mCRIANDO MENUS DE OPÇÕES\n')

# menu do programa
    # pegando informações e declarando o que precisar
num1 = int(input('\033[36mPrimeiro Número: \033[37m'))
num2 = int(input('\033[36mSegundo Número: \033[37m'))
menu = 0
        # mostrando graficamente o menu
while menu != 5:
    sleep(2)
    print('\n\tMENU DE OPÇÕES', end='')
    desing = '=-=' * 13 + '\033[m'
    print('\n\033[33m' + desing)
    print('''\t\033[36m[1]\033[31m Somar
    \t\033[36m[2]\033[32m Multiplicar
    \t\033[36m[3]\033[33m Maior
    \t\033[36m[4]\033[34m Novos Números
    \t\033[36m[5]\033[35m Sair do Programa''')
    print('\033[33m' + desing)
        # fim do menu
    # escolha do menu
    menu = int(input('\033[33mEscolha uma opção:\033[37m '))
    # escolheu errado
    while menu not in [1, 2, 3, 4, 5]:
        print('\n\033[31mOçpão Inválida, tente novamente')
        menu = int(input('\033[33mEscolha uma opção:\033[37m  '))
    # escolheu errado fim
    # escolha 1 
    if menu == 1:
        soma = num1 + num2 
        print('\n\033[36mA soma dos números \033[31m{} \033[36me \033[31m{} \033[36mé \033[31m{}'.format(num1, num2, soma))
    # escolha 2
    elif menu == 2:
        mult = num1 * num2
        print('\n\033[36mA multiplicação dos números \033[32m{} \033[36me \033[32m{} \033[36mé \033[32m{}'.format(num1, num2, mult))
    # escolha 3
    elif menu == 3:
        if num1 > num2:
            print('\n\033[36mO maior número é {}.'.format(num1))
        else:
            print('\n\033[36mO maior número é \033[33m{}'.format(num2))
    # escolha 4
    elif menu == 4:
        print('\n\033[34mEscreva novamente os números...')
        num1 = int(input('\033[36mPrimeiro Número: \033[37m'))
        num2 = int(input('\033[36mSegundo Número: \033[37m'))
    else:
        sleep(1)
        print('\nFechando o Programa...\n')
        sleep(3)
        print('Fim\n')