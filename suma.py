def suma(l):
    #suma un conjunto de valores de una lista.
    suma = 0
    for num in  l:
        suma += num
    
    return suma

num = [1,2,3,4,5]
print(suma(num))