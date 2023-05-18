
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

otros = []

# obtener los nombres que se encuentran en la lista de nombres pero no en magos ni cientificos
for i in nombres:
    if i in magos or i in cientificos:
        continue
    otros.append(i)
# añadir "El Gran" a los nombres que se encuentran en la lista de magos
def hacer_grandioso(magos):
    nuevo_mago = []
    for i in magos:
        a = "El gran " + i
        nuevo_mago.append(a)
    return nuevo_mago
# imprime todos los nombres de la lista nombre 
def imprimir_nombres(nombres):
    new_list = []
    for i in range(len(nombres)):
        new_list.append(nombres[i])
    return new_list
    
# imprime por categoria los nombres
def categoria_nombres(magos, cientificos, otros):
    a = "Magos: " + str(magos) + "\n"
    b = "Cientificos: " + str(cientificos) + "\n"
    c = "Otros: " + str(otros) 
    return a + b + c
    

categorias = categoria_nombres(magos, cientificos, otros)
nueva_lista = imprimir_nombres(nombres)
mago_modificados = hacer_grandioso(magos)

print(nueva_lista)
print(categorias)
print(mago_modificados)

