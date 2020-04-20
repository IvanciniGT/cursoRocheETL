
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicar(a,b):
    return a*b

operacion1=lambda a,b : a*b
print(operacion1(6,5))

resultado=suma(3,5)

print(resultado)

operacion=suma

print(operacion(6,7))

def calcula(operacion,a,b):
    return operacion(a,b)


print(calcula(suma,6,7))

print(calcula(resta,6,7))

print(calcula(lambda a,b:a/b ,42,7))

