print("Escolha um número:")
n1 = float(input())
print("Escolha outro número:")
n2 = float(input())
print("Escolha uma operação matemática: +, -, * ou /")
operacao = input()


def calculadora (n1,n2,operacao):
  if (operacao == "+"): 
    return (n1 + n2)
  elif (operacao == "-"):
    return (n1 - n2)
  elif (operacao == "*"):
    return (n1 * n2)
  elif (operacao == "/"):
    return (n1 / n2)
  else:
    return 0 

resultado = calculadora(n1, n2, operacao)
print("O resultado da operação é:", resultado)