import pandas

csv_file= pandas.read_csv("data.csv")

# Description: Leer un archivo de texto

File1= open("contenido.txt","r")
my_read= File1.read()
print(my_read)

# Leer una linea
my_read= File1.readline(3)
print(my_read)

#Es importante cerrar el archivo
File1.close()

#Escribir en un archivo
File2= open("contenido.txt","w")
File2.write("\nEsta es una nueva linea4")
print(File2)

 