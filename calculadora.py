from math import sqrt, pi, pow
print("Bem vindo a calculadora.")

def operacoes():
    try:
        print('Opções: \n-Adição \n-Subtração\n-Multiplicação \n-Divisão\n-Potenciação\n-Raiz Quadrada')
        operacao = input('Digite a operação que voce quer realizar: ').lower().strip()
        if operacao in ["soma", 'adicao', 'adição']:
            a = float(input("Digite o primeiro número da operação: "))
            b = float(input("Digite o segundo número da operação: "))
            print(f"{a:.2f} + {b:.2f} = {a+b:.2f}")
        elif operacao in ['subtracao', 'subtração']:
            a = float(input("Digite o primeiro número da operação: "))
            b = float(input("Digite o segundo número da operação: "))
            print(f"{a:.2f} - {b:.2f} = {a-b:.2f}")
        elif operacao in ['multiplicacao', 'multiplicação']:
            a = float(input("Digite o primeiro número da operação: "))
            b = float(input("Digite o segundo número da operação: "))
            print(f"{a:.2f} x {b:.2f} = {a*b:.2f}")
        elif operacao in ['divisao', 'divisão']:
            if (b != 0):
                a = float(input("Digite o primeiro número da operação: "))
                b = float(input("Digite o segundo número da operação: "))
                print(f"{a:.2f} / {b:.2f} = {a/b:.2f}")
            else:
                print("Esta divisão não é possível.")
        elif operacao in ['potenciacao','potenciação']:
            a = float(input("Digite a base da operação: "))
            b = float(input("Digite a potencia: "))
            print(f"{a:.2f} ^ {b:.2f} = {pow(a,b):.2f}")
        elif operacao in ['raiz','raíz', 'raiz quadrada', 'raíz quadrada']:
            a = float(input("Digite o número da operação: "))
            print(f"√{a:.2f} = {sqrt(a):.4f}")
        else:
            print("Escolha uma forma de operação válida.")
    except ValueError:
        print('Números inválidos.')

def bhaskara():
   try:
        a = float(input("Digite o valor do coeficiente A: "))
        if a == 0:
            print('Não existem raízes reais.') 
        else:       
            b = float(input("Digite o valor do coeficiente B: "))
            c = float(input("Digite o valor do coeficiente C: "))
            d = (pow(b,2))-(4*a*c)
            r_1 = -b + (sqrt(d))/(2*a)
            r_2 = -b - (sqrt(d))/(2*a)
            if d != 0:
                if d > 0:
                    print(f"Há duas raízes reais diferentes. Elas são {r_1:.2f} e {r_2:.2f}.")
                else:
                    print("Não existem raízes reais.")  
            else:
                print(f"As duas raízes deste número são iguais. Ela é {r_1:.2f}.")
   except ValueError:
      print('Coeficiente(s) inválido(s).')

def area():
    try:
        d = float(input('Digite o diametro do circulo em centímetros: '))
        a = pow(d/2, 2)*pi
        print(f'A área deste círculo é {a:.2f}cm.')
    except ValueError:
        print('Isto não é um número.')

while True:
    conta = input('Opções: \n-Operação básica \n-Bhaskara\n-Área do círculo \n-Sair\nDigite a opção desejada: ').lower().strip()
    if conta in ['operacao', 'operacao basica', 'operação básica', 'operação','operacao básica', 'operaçao basica', 'operacão basica']:
        operacoes()
    elif conta in ['formula de bhaskara', 'fórmula de bhaskara', 'bhaskara']:
        bhaskara()
    elif conta in ['area do circulo','área do círculo', 'area', 'área']:
        area()
    elif conta in ['sair']:
        break
    else:
        print('Opção inválida.')
