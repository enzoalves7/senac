def division(n1, n2):
    if(n2 == 0):
        raise ZeroDivisionError
    else: 
        return n1/n2
try:    
    resultado = division(int(input("Valor 1: ")), int(input("Valor 2: ")))
    print(f"Resultado da Divisão: {resultado}")
except ZeroDivisionError as e:
    print(e)