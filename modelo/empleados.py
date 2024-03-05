from sqlite3 import *

class Empleado:
    def __init__ (self):
        self.conexx=connect("sistema_de_regitros.db")
        self.cursor=self.conexx.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS empleados(
            id_empleado INTEGER PRIMARY KEY,
            nombre TEXT,
            usuario TEXT UNIQUE,
            contrasena TEXT,
            apellido TEXT,
            telefono INTEGER UNIQUE
        )''')
    def crear(self,id,nombre,usuarios,contraseña,apellido,contacto):
        self.__contraseña=contraseña
        self.cursor.execute(f"INSERT INTO empleados (id_empleado,nombre,usuario,contrasena,apellido,telefono) VALUES (?,?,?,?,?,?)",(id,nombre,usuarios,self.__contraseña,apellido,contacto))
        self.conexx.commit()
        #self.conexx.close()
    
    def leer(self,id):
        self.cursor.execute(f"SELECT * FROM empleados WHERE id_empleado={id}")
        self.mostrar=self.cursor.fetchall()
        return self.mostrar

    def lee_todo(self):
        self.cursor.execute("SELECT * FROM empleados")
        self.mostrar_todo=self.cursor.fetchall()
        return self.mostrar_todo
       
    def actualizar(self,columna,cambio,id):
        self.cursor.execute(f"UPDATE empleados SET {columna}=? WHERE id_empleado=?",(cambio,id))
        self.conexx.commit()

    def eliminar(self,id):
        self.cursor.execute(f"DELETE FROM empleados WHERE id_empleado={id}")
        self.conexx.commit()

    def iniciar_sesion(self,usuarios):
        self.cursor.execute(f"SELECT * FROM empleados WHERE usuario=?",usuarios)
        self.mostrar_usuario=self.cursor.fetchall()
        return self.mostrar_usuario




