def busqueda_binaria(lista, elemento):
  
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

mi_lista = [1, 2, 4, 5, 7, 9]
elemento_a_buscar = 7
resultado = busqueda_binaria(mi_lista, elemento_a_buscar)
if resultado != -1:
    print(f"El elemento {elemento_a_buscar} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")

