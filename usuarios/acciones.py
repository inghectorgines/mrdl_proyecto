import usuarios.usuario as modelo
import consultas.acciones 

class Acciones:

    def registro(self):
        print("Registrate en el sistema")

        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        consultorio = input("Introduce el numero de consultorio: ")
        area = input("Introduce el area: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, consultorio, area, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
             print(f"\nDoctor(a): {registro[1].nombre}! Registrado correctamente ✔")
        else:
            print("\nNo te haz registrado correctamnete !!!")


    def login(self):
        print("Identificate en el sistema")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            usuario = modelo.Usuario('', '', '', '', email, password)
            login = usuario.identificar()

            if email == login[5]:
                print(f"Bienvenido al sistema Doctor(a): {login[1]}!")
                self.proximasAcciones(login)

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("\nLogin incorrecto intentalo mas tarde ")
        
    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles🩺
            -Crear Consulta (crear)
            -Mostrar Consultas (mostrar)
            -Eliminar Consulta (eliminar)
            -Editar Consulta (editar)
            -Salir (salir)
        """)
        
        accion = input("¿Que quieres hacer?")
        hasEl = consultas.acciones.Acciones()

        if accion == "crear":
            hasEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hasEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "eliminar":
            hasEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "editar":
            hasEl.editar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            exit()    
