my_malaga  = "Viva el Malaga"
my_andalucia = "Viva Andalucia"


print (len(my_andalucia))

print (my_andalucia + "menos que" + my_malaga)


#Salto de linea
my_new_line = "La afición Malagueña nunca deja nunca deja de animar\nvamos"
print (my_new_line)

#Tabulador
my_new_line_tabulacion = "arriba arriba arriba\t basti"
print (my_new_line_tabulacion)

#Formateo

name , apellido, edad = "Juanjo" , "Garcia", 36 
print ("Mi nombres es {} {} y mi edad es {}".format(name,apellido,edad))
print ("Mi nombres es %s %s y mi edad es %d" %(name,apellido,edad))
#Formatear las variables
print (f"Mi nombre es  {name}{apellido} y mi edad es {edad}")
