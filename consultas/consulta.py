from sqlite3 import connect
from unittest import result
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consulta:
    def __init__(self, usuario_id, paciente="", descripcion=""):
        self.usuario_id = usuario_id
        self.paciente = paciente
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO consultas VALUES(null, %s, %s, %s, NOW())"
        consulta = (self.usuario_id, self.paciente, self.descripcion)

        cursor.execute(sql, consulta)
        database.commit()

        return [cursor.rowcount, self]
    
    def listar(self):
        sql = f"SELECT * FROM consultas WHERE usuario_id = {self.usuario_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def editar(self, paciente, descripcion, id):
        sql = f"UPDATE consultas SET paciente = '{paciente}', descripcion = '{descripcion}' WHERE id = {id}"

        try:
            cursor.execute(sql)
            database.commit()

            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
                
    def eliminar(self):
        sql = f"DELETE FROM consultas WHERE usuario_id = {self.usuario_id} AND paciente LIKE '%{self.paciente}%'"
        cursor.execute(sql)
        database.commit()
        return[cursor.rowcount, self]


    