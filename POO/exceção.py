try: 
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))
    div = num1/num2
    print(div)

except ValueError as e:
    print("Error! Digite um numero valido!")
except ZeroDivisionError as e2:
    print("Error: Divisão por Zero!")
else:
    print("continua 1...")
finally:
    print("continua 2...")
