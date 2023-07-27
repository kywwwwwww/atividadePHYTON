# Código para calcular o peso ideal para uma pessoa baseado em sua altura (tanto para homem quanto para mulher)

def calcular_peso_ideal(altura, genero):
    if genero.lower() == 'homem':
        peso_ideal = (72.7 * altura) - 58
    elif genero.lower() == 'mulher':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Gênero inválido. Use 'homem' ou 'mulher'.")

    return peso_ideal

def main():
    altura = float(input("Digite a altura da pessoa (em metros): "))
    genero = input("Digite o gênero da pessoa (homem ou mulher): ")

    try:
        peso_ideal = calcular_peso_ideal(altura, genero)
        print(f"O peso ideal para a altura {altura:.2f} metros e gênero {genero} é: {peso_ideal:.2f} kg")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
