##tuples

my_tuple = tuple()
my_other_tuple = (34,33,60,40)

my_tuple = ("Juanjo", "Jumilla", 35, "Python", "Python")  
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[-2])

print(my_tuple.count("Juanjo"))
print(my_tuple.index("Juanjo"))

#Esto es un error
#my_tuple[1] = "1.80"

#Sumar tuplas
print (my_tuple + my_other_tuple)

print(my_other_tuple[1:3])

my_other_tuple = list(my_other_tuple)
print(type(my_other_tuple))

del my_other_tuple
#Esto es un error
print(my_other_tuple)