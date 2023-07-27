# Código que calcula qual é o seu salário baseado no quanto voce ganha por hora e quantas horas você trabalha

valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))

salario_mes = valor_por_hora * horas_trabalhadas_mes

print(f"O total do seu salário no mês é: R$ {salario_mes:.2f}")