### Lists ###

my_list = list()
my_other_list = []

print(my_list)

my_list = ["35", "23", "20"]

print(my_list)
print (len(my_list))

my_other_list = [35, 1.17, "Python", "Java", "C++"]

#Mostrar por pantalla el tipo de variable
print(type(my_other_list))
print (type(my_list))

#Mostrar por pantalla el primer elemento de la lista
print(my_other_list[-3])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[3])

#Esto es un error
#print(my_other_list[5])

#Mostrar por pantalla el ultimo elemento de la lista
print(my_other_list.count("Python"))

edad, altura, lenguaje, lenguaje2, lenguaje3 = my_other_list

print (edad)

#Sumar listas
print (my_other_list + my_list)

#Multiplicar listas
print (my_other_list * 2)

#añadir elementos a la lista
my_other_list.append("PHP")

#insterar elementos en una posicion concreta
my_other_list.insert(2, "Ruby")

#Eliminar elementos de la lista
my_other_list.remove("Ruby")

#Eliminar el ultimo elemento de la lista
pod_eliminado = my_other_list.pop()
print (pod_eliminado)

#Borrar un elemento de la lista
del my_other_list[0]
print(my_other_list)

#Cambiar un elemento de la lista
my_other_list[0] = 2.3
print(my_other_list)    

#Copiar una lista
my_new_list = my_other_list.copy()
print (my_new_list)

#Ordenar una lista al reves
my_other_list.reverse()
print(my_other_list)

#Ordenar una lista
my_other_list.sort()
print(my_other_list)