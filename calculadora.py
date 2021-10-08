import math 


print('\033[0;35;40m██╗░░██╗░█████╗░░█████╗░░█████╗░  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░')
print('\033[0;35;40m╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
print('\033[0;35;40m░╚███╔╝░███████║██║░░██║██║░░╚═╝  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝')
print('\033[0;35;40m░██╔██╗░██╔══██║██║░░██║██║░░██╗  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗')
print('\033[0:35;40m██╔╝╚██╗██║░░██║╚█████╔╝╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
print('\033[0;35;40m╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝')


print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
print('\033[0;35;40mBem vindo à calculadora do Xaoc. Digite o que deseja fazer na calculadora, de acordo com a tabela abaixo.')
print('\033[;33;40mDivisão = Para dividir.\nSoma = Para somar.\nSubtrair = Para subtrair.\nMultiplicação = Para multiplicar.')
print('\033[;33;40mRaiz = Para raiz quadrada.')
print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')

resp = str(input('\033[;33;40mDigite aqui o que deseja fazer na calculadora: '))
resp2 = resp.capitalize()
print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤㅤㅤㅤ')


if resp2 == 'Divisão':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    div = num1 / num2
    resposta = div

elif resp2 == 'Soma':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    som = num1 + num2
    resposta = som

elif resp2 == 'Subtrair':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    sub = num1 - num2
    resposta = sub

elif resp2 == 'Multiplicação':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    mult = num1 * num2
    resposta = mult

elif resp2 == 'Raiz':
    num1 = float(input('\033[;33;40mDigite aqui o número o qual você gostaria de saber a raiz: '))
    raiz = math.sqrt(num1)
    resposta = raiz

else:
    print(f'\033[1;37;41mERRO: Você não escolheu nenhum operador ou digitou um comando errado!')

print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤㅤㅤㅤ')
print(f'\033[1;31;40mO resultado de sua operação é {resposta:.1f}!')

print(f'\033[0;37;40mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
print('\033[0;37;40mㅤ█████████████████████')
print('\033[0;37;40mㅤ█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█')
print('\033[0;37;40mㅤ██─▄█▀██─█▄▀─███─██─█')
print('\033[0;37;40mㅤ▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀')
