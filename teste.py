from collections import defaultdict
def verifica_palavra_repetida_retorna_index(lista):
    # Define o objeto que armazenará os índices de cada elemento:
    keys = defaultdict(list);
    # Percorre todos os elementos da lista:
    for key, value in enumerate(lista):
        # Adiciona o índice do valor na lista de índices:
        keys[value].append(key)
    # Exibe o resultado:
    lista_com_valores = [(value, keys[value]) for value in keys if len(keys[value]) >= 1]
    return lista_com_valores


lista = ['oi', 'tchau', 'expelliarmus', 'ola', 'hello', 'bye', 'tchau', 'ola', 'hello', 'bye', '']
lista_de_indices = verifica_palavra_repetida_retorna_index(lista)
print(lista_de_indices)
#resultado:  [('oi', [0]), ('tchau', [1, 6]), ('expelliarmus', [2]), 
#             ('ola', [3, 7]), ('hello', [4, 8]), ('bye', [5, 9]), ('', [10])]

#usando o indice(index):
print(lista[3], lista[7])
#resultado: ola ola
