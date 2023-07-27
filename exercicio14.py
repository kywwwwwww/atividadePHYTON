# Código para calcular uma multa caso o peso passe do peso permitido

peso_limite = 50
peso_peixes = float(input("Digite o peso de peixes trazidos por João (em quilos): "))

if peso_peixes <= peso_limite:
        print("João não excedeu o limite de peso, nenhuma multa é devida.")
else:
        excesso = peso_peixes - peso_limite
        valor_multa_por_quilo = 4.00
        multa = excesso * valor_multa_por_quilo

        print(f"João excedeu o limite de peso em {excesso:.2f} quilos.")
        print(f"A multa devida por excesso de peso é de R$ {multa:.2f}.")