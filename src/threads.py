import threading

# Função para calcular a soma de uma parte da lista
def soma_parcial(lista, inicio, fim, resultado, indice):
    soma = sum(lista[inicio:fim])  # Calcula a soma da sublista
    resultado[indice] = soma  # Armazena o resultado no índice correspondente

# Função principal
def soma_lista_com_threads(lista, num_threads):
    tamanho_lista = len(lista)
    parte = tamanho_lista // num_threads  # Encontra o tamanho de cada parte

    # Cria uma lista para armazenar os resultados das threads
    resultado = [0] * num_threads
    threads = []

    for i in range(num_threads):
        inicio = i * parte
        fim = (i + 1) * parte if i != num_threads - 1 else tamanho_lista  # Garante que a última parte vá até o final da lista
        thread = threading.Thread(target=soma_parcial, args=(lista, inicio, fim, resultado, i))
        threads.append(thread)
        thread.start()

    # Aguarda as threads terminarem
    for thread in threads:
        thread.join()

    # Retorna a soma total
    return sum(resultado)

# Exemplo de uso
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_threads = 2  # Número de threads desejado
    soma_total = soma_lista_com_threads(lista, num_threads)
    print(f"A soma total da lista é: {soma_total}")
