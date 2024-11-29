a="Hola"
b=input("Lleguir paraula: ")
# Mostri caracters de la paraula lleguida 
for e in b:
    print(e)
#longitud paraula 
print(len(b))

#Comparar-les
if a == b:
    print("{} i {} son iguals ".format(a, b))
else:
    print("{} i {} son diferents ".format(a, b))

#Ajuntar-les amb un guio
print(a+"-"+b)

#Repetir-la 3 vegades 
print(b*3)

#Mirar si la vocal a es dins b(string)
if "a" in b:
    print("a es dins l'string {}".format(b))
else:
    print("a no hi es dins")