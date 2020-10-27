#'!/usr/bin/python3'

import mysql.connector
import cgi
from mysql.connector import errorcode

print("Content-Type: text/html\n")
print(" ")
"""
datos = cgi.FieldStorage()
nombre = format(datos.getvalue('nombre'))
precio = format(datos.getvalue('precio'))
categoria = format(datos.getvalue('categoria'))
fechaexp = format(datos.getvalue('fechaexp'))
"""

"""
nombre = 'Arroz Diana'
precio = 2000
categoria = 'perecederos'
fechaexp = '12/31/2020'
"""

print(" ")
print("<h1>conectando...</h1>")
print(" ")

try:
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
