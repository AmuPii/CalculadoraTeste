print("""Bem vindo a calculadora,
        Vamos começar com dois numeros,
        ________________________________""")

input("Aperte enter para continuar")
print("________________________________")

def Numeros():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    return num1, num2

num1, num2 = Numeros()

print("""________________________________)
"   Agora vamos escolher a operação
     1 - Soma 
     2 - Subtração 
     3 - Multiplicação 
     4 - Divisão
    _____________________________________
      
      """)
selectedNum = input("Qual operação você deseja escolher? ")

if selectedNum not in ['1', '2', '3', '4']:
    print("Operação inválida. Por favor, escolha uma operação válida.")
    selectedNum = input("Qual operação você deseja escolher? ")

def resultado():
    if selectedNum == '1':
        return f"A soma de {num1} + {num2} é igual a {num1 + num2}"
    elif selectedNum == '2':
        return f"A subtração de {num1} - {num2} é igual a {num1 - num2}"
    elif selectedNum == '3':
        return f"A multiplicação de {num1} * {num2} é igual a {num1 * num2}"
    elif selectedNum == '4':
        if num2 != 0:
            return f"A divisão de {num1} / {num2} é igual a {num1 / num2}"
        else:
            return "Erro: Não é permitido fazer divisão por zero."
print("--------------------------------")
print(resultado())
print("--------------------------------")