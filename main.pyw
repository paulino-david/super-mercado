from modelo.empleados import *
from modelo.productos import *
from modelo.ventas import *
from vista.interface import *

ventana=Tk()
producto=Productos()
empleado=Empleado()
yo=Interface(ventana,producto,empleado)     
ventana.mainloop()     