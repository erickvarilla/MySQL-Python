from conex import Conectar
from persona import Persona
f = Conectar()
a = Persona()
# f.mostrar()
# f.crearComic()

print("#################################################")
print("#                   tienda de comics            #".upper())
print("#################################################")
print()
while True:
    print("##################################")
    print("#                Menu            #".upper())
    print("##################################")
    print("#    1. Agregar comics           #".upper())
    print("#    2. Listar comics            #".upper())
    print("#    3. Buscar Comics por Codigo #".upper())
    print("#    4. Modificar Codigo         #".upper())
    print("#    5. Eliminar Codigo          #".upper())
    print("#    6. Agregar Cliente          #".upper())
    print("#    7. Listar Clientes          #".upper())
    print("#    8. Buscar Cliente           #".upper())
    print("#    9. Modificar Cliente        #".upper())
    print("#    10. Eliminar Cliente        #".upper())
    print("#    11. Salir de la tienda      #".upper())
    print("##################################")
    opcion = int(input("Elija una opcion: ".upper()))
    if opcion == 1:
        f.crearComic()
    elif opcion == 2:
        f.ListarComic()
    elif opcion == 3:
        f.BuscarComis()
    elif opcion == 4:
        f.actualizar_comic()
    elif opcion == 5:
        f.eliminar_comic()
    elif opcion == 6:
        a.Crear_Persona()
    elif opcion == 7:
        a.Listar_Personas()
    elif  opcion == 8:
        a.Buscar_Persona()
    elif  opcion == 9:
        a.Modificar_Persona()
    elif  opcion == 10:
        a.eliminar_persona()
    elif opcion == 11:
        break
print("!!!gracias por vicitar nuestra tienda!!!".upper())



