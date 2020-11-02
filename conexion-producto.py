#'!/usr/bin/python3'

import mysql.connector #Se instala un paquete para realizar consultas en la base de datos MYSQL
import cgi #Esta libreria le dice al servidor web cómo enviar y recibir datos de un servidor a un cliente.
from mysql.connector import errorcode #Códigos de error del servidor y del cliente MySQL definidos como atributos 
                                      #del módulo con el número de error como valor facilitando la lectura del codigo fuente.

print("Content-Type: text/html\n") #instruccion que indica al browser el tipo de datos que recibirá.
print(" ") #Espacio en blanco
"""
datos = cgi.FieldStorage() #devuelve los datos del formulario
nombre = format(datos.getvalue('nombre')) #Devuelve el valor de nombre
precio = format(datos.getvalue('precio')) #Devuelve el valor de precio
categoria = format(datos.getvalue('categoria')) #Devuelve el valor de categoria
fechaexp = format(datos.getvalue('fechaexp')) #Devuelve el valor de fechaexp
"""

"""
nombre = 'Arroz Diana'   #Se ingresa el producto y sus atributos
precio = 2000            
categoria = 'perecederos'
fechaexp = '12/31/2020'
"""

print(" ") #se crea otro espacio en blanco para evitar errores
print("<h1>conectando...</h1>") #se imprime un mensaje 
print(" ") #se crea otro espacio en blanco para evitar errores

try: #Tratamiento de errores, cuando ocurre algun error python detiene la ejecución y devulve una exepción.
    #si esto ocurre nos dara una señal que ha occurrido un funcionamiento no esperado o error en el programa, indicándonos aproximadamente qué fue lo que ocurrió.
    cnx = mysql.connector.connect(user='root', password = '1234', database='productospryt', host='127.0.0.1') 
    cursordb = cnx.cursor()
    sql = "INSERT INTO productos(nombre, precio, categoria, fechaexp) VALUES (%s, %s,%s, %s)"
    val = (nombre, precio, categoria, fechaexp)
    cursordb.execute(sql, val)
    cnx.commit()
    print(" ")
    print("<h1>Registro exitoso</h1>")
    print(" ")
    cursordb.close()
    cnx.close()
    print(" ")
    print("<h1>terminado!</h1>")
    print(" ")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("<h1>Something is wrong with your user name or password</h1>")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("<h1>Database does not exist</h1>")
    else:
        print(err)
