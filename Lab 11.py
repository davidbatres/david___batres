print ("Semana No. 11: Ejercicio 1")

n = int(input("Ingrese un nùmero mayor que 0: "))
if (n <= 0):
    print("Error, debe ser mayor a 0: ")

#declaración de variables
a = 0
b = 1 
c = 0
i = 2 
resultado = ""

if (n>0):
    resultado = str(a)

    if(n>1):
        resultado += ", " + str(b)
        print(resultado)
    while (i<n):
        c = a + b
        resultado += ", " + str(c)
        a = b
        b = c
        i = i + 1
    print ( resultado)
else:
    print(resultado) 

print("Semana No. 11 Ejercicio 2")

n2 = int(input("Ingrese un nùmero mayor que 0: "))

if (n<=0):
    print("Error: el número debe ser mayor que cero")
resultadoA = 0
for x in range (1, n2+1):
    resultadoA += (1/x)
    print("Inciso A ", resultadoA)

print("Semana No. 11 Ejercicio 3")

def calcular_sumatoria(x, a, n3):
    suma = 0
    for k in range(n3 + 1):
        suma += x**k * a**(n3 - k)
    return suma

def main():
    x = int(input("Ingrese el valor de x (número entero): "))
    a = int(input("Ingrese el valor de a (número entero): "))
    n3 = int(input("Ingrese el valor de n (número entero): "))
    
    resultadoC = calcular_sumatoria(x, a, n3)
    print("El resultado de la sumatoria es:", resultadoC)

if __name__ == "__main__":
    main()