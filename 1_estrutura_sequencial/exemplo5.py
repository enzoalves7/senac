valor_horas = float(input("Quanto voce ganha por hora? "))
horas_mes = float(input("Quantas horas voce trabalha por mes? "))

salario_bruto = valor_horas * horas_mes
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"Imposto de Renda (11%): R$ {imposto_renda}")
print(f"INSS (8%): R$ {inss}")
print(f"Sindicato (5%): R$ {sindicato}")
print(f"Salário Líquido: R$ {salario_liquido}")