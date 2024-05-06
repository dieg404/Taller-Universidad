lista_n = []
lista_e = []
lista_es = []
lista_na = []


posicion_e = []
posicion_n = []


x = int(input("Ingrese cuantos usuarios va a registrar: "))

for i in range(x):
    n = input("Ingrese su nombre: ")
    e = int(input("Ingrese su edad: "))
    es = int(input("Ingrese su estrato: "))
    na = input("Ingrese su nivel academico: ")
    print("-" * 20)

    if e <= 4 or e >= 40:
        print("Error")
        break
    elif e >= 5 and e <= 40:
        lista_n.append(n)
        lista_e.append(e)
        lista_es.append(es)
        lista_na.append(na)
    else:
        print("No debe salir")
    

for i in lista_e:


    if i >= 5 and i <= 10:
        p1 = lista_n.index(i)
        p2 = lista_e.index(i)
        p1.append(posicion_n)
        p2.append(posicion_e)
    elif i > 10 and i <= 20:
        p1 = lista_n.index(i)
        p2 = lista_e.index(i)
        p1.append(posicion_n)
        p2.append(posicion_e)
    elif i > 20 and i <= 30:
        p1 = lista_n.index(i)
        p2 = lista_e.index(i)
        p1.append(posicion_n)
        p2.append(posicion_e)
    elif i > 30 and i < 40:
        p1 = lista_n.index(i)
        p2 = lista_e.index(i)
        p1.append(posicion_n)
        p2.append(posicion_e)
    else:
        print("Chao")

print(posicion_n)
print(posicion_e)




