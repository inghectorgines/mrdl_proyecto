from pydoc import describe
import consultas.consulta as modelo


class Acciones:

    def crear(self, usuario):
        print(f"Crear una consulta🩺")
        
        paciente = input("Introduce el nombre del paciente: ")
        descripcion = input("Describe el asunto: ")

        consulta = modelo.Consulta(usuario[0], paciente, descripcion)
        guardar = consulta.guardar()

        if guardar[0] >= 1:
            print(f"\nLa consulta de {consulta.paciente} se ha creado correctamente ✔")
        
        else:
            print(f"\nNo se guardo tu consulta")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]} Tus consultas🩺")
        consulta = modelo.Consulta(usuario[0])
        consultas = consulta.listar()

        for consulta in consultas:
            print("\n-----------------------------------------")
            print("Folio: ", consulta[0])
            print("Nombre del paciente: ", consulta[2])
            print("Descripción de los sintomas: ",consulta[3])
            print("\n-----------------------------------------")
            
    def borrar(self, usuario):
        print(f"\nBorrar consultas🩺")
        paciente = input("Introduce el nombre de tu paciente para borrar la consulta: ")
        consulta = modelo.Consulta(usuario[0], paciente)
        eliminar = consulta.eliminar()
        if eliminar[0]>= 1:
            print(f"Se borro la consulta ✔")
        else:
            print("No se borro la consulta, prueba mas tarde")

    def editar(self, usuario):
        id = input("\nIntroduce el folio de la consulta a editar: ")
        paciente = input("Introduce nombre del paciente: ")
        descripcion = input("Describa el diagnostico: ")
       
        consulta = modelo.Consulta(usuario[0])
        modificar = consulta.editar(paciente, descripcion, id)

        if modificar[0] >= 1:
            print(f"\nLa consulta se actualizo correctamente ✔")
        else:
            print("No se pudo actualizar, prueba más tarde...")