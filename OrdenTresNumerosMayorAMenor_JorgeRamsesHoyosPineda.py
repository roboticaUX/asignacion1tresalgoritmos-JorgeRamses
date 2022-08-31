#Recibir tres números y ordenarlos de mayor a menor, se debe validar que no existan números iguales.
print("Digite el primer numero: ")
num1 = input()
print("Digite el segundo numero: ")
num2 = input()
print("Digite el tercer numero: ")
num3 = input()
numeros = [num1, num2, num3]
#Revision de números repitidos
for i in range(len(numeros)):
    for j in range(i+1,len(numeros),1):
        if(numeros[i] == numeros[j]):
            print("Existen números iguales")
            exit()
#Ordenación del arreglo
for i in range(len(numeros)):
    for j in range(i+1,len(numeros),1):
        if(numeros[i] < numeros[j]):
            auxiliar = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = auxiliar
print("Números ordenados de mayor a menor: ")
print(*numeros)