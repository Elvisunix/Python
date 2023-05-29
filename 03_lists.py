### Lists ###

my_list = list()
my_other_list = []



my_list = ["35", "23", "20"]

print(my_list)
print (len(my_list))

my_other_list = [35, 1.17, "Python", "Java", "C++"]

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