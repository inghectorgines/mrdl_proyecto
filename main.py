print("Nombre: Diana Laura Martinez Romero\nGrupo: 9 A\nMateria: Desarrollo Para Dispositivos Inteligentes\nFecha: 14/06/2022\n")

from usuarios import acciones

print("""
Bienvenido al sistema🩺
Acciones disponibles: 
    - registro
    - login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?:")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
