# Código para determinara quantidade de latas de tinta dependendo do tamanho dela 

import math

def calcular_quantidade_tinta(area_metros_quadrados):
    litros_tinta_necessarios = area_metros_quadrados / 6
    latas_18_litros = math.ceil(litros_tinta_necessarios / 18)
    galoes_3_6_litros = math.ceil(litros_tinta_necessarios / 3.6)
    mistura_latas_galoes = math.ceil(litros_tinta_necessarios / 18)
    resto = mistura_latas_galoes % 18

    if resto > 0:
        latas_18_litros = mistura_latas_galoes // 18
        galoes_3_6_litros = math.ceil(resto / 3.6)
    else:
        latas_18_litros = mistura_latas_galoes // 18
        galoes_3_6_litros = 0

    return latas_18_litros, galoes_3_6_litros

def calcular_preco_total(latas_18_litros, galoes_3_6_litros):
    preco_lata_18_litros = 80
    preco_galao_3_6_litros = 25

    preco_total_latas = latas_18_litros * preco_lata_18_litros
    preco_total_galoes = galoes_3_6_litros * preco_galao_3_6_litros

    return preco_total_latas, preco_total_galoes

def main():
    area_metros_quadrados = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

    latas_18_litros, galoes_3_6_litros = calcular_quantidade_tinta(area_metros_quadrados)
    preco_total_latas, preco_total_galoes = calcular_preco_total(latas_18_litros, galoes_3_6_litros)

    print(f"Situação 1 - Comprar apenas latas de 18 litros:")
    print(f"Quantidade de latas: {latas_18_litros}")
    print(f"Preço total: R$ {preco_total_latas:.2f}\n")

    print(f"Situação 2 - Comprar apenas galões de 3,6 litros:")
    print(f"Quantidade de galões: {galoes_3_6_litros}")
    print(f"Preço total: R$ {preco_total_galoes:.2f}\n")

    print(f"Situação 3 - Misturar latas e galões:")
    print(f"Quantidade de latas: {latas_18_litros}")
    print(f"Quantidade de galões: {galoes_3_6_litros}")
    preco_total_mistura = preco_total_latas + preco_total_galoes
    print(f"Preço total: R$ {preco_total_mistura:.2f}")

if __name__ == "__main__":
    main()
