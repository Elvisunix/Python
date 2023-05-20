#Variables

my_variable="Hola soy Paco"
my_numero= '2'
my_boolean= False
my_int_to_str_variable=str(my_variable)
print(type(my_int_to_str_variable))
print (my_int_to_str_variable)

#Concatenar texto con la variable
print("El numero premiado es:", my_numero)

#Mostramos por pantalla la cantidad de caracteres de las variables
print(len(my_variable))

#Variables en una sola linea
name , surname, alias = "Juanjo", "Jumilla", "Pandero"
print(alias)

#Concatenar variables
print("Me llamo:", name , "Mi apodo es:" ,alias, "Mi edad es:", 35 )

#Variables solicitadas desde terminal
direccion = input('¿Que dirección quieres buscar?')
print (direccion)