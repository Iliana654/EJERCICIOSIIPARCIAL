#Return sin argumentos----

# def mi_funcion():
#     return "Hola mundo"

# print(mi_funcion())

# resultado= mi_funcion()

# print(resultado)

#función del factorial---

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         #Factorial ciclo for
#         resultado=1
#         for i in range(1, n+1):
#             resultado*=1
#             return resultado
        
# n=print(int(input("Ingrese el número para calcular el factorial:")))
# print(factorial(n))

#interacción entre funciones----

# def funcion_1():
#     a=1
#     return a

# def funcion_2(a):
#     b=2+a
#     return b

# def funcion_3(a,b):
#     c=3+a+b
#     return c

# def funcion_4(a,b,c):
#     d=4+a+b+c
#     return d

# print(funcion_4(funcion_1(), funcion_2(funcion_1()), funcion_3(funcion_1(), funcion_2(funcion_1()))))

# f1=funcion_1()
# f2=funcion_2(f1)
# f3=funcion_3(f1, f2)
# f4=funcion_4(f1, f2, f3)
# print(f4)

# #Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio.

def compara_numero(a, b,c):
    suma=a+b+c
    if suma>15:
        resultado= max(a, b, c)
    elif suma<10:
        resultado=min(a,b,c)
    else:
        resultado=a+b+c-max(a,b,c)-min(a,b,c)
    return resultado
print(compara_numero(8,2,3))

#ORDENA VALORES DE MAYOR A MENOR------
