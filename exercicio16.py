# Código para determinar a quantidade necessárias de latas de tintas

import math

def calcular_latas_tinta(area_metros_quadrados):
    litros_tinta_necessarios = area_metros_quadrados / 3
    latas_tinta_necessarias = math.ceil(litros_tinta_necessarios / 18)
    preco_total = latas_tinta_necessarias * 80

    return latas_tinta_necessarias, preco_total

def main():
    area_metros_quadrados = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

    latas_tinta, preco_total = calcular_latas_tinta(area_metros_quadrados)

    print(f"Quantidade de latas de tinta necessárias: {latas_tinta}")
    print(f"Preço total da compra: R$ {preco_total:.2f}")

if __name__ == "__main__":
    main()
