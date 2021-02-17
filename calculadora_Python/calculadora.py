print('******************** Python Calculator ***********************')


print('\n')

print('Selecione o número da operação desejada')

print('\n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potência')

print('\n')


option = input('Digite sua opção (1/2/3/4/5): ')
print('\n')

valor1 = int(input('Digite o primeiro número: '))

valor2 = int(input('Digite o segundo número: '))

print('\n')

def soma(x, y):
    resultado = x+y
    print(x, '+', y, '=', resultado)

def subtracao(x,y):
    resultado = x-y
    print(x, '-', y, '=', resultado)

def multiplicacao(x,y):
    resultado = x*y
    print(x, '*', y, '=', resultado)

def divisao(x, y):
    if y == 0:
        print("Impossível divisão por 0")
    else:
        resultado = x/y
        print(x, '/', y, '=', resultado)

def potencia(x, y):
    resultado = x**y
    print(x, '**', y, '=', resultado)

if option == '1':
    soma(valor1, valor2)   
elif option == '2':
    subtracao(valor1, valor2)
elif option == '3':
    multiplicacao(valor1, valor2)
elif option == '4':
    divisao(valor1,valor2)
elif option == '5':
    potencia(valor1, valor2)
else:
    print('Opção Inválida')

print('\n')



