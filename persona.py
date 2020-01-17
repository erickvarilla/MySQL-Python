from conex import Conectar
class Persona:
    a = Conectar()
    ##==========================
    ## Metodo para crear un Cliente
    ##==========================
    def Crear_Persona(self):
        try:            
            nombre = input("nombre: \n".upper())
            apellido = input("apellido: \n".upper())
            telefono = input("telefono: \n".upper())
            dirreccion = input("dirreccion: \n".upper())
            email = input("email: \n".upper())
            identificacion = int(input("identificacion: \n".upper()))
            # sql = "INSERT INTO `revista`(`nombre_comic`, `autor`, `fecha`, `precio`) VALUES ('flash','hernando','2019-10-10',1234)"
            sql = "INSERT INTO persona(nombre,apellido,telefono,dirreccion,email,identificacion) VALUES (%s,%s,%s,%s,%s,%s)"
            valores = (nombre,apellido,telefono,dirreccion,email,identificacion)
            self.a.mycursor.execute(sql, valores)
            self.a.mydb.commit()
        except ValueError:
            print("No pudo listar los comics ")
        else:
            print("Persona Agregada..".upper())
    
    ##==========================
    ## Metodo para Listar Clientes
    ##==========================
    def Listar_Personas(self):
        try:
            sql = "SELECT * FROM `persona`"
            self.a.mycursor.execute(sql)
            resultado = self.a.mycursor.fetchall()
        except ValueError:
            print("no se puedo obtener la información de la base de datos".upper())
        else:
            
            print("###################################")
            print("#        listado de clientes      #".upper())
            print("###################################\n")
            print("Total de registros: ",self.a.mycursor.rowcount)
            for data in resultado:
                print("Identificacion: {} Nombre: {} - Apellido: {} - Telefono: {} - Email: {} - Dirrección: {}".format(data[6],data[0],data[1],data[2],data[4],data[3]))
            print()
                
    ##==========================
    ## Metodo para Buscar Cliente
    ##==========================
    def Buscar_Persona(self):
        try:
            identificacion=int(input("Identificación del Cliente: ".upper()))
            sql = "SELECT * FROM `persona` WHERE `identificacion` = %s"
            valor = (identificacion,)
            self.a.mycursor.execute(sql,valor)
            resultado = self.a.mycursor.fetchone() # Obtengo solo un registro
        except ValueError:
            print("no se puedo obtener la información de la base de datos".upper())
        else:
          
            print("###################################")
            print("#        listado de clientes      #".upper())
            print("###################################\n")
            print("Total de registros: ",self.a.mycursor.rowcount)
            print("Identificacion: {} Nombre: {} - Apellido: {} - Telefono: {} - Email: {} - Dirrección: {}".format(resultado[6],resultado[0],resultado[1],resultado[2],resultado[4],resultado[3]))
            print()
    ##==========================
    ## Metodo para Modificar Cliente
    ##==========================
    def Modificar_Persona(self):
        try:
            identificacion=int(input("Identificación del Cliente: ".upper()))
            email = input("Email: ")
            dirreccion = input("Dirrecion: ")
            telefono = input("Telefono: ")
            sql = "UPDATE `persona` SET `dirreccion` = %s, `telefono` = %s, `email` = %s WHERE `identificacion` = %s"
            valor = (dirreccion,telefono,email,identificacion)
            self.a.mycursor.execute(sql,valor)
            self.a.mydb.commit()
        except ValueError:
            print("no se puedo obtener actualizar la información de la base de datos".upper())
        else:
            print("informacion actualizada..\n".upper())
    ##==========================
    ## Metodo para Eliminar Cliente
    ##==========================
    def eliminar_persona(self):
        try:
            identificacion=int(input("Identificación del Cliente: ".upper()))
            sql ="DELETE FROM `persona` WHERE `identificacion` = %s"
            valor = (identificacion,)
            self.a.mycursor.execute(sql,valor)
            self.a.mydb.commit()
        except ValueError:
            print("No se pudo eliminar el registro".upper())
        else:
            print("Registro Eliminado..".upper())


