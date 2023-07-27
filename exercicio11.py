# Código que calcula o produto do dobro do primeiro numero com metade do segundo numero, a soma do triplo do primeiro numero com o terceiro numero e o terceiro numero elevado ao cubo

num_inteiro1 = int(input("Digite o primeiro número inteiro: "))
num_inteiro2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

produto = (2 * num_inteiro1) * (num_inteiro2 / 2)
soma = (3 * num_inteiro1) + num_real
cubo = num_real ** 3

print(f"Produto do dobro do primeiro com metade do segundo: {produto}")
print(f"Soma do triplo do primeiro com o terceiro: {soma}")
print(f"O terceiro elevado ao cubo: {cubo:.2f}")