#Return sin argumentos----

# def mi_funcion():
#     return "Hola mundo"

# print(mi_funcion())

# resultado= mi_funcion()

# print(resultado)

#función del factorial

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

#interacción entre funciones

def funcion_1():
    a=1
    return a

def funcion_2(a):
    b=2+a
    return b

def funcion_3(a,b):
    c=3+a+b
    return c

def funcion_4(a,b,c):
    d=4+a+b+c
    return d

print(funcion_4(funcion_1(), funcion_2(funcion_1()), funcion_3(funcion_1(), funcion_2(funcion_1()))))

f1=funcion_1()
f2=funcion_2(f1)
f3=funcion_3(f1, f2)
f4=funcion_4(f1, f2, f3)
print(f4)