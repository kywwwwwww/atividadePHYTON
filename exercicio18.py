# Código que informa o tempo de download de um arquivo em MB e determinando tambem a velocidade de link a internet

def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
    tamanho_arquivo_bits = tamanho_arquivo_mb * 8 * 1024 * 1024
    tempo_segundos = tamanho_arquivo_bits / (velocidade_internet_mbps * 1024 * 1024)
    tempo_minutos = tempo_segundos / 60

    return tempo_minutos

def main():
    tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
    velocidade_internet_mbps = float(input("Digite a velocidade do link de internet (em Mbps): "))

    tempo_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)

    print(f"O tempo aproximado de download será de {tempo_minutos:.2f} minutos.")

if __name__ == "__main__":
    main()
