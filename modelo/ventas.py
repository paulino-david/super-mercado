from sqlite3 import *

class Ventas:
    def __init__ (self,id_ventas,id_empleado,id_producto,fecha):
        self.id_ventas=id_ventas
        self.id_empleado=id_empleado
        self.id_producto=id_producto
        self.fecha=fecha

        self.connex=connect("sistema_de_regitros.db")
        self.cursor=self.connex.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ventas(
            id_empleado TEXT,
            id_producto TEXT,
            fecha TEXT,
            FOREIGN KEY (id_empleado)
            REFERENCES empleados(id_empleado)
            FOREIGN KEY (id_productos)
            REFERENCES productos(id_producto)
        )''')
        self.connex.commit()
        self.connex.close()

    def crear(self):
        self.cursor.execute("INSERT INTO ventas (id_ventas,id_empleado,id_producto,fecha) VALUES (?,?,?)",(self.id_ventas,self.id_empleado,self.id_producto,self.fecha))
        self.connex.commit()
        self.connex.close()

    def leer(self):
        self.cursor.execute("SELECT * FROM ventas")
        self.mostrador=self.cursor.fetchall()
        print(self.mostrador)
        self.connex.commit()
        self.connex.close()

    def actualizar(self,columna,valor1,valor2):
        self.cursor.execute(f"UPDATE ventas SET {columna}=? WHERE id_ventas=?",(valor1,valor2))
        self.connex.commit()
        self.connex.close()

    def eliminar(self,id_ventas):
        self.cursor.execute(f"DELETE FROM ventas WHERE id_ventas={id_ventas}")
        self.connex.commit()
        self.connex.close()

