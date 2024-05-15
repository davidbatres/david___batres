print("Ejercicio 1")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

divisionReal = n1 / n2
divEntera = n1 // n2
divModular = n1 % n2 
suma = n1 + n2 
resta = n1 - n2
multiplicacion = n1 *n2 

print (n1,"+", "=", suma)
print (n1,"-", "=", resta)
print (n1,"*", "=", multiplicacion)
print (n1,"/",n2,"=", divisionReal)
print (n1,"//",n2,"=", divEntera)
print (n1,"%",n2,"=", divModular)

print("ejercicio 2: operaciones booleanas")

igualdad = n1 == n2
diferentes = n1 != n2
mayor= n1 > n2 
menor= n1 < n2 
print(n1, "==", n2, "=", igualdad)
print(n1, "!=", n2, "=", diferentes)
print(n1, ">", n2, "=", mayor )
print(n1, "<", n2, "=", menor )

print("ejercicio 3: jerarquia de operadores ")
a = int(input("ingrese el primer numero "))
b = int(input("ingrese el segundo numero "))
c = int(input("ingrese el tercero numero "))

print( "i.", a*b+c)
print("ii.", a*(b+c))
print("iii.", a/(b+c))
print("iv.", (3*a+2*b)/(c**2))

print("Actividad 3, ejercicio 1")
metros1= int(input("ingrese metros"))

km = metros1 / 1000
mill = km/1.609
ft = metros1*3.28
pul = ft*12 

print("km:", km )
print("millas:", mill )
print("pies:", ft )
print("pulgadas:", pul )

print("actividad 3, ejercicio 2")

metros2 = int(intput("ingrese metros: "))
yardas= metros2 // 0.9144
mody= metros2  % 0.9144
pies = mody // 0.333333
pul= m2 * 39.37

print = ("yardas;, y, "pies: "pies, pul", pul)




