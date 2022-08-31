def quickSort(secuence):
    length = len(secuence) #Se mide la longitud del arreglo
    if length <= 1:
        return secuence #Se evita repetir el algoritmo cuando la longitud es de 1 o menor
    else:
        pivot = secuence.pop() #Se escoje el último elemento como pivote
    items_grater = []
    items_lower = []
    for item in secuence:
        if item > pivot:
            items_grater.append(item) #elementos mayores al pivote
        else:
            items_lower.append(item) #elementos menores al pivote
    return quickSort(items_lower) + [pivot] + quickSort(items_grater)

numeros = [8,3,12,4,2,9,7,1]
print(quickSort(numeros))