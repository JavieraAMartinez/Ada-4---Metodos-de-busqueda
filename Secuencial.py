def busqueda_secuencial(lista, elemento):
  
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


mi_lista = [4, 2, 7, 1, 9, 5]
elemento_a_buscar = 7
resultado = busqueda_secuencial(mi_lista, elemento_a_buscar)
if resultado != -1:
    print(f"El elemento {elemento_a_buscar} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")

