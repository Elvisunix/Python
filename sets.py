##sets

my_set = set()
my_other_set = {}
print(type(my_set))

print(type(my_other_set))

my_other_set = {"Juanjo", "Jumilla", 35, "Python"}
print(type(my_other_set))

print(len(my_other_set))

#Añadir elementos
my_other_set.add("Paco")
print(my_other_set)

my_other_set.add("Juanjo")
print(my_other_set)

#Comprobar si un elemento esta en el set
print ("Paco" in my_other_set)
print ("Maria" in my_other_set)

#Eliminar elementos
my_other_set.remove("Paco")
print(my_other_set)

#vaciar el set
my_other_set.clear()
print(len(my_other_set))

#Eliminar el set
del my_other_set

my_set = {"Juanjo", "Jumilla", 35, "Python"}
my_list = list(my_set)

print (type(my_list))
print (my_list)
print (my_list[2])