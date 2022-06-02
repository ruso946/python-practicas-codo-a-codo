'''#1 Escribe un programa muestre por pantalla “Hello World”.'''
print("Hello Word")

'''#2 Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.'''
print("el resultado de 3 mas 5 es: ",3+5)

'''#3 Escribe un programa que pida el nombre del usuario y escriba un texto que
diga “Hola nombreUsuario”'''
nombre= input("Cual es el nombre del usuario?")
print("Hola ",nombre)

'''#4 Escribe un programa que pida un número, pida otro número y escriba el
resultado de sumar estos dos números.'''
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
print("el resultado de la suma es: ",num1+num2)

'''#5 Escribe un programa que pida dos números y escriba en la pantalla cual es el
mayor.'''
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
if num1 > num2:
    print(num1, " es el mayor ")
elif num2 > num1:    
    print(num2, " es el mayor ")

'''#6 Escribe un programa que pida 3 números y escriba en la pantalla el mayor de
los tres.'''
num=0
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese otro numero: "))
if num1 > num2:
    num=num1
else:
    num=num2

num3=int(input("ingrese otro numero mas: "))

if num3 > num:
    num=num3

print(num, " es el mayor ")

'''#7 Escribe un programa que pida un número y diga si es divisible por 2'''
num1=int(input("ingrese un numero: "))
if num1%2==0:
    print("es divisible por 2")
else:
    print("no es divisible por 2")

'''#8 Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o
7 (sólo hay que comprobar si lo es por uno de los cuatro)'''
num1=int(input("ingrese un numero: "))
div=2
if num1%div==0:
    print(f"es divisible por {div}")
else:
    div=3
    if num1%div==0:
        print(f"es divisible por {div}")
    else:
        div=5
        if num1%div==0:
            print(f"es divisible por {div}")
        else:
            div=7
            if num1%div==0:
                print(f"es divisible por {div}")

'''#9 Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay
que decir todos por los que es divisible)'''
num1=int(input("ingrese un numero: "))
div=2
if num1%div==0:
    print(f"es divisible por {div}")
div=3
if num1%div==0:
    print(f"es divisible por {div}")
div=5
if num1%div==0:
    print(f"es divisible por {div}")
div=7
if num1%div==0:
    print(f"es divisible por {div}")


'''#10 Escribir un programa que escriba en pantalla los divisores de un número dado'''
div=1
num1=int(input("ingrese un numero: "))
for div in range (1,num1):
    if num1%div==0:
        print(f"es divisible por {div}")

'''#11 Escribir un programa que nos diga si un número dado es primo (no es divisible
por ninguno otro número que no sea él mismo o la unidad)'''
div=1
cuenta=0
num1=int(input("ingrese un numero: "))
for div in range (1,num1+1):
    if num1%div==0:
        cuenta=cuenta+1
if cuenta==2 or num1==1:
    print("es un número primo")
else:
    print("no es un número primo")

'''#12 Pide una nota (número). Muestra la calificación según la nota:
 0-3: Muy deficiente
 3-5: Insuficiente
 5-6: Suficiente
 6-7: Bien
 7-9: Notable
 9-10: Sobresaliente'''

nota=float(input("ingrese una nota: "))
if nota>0 and nota<=3:
    print("Muy deficiente")
if nota>3 and nota<=5:
    print("Insuficiente")
if nota>5 and nota<=6:
    print("Suficiente")
if nota>6 and nota<=7:
    print("Bien")
if nota>7 and nota<=9:
    print("Notable")
if nota>9 and nota<=10:
    print("Sobresaliente")

'''#13 Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
forma:
1
22
333
4444
55555
666666'''

num=31
for i in range (num):
    cad=""
    for x in range (i):
        cad=cad+str(i)
    print (cad)
    print("")

'''
14 Haz un programa que escriba una pirámide inversa de los números del 1 al
número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666
55555
4444
333
22
1
'''

num=int(input("ingrese un numero para la piramide inversa: "))
for i in range (num,0,-1):
    cad=""
    for x in range (i):
        cad=cad+str(i)
    print (cad)
    print("")

'''
15  Crear un programa que escriba los números del 1 al 500, y que indique cuales
son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por
ejemplo:
'''
num=500
for i in range (1,num+1):
    cad = str(i)
    if i%4==0:
        cad = cad + " (múltiplo de 4)"
    if i%9==0:
        cad = cad + " (múltiplo de 9)"
    print (cad)
    if i%5==0:
        print("---------------------------------")