from conex import Conectar
import datetime
class Compra():
    c = Conectar()
    ##==========================
    ## Metodo para crear una Compra
    ##==========================
    def Crear_Compra(self):
        try:
            print("######################################")
            print("#        Registrar Nueva Compra      #".upper())
            print("######################################\n")
            id_comic = int(input("Codigo del Comis: "))
            id_persona = int(input("Codigo de la Persona: "))
            fecha_actual= datetime.datetime.now()
            fecha_compra = fecha_actual.strftime("%Y-%m-%d %H:%M")# se castea para tener un formato valido para mysql
            sql ="INSERT INTO `compra`(`id_comic`,`id_persona`,`fecha_compra`) VALUES(%s,%s,%s)"
            valor =(id_comic,id_persona,fecha_compra)
            self.c.mycursor.execute(sql,valor)
            self.c.mydb.commit()
        except ValueError:
            print("No se Registro la compra")
        else:
            print("Compra Registrada")
        

    ##==========================
    ## Metodo para listar Compras
    ##==========================
    def Listar_Compras(self):
        try:
            sql="SELECT compra.id_compra,persona.nombre,persona.apellido,persona.identificacion,revista.nombre_comic,revista.precio,compra.fecha_compra FROM `compra` INNER JOIN revista ON revista.id = compra.id_comic INNER JOIN persona ON persona.id = compra.id_persona"
            self.c.mycursor.execute(sql)
            resultado = self.c.mycursor.fetchall()
        except ValueError:
            print("No se Listo La información")
        else:
            print("##################################")
            print("#        Registro de Compras     #".upper())
            print("##################################\n")
            print("Total de compras Registradas: ",self.c.mycursor.rowcount)
            for data in resultado:
                print("Codigo de la Compra: {} - Nombre del Cliente: {} {} - Cedula: {} - Nombre del Comic: {} - Precio: {} - Fecha de Compra: {}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            print()
    ##==========================
    ## Metodo para Buscar Compra
    ##==========================
    def Buscar_Compra(self):
        try:
            id = int(input("Codigo de la compra a buscar: ".upper()))
            sql="SELECT compra.id_compra,persona.nombre,persona.apellido,persona.identificacion,revista.nombre_comic,revista.precio,compra.fecha_compra FROM `compra` INNER JOIN revista ON revista.id = compra.id_comic INNER JOIN persona ON persona.id = compra.id_persona WHERE compra.id_compra = %s"
            valor=(id,)
            self.c.mycursor.execute(sql,valor)
            data = self.c.mycursor.fetchone()
        except ValueError:
            print("No se Listo La información")
        else:
            print("##################################")
            print("#        Registro de Compras     #".upper())
            print("##################################\n")
            print("Total de compras Registradas: ",self.c.mycursor.rowcount)
            print("Codigo de la Compra: {} - Nombre del Cliente: {} {} - Cedula: {} - Nombre del Comic: {} - Precio: {} - Fecha de Compra: {}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6]))
            print()
    
    ##==========================
    ## Metodo para Eliminar Compra
    ##==========================
    def Eliminar_Compra(self):
        try:
            id = int(input("Codigo de la compra a eliminar: ".upper()))
            sql = "DELETE FROM compra WHERE id_compra = %s"
            valor=(id,)
            self.c.mycursor.execute(sql,valor)
            self.c.mydb.commit()
        except ValueError:
            print("Dato no existe")
        else:
            print("Registro Eliminado....")