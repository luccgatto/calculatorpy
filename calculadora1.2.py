import math
import string 


print('\033[0;35;40m██╗░░██╗░█████╗░░█████╗░░█████╗░  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░')
print('\033[0;35;40m╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
print('\033[0;35;40m░╚███╔╝░███████║██║░░██║██║░░╚═╝  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝')
print('\033[0;35;40m░██╔██╗░██╔══██║██║░░██║██║░░██╗  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗')
print('\033[0:35;40m██╔╝╚██╗██║░░██║╚█████╔╝╚█████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
print('\033[0;35;40m╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝')


print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
print('\033[0;35;40mBem vindo à calculadora do Xaoc. Digite o que deseja fazer na calculadora, de acordo com a tabela abaixo.')
print('\033[;33;40m[1] Para dividir.\n[2] Para somar.\n[3] Para subtrair.\n[4] Para multiplicar.')
print('\033[;33;40m[5] Para raiz quadrada.\n[6] Para calcular se é possível formar um triângulo.')
print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')

resp = str(input('\033[;33;40mDigite aqui o que deseja fazer na calculadora: '))
resp2 = resp.capitalize()
print(f'\033[mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ ㅤㅤㅤㅤ')


if resp2 == '1':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    div = num1 / num2
    resposta = div
    respfinal = resp2

elif resp2 == '2':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    som = num1 + num2
    resposta = som
    respfinal = resp2

elif resp2 == '3':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    sub = num1 - num2
    resposta = sub
    respfinal = resp2

elif resp2 == '4':
    num1 = float(input('\033[;33;40mAgora digite qual o primeiro número de sua operação: '))
    num2 = float(input('\033[;33;40mAgora digite qual o segundo número de sua operação: '))
    mult = num1 * num2
    resposta = mult
    respfinal = resp2

elif resp2 == '5':
    num1 = float(input('\033[;33;40mDigite aqui o número o qual você gostaria de saber a raiz: '))
    raiz = math.sqrt(num1)
    resposta = raiz
    respfinal = resp2

if resp2 == '1':
    print(f'\033[1;31;40mO resultado de sua operação é {resposta:.1f}!')
elif resp2 == '2':
    print(f'\033[1;31;40mO resultado de sua operação é {resposta:.1f}!')
elif resp2 == '3':
    print(f'\033[1;31;40mO resultado de sua operação é {resposta:.1f}!')
elif resp2 == '4':
    print(f'\033[1;31;40mO resultado de sua operação é {resposta:.1f}!')
elif resp2 == '5':
    print(f'\033[1;31;40mO resultado de sua operação é {resposta:.1f}!')
elif resp2 == '6':
    num1 = float(input('\033[;33;40mDigite o primeiro número do triângulo: '))
    num2 = float(input('\033[;33;40mDigite o segundo número do triângulo: '))
    num3 = float(input('\033[;33;40mDigite o terceiro número do triângulo: '))
    respfinal = resp2
    if num1<=0 or num2<=0 or num3<=0:
            trianum = "Triângulo inexistente!"
            print(trianum)
    elif num1>=num2+num3 and num3<=num2+num1 and num2<=num3+num1: 
            triandois = "Triângulo inexistente!"
            print(triandois)
    elif num1==num2 and num2==num3:
            triantres = "Triângulo equilátero!"
            print(triantres)
    elif num1==num2 or num2==num3 or num3==num1:
            trianquatro = "Triângulo isósceles!"
            print(trianquatro)
    else:
            triancinco = "Triângulo escaleno!"
            print(triancinco)
else:
    print(f'\033[1;37;41mERRO: Você não escolheu nenhum operador ou digitou um comando errado!')

print(f'\033[0;37;40mㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
print('\033[0;37;40mㅤ█████████████████████')
print('\033[0;37;40mㅤ█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█')
print('\033[0;37;40mㅤ██─▄█▀██─█▄▀─███─██─█')
print('\033[0;37;40mㅤ▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀')