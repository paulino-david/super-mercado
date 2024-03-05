from sqlite3 import *

class Productos:
    def __init__ (self):
        self.connex=connect("sistema_de_regitros.db")
        self.cursor=self.connex.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
            id_producto INTEGER PRIMARY KEY,
            nombre TEXT,
            precio INTEGER,
            stock INTEGER
        )''') 
    def crear(self,id_producto,nombre,precio,stock):
        self.cursor.execute("INSERT INTO productos (id_producto,nombre,precio,stock) VALUES (?,?,?,?)",(id_producto,nombre,precio,stock))
        self.connex.commit()
        #self.connex.close()

    def leer(self,id):
        self.cursor.execute(f"SELECT * FROM productos WHERE id_producto={id}")
        mostrador=self.cursor.fetchall()
        return mostrador
        
    def lee_todo(self):
        self.cursor.execute("SELECT * FROM productos")
        mostrar=self.cursor.fetchall()
        return mostrar
        
    def actualizar(self,columna,cambio,id):
        self.cursor.execute(f"UPDATE productos SET {columna}=? WHERE id_producto=?",(cambio,id))
        self.connex.commit()
        

    def eliminar(self,id):
        self.cursor.execute("DELETE FROM productos WHERE id_producto=?",(id))
        self.connex.commit()
        #self.connex.close()

#producto=Productos()
#producto.crear("manuel",899,4)
#self.empleados.actualizar(self.operacion,self.entry_nombre.get(),self.id_entry.get())
#print(self.producto.lee_todo())
#print(producto.lee_todo())
#producto.eliminar()