#Funcion
from math import factorial


def facotiral(num):
    if(num < 0):
        print("Error :(")
        exit()
    elif(num == 0):
        return 1
    else:
        return num*factorial(num-1)

print("Digite un número: ")
numero = input()
print("El facotorial del numero es:")
print(facotiral(int(numero)))