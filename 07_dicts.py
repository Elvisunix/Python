 ##dictionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "Juanjo", "Apellido" : "Jumilla", "Edad" : 35, 1:"Python"}

my_dict = {"Nombre" : "Juanjo", 
           "Apellido" : "Jumilla", 
           "Edad" : 35, 
           "Lenguajes" :{"Python", "Java", "C++"},
           1:1.17

          }

print(my_other_dict)
print(my_dict)

D = {'a':0,'b':1,'c':2}

print(D['b'])

#añadir elementos al diccionario
my_dict["Callenueva"] = "Calle Nueva"
print(my_dict["Nombre"])
print(my_dict["Lenguajes"])
print(my_dict)  


print("Juanjo" in my_dict)
print("Nombre" in my_dict)
