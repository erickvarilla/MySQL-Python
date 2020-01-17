# Para instalar la libreria de mysql
#python -m pip install mysql-connector
# Importar libreria
import mysql.connector
from decimal import Decimal
from mysql.connector import errorcode # para manejar los errores

class Conectar:
    # crear conexion a la base de datos
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="comic"
        )
    except mysql.connector.Error as err: # error de mysql
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Error de conexion de credenciales
            print("Las credenciales de conexion son incorrectas")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            
    else:
        mycursor = mydb.cursor() # importante crear el cursor para hacer referecia a la BD
   
    ##==========================
    ## Metodo para crear un comic
    ##==========================
    def crearComic(self):
        try:
            nombre_comic = input("nombre del comic: \n".upper())
            autor = input("autor del comic: \n".upper())
            fecha = input("utilize el formato año-mes-dia\nfecha de lanzamiento del comic: \n".upper())
            precio = Decimal(input("precio del comic: \n".upper()))
            # sql = "INSERT INTO `revista`(`nombre_comic`, `autor`, `fecha`, `precio`) VALUES ('flash','hernando','2019-10-10',1234)"
            sql = "INSERT INTO `revista`(`nombre_comic`, `autor`, `fecha`, `precio`) VALUES (%s,%s,%s,%s)"
            valores = (nombre_comic,autor,fecha,precio)
            self.mycursor.execute(sql, valores)
            self.mydb.commit()
        except ValueError:
            print("No se pudo ingresar en la base de datos")
        else:
            print("Registro agregado")
        
        
    
    ##==========================
    ## Metodo para listar los comic
    ##==========================
    def ListarComic(self):
        try:
            sql = "SELECT * FROM `revista`"
            self.mycursor.execute(sql)
            myresult = self.mycursor.fetchall()
        except ValueError:
            print("No pudo listar los comics ")
        else:
            print("Numero total de registros: ", self.mycursor.rowcount)
            for x in myresult:
                fecha = str(x[3]).split()
                print("id: {} - Nombre del Comic: {} - Autor: {} - Fecha: {} - Precio: {}".format(x[0],x[1],x[2],fecha[0],x[4]))
    
        
       
    ##==========================
    ## Metodo para buscar un comic
    ##==========================
    def BuscarComis(self):
        try:
            id=input("Digite el codigo del comics que desea buscar: ")
            id2=input("Digite el codigo del comics que desea buscar: ")
            sql='SELECT * FROM revista WHERE id BETWEEN '+id+' AND '+id2
            self.mycursor.execute(sql)
            #myresult = self.mycursor.fetchone() # Obtener solo un registro
            myresult = self.mycursor.fetchall()
        except ValueError:
            print("No se pudo buscar el comics retifique la informacion que busca")
        else:
           for x in myresult:
                fecha = str(x[3]).split()
                print("id: {} - Nombre del Comic: {} - Autor: {} - Fecha: {} - Precio: {}".format(x[0],x[1],x[2],fecha[0],x[4]))

    ##==========================
    ## Metodo para actualizar un comic
    ##==========================
    def actualizar_comic(self):
        try:
            id = int(input("Digite el Codigo del Comic: \n".upper()))
            nombre = input("Nombre Comic: \n".upper())
            sql = 'UPDATE `revista` SET `nombre_comic`= %s WHERE `id` = %s '
            valor = (nombre,id)
            self.mycursor.execute(sql,valor)
            self.mydb.commit()
        except ValueError:
            print("No se pudo actualizar el comic")
        else:
            print("Comics Actualizado...")
    ##==========================
    ## Metodo para eliminar un comic
    ##==========================
    def eliminar_comic(self):
        try:
            id = int(input("Digite el Codigo del Comic: \n".upper()))
            sql = 'DELETE FROM revista WHERE id= %s'
            valor=(id,)
            self.mycursor.execute(sql,valor)
            self.mydb.commit()
        except ValueError:
            print("No se pudo Eliminar el comic")
        else:
            print("Comics Eliminado...")