from tkinter import *
from PIL import Image,ImageTk
import time

texto= " "
class Interface:
    def __init__(self,ventana, producto,empleados):
        self.ventana=ventana
        self.empleados=empleados 
        self.ventana.geometry("500x400")
        self.ventana.config(bg="lightblue")
        self.perfil=Image.open("C:/Users/Paulino/Documents/Programming/Programming Documents/ARCHIVOS DE APRENDIZAGE/perfil 1.jpg")
        self.recorte=self.perfil.resize((int(self.perfil.width/3),int(self.perfil.height/3)))
        self.imgtk=ImageTk.PhotoImage(self.recorte)

        self.us=StringVar()
        self.con=StringVar()
        self.producto =producto
            
        self.imgperfil=Label(self.ventana,image=self.imgtk).pack()
        self.us_usuario=Label(self.ventana,text="Usuario: ",bg="lightblue").place(x=10,y=200)
        self.contraseña=Label(self.ventana,text="Contraseña: ",bg="lightblue").place(x=10,y=250)
            
        self.us_entrada=Entry(self.ventana,width=50,relief="sunken",textvariable=self.us).place(x=70,y=200)
        self.con_entrada=Entry(self.ventana,width=50,relief="sunken",textvariable=self.con).place(x=90,y=250)

        self.continuar=Button(self.ventana,text="Continuar",relief="flat",bg="lightblue",command=self.continuar).place(x=300,y=360)
        self.cerrar=Button(self.ventana,text="Cerrar",relief="flat",bg="grey",command=self.ventana.destroy).place(x=420,y=360)


    def continuar(self):
        self.leer_empleados=self.empleados.lee_todo()
        for recorer_empleados in self.leer_empleados:
            if self.us.get()=="" and self.con.get()=="":
                self.error_both=Label(self.ventana,text="Inserte su nombre de usuario y su contraseña",bg="lightblue",fg="red")
                self.error_both.place(x=100,y=300)
                break

            if self.us.get()==recorer_empleados[2] and self.con.get()==recorer_empleados[3]:
                self.correct_both=Label(self.ventana,text="Correcto                              ",bg="lightblue",fg="lightgreen")
                self.correct_both.place(x=150,y=300)
                self.nex()
            else:
                self.error_both=Label(self.ventana,text="Error en el usuario o la contraseña                    ",bg="lightblue",fg="red")
                self.error_both.place(x=100,y=300) 
                break
    def nex(self):  
        self.ventana.withdraw()
        self.registro=Tk()
        self.registro.geometry("500x400")
        self.registro.config(bg="white")
    
        self.bara_menu=Menu(self.registro)
        self.registro.config(menu=self.bara_menu)
    
        self.menu_registro=Menu(self.bara_menu,tearoff=False)
        self.bara_menu.add_cascade(label="Registros",menu=self.menu_registro)
        self.menu_registro.add_command(label="Empleados",command=self.empleado)

        self.operaciones_menu=Menu(self.bara_menu,tearoff=False)
        self.bara_menu.add_cascade(label="Operaciones",menu=self.operaciones_menu)
        self.operaciones_menu.add_command(label="Nuevo Producto",command=self.nuev)
        self.operaciones_menu.add_command(label="Facturar",command=self.factura)
        self.operaciones_menu.add_command(label="Eliminar Producto",command=self.interface_eliminar_producto)
        self.operaciones_menu.add_command(label="Actualizar datos de productos",command=self.interface_actualizacion)
        
        self.tabla_sec=Frame(self.registro,relief="sunken",height=200,width=480,borderwidth=2,bg="white")
        self.tabla_sec.place(x=10,y=190)
        
        self.titulo=Label(self.registro,text="REGISTROS DE PRODUCTOS",bg="white",font=30)
        self.titulo.place(x=130,y=100)
        self.id=Label(self.tabla_sec,text="ID    |",bg="white")
        self.id.place(x=1,y=1)
        self.nombre=Label(self.tabla_sec,text="Nombres                         |",bg="white")
        self.nombre.place(x=30,y=1)
        self.precios=Label(self.tabla_sec,text="Precios                                |",bg="white")
        self.precios.place(x=165,y=1)    
        self.stock=Label(self.tabla_sec,text="Stock                                ",bg="white")
        self.stock.place(x=310,y=1)  
    
        self.lis_id=Listbox(self.tabla_sec,width=4,height=11,relief="sunken")
        self.lis_id.place(x=1,y=20)
        self.lis_nombre=Listbox(self.tabla_sec,width=24,height=11,relief="sunken")
        self.lis_nombre.place(x=30,y=20)  
        self.lis_precio=Listbox(self.tabla_sec,width=24,height=11,relief="sunken")
        self.lis_precio.place(x=156,y=20) 
        self.lis_stock=Listbox(self.tabla_sec,width=27,height=11,relief="sunken")
        self.lis_stock.place(x=305,y=20) 

               
        leer_producto=self.producto.lee_todo()
        for recorer in leer_producto:
            self.lis_id.insert(1,f"{recorer[0]}\n")
            self.lis_nombre.insert(1,f"{recorer[1]}\n")
            self.lis_precio.insert(1,f"{recorer[2]} FCFA\n")
            self.lis_stock.insert(1,f"{recorer[3]}\n")

    def nuev(self):
        self.registro.withdraw()
        self.n_p=Toplevel()
        self.n_p.geometry("400x300")
        self.n_p.config(bg="white")

        self.id_entrada_producto=IntVar()
        self.nom=StringVar()
        self.prec=IntVar()
        self.stoc=IntVar()
        
        self.titulo1=Label(self.n_p,text="NUEVO PRODUCTO",bg="white",font=30)
        self.titulo1.pack()
        self.id_productos=Label(self.n_p,text="ID del Producto: ",bg="white")
        self.id_productos.place(x=10,y=50)
        self.nombre=Label(self.n_p,text="Nombre del producto: ",bg="white")
        self.nombre.place(x=10,y=90)
        self.precio=Label(self.n_p,text="Precio del producto: ",bg="white")
        self.precio.place(x=10,y=140)    
        self.stock=Label(self.n_p,text="Stock del producto: ",bg="white")
        self.stock.place(x=10,y=190)
    
        self.id_entrada=Entry(self.n_p,width=40,relief="sunken",textvariable=self.id_entrada_producto)
        self.id_entrada.place(x=130,y=50)
        self.nom_entrada=Entry(self.n_p,width=40,relief="sunken",textvariable=self.nom)
        self.nom_entrada.place(x=140,y=90)
        self.precio_entrada=Entry(self.n_p,width=40,relief="sunken",textvariable=self.prec)
        self.precio_entrada.place(x=130,y=140)
        self.stock_entrada=Entry(self.n_p,width=40,relief="sunken",textvariable=self.stoc)
        self.stock_entrada.place(x=130,y=190)

        self.registrar=Button(self.n_p,text="Registrar",relief="flat",bg="lightblue",command=self.register)
        self.registrar.place(x=100,y=250)
        self.cancelar=Button(self.n_p,text="Cerrar",relief="flat",bg="grey",command=self.ciere)
        self.cancelar.place(x=200,y=250)

    def register(self): 
        leer=self.producto.crear(self.id_entrada_producto.get(),self.nom.get(),self.prec.get(),self.stoc.get())
        self.lis_id.insert(1,f"{self.id_entrada_producto.get()}\n")
        self.lis_nombre.insert(1,f"{self.nom.get()}\n")
        self.lis_precio.insert(1,f"{self.prec.get()} FCFA\n")
        self.lis_stock.insert(1,f"{self.stoc.get()}\n")
        self.n_p.destroy()
        self.registro.deiconify()

    def ciere(self):
        self.n_p.destroy()
        self.registro.deiconify()        

    def interface_eliminar_producto(self):
        self.registro.withdraw()
        self.interface_eliminar=Toplevel()
        self.interface_eliminar.geometry("400x300")

        self.borrador=StringVar()

        self.etiqueta_general=Label(self.interface_eliminar,text="Eliminador de Productos")
        self.etiqueta_general.place(x=140,y=10)
        self.etiqueta_eliminar=Label(self.interface_eliminar,text="Introduzca el ID del producto: ")
        self.etiqueta_eliminar.place(x=10,y=50)
        self.entrada_eliminar=Entry(self.interface_eliminar,width=50,textvariable=self.borrador)
        self.entrada_eliminar.place(x=10,y=80)

        self.boton_listo=Button(self.interface_eliminar,text="Listo",bg="lightblue",relief="flat",command=self.listo_eliminar)
        self.boton_listo.place(x=100,y=200)
        self.cerrar_eliminador=Button(self.interface_eliminar,text="Cerrar",relief="flat",bg="grey",command=self.cerrar_eliminar)
        self.cerrar_eliminador.place(x=200,y=200)


    def listo_eliminar(self):
        self.interface_eliminar.withdraw()
        self.producto.eliminar(self.borrador.get())
        self.nex()

    def cerrar_eliminar(self):
        self.interface_eliminar.withdraw()
        self.registro.deiconify()

    def interface_actualizacion(self):
        self.registro.withdraw()
        self.interface_actualizar=Toplevel()
        self.interface_actualizar.geometry("400x300")

        self.id_entry=IntVar()
        self.entry_nombre=StringVar()
        self.entry_precio=IntVar()
        self.entry_stock=IntVar()
        self.operacion=" "

        self.etiqueta_actualizar=Label(self.interface_actualizar,text="Actualizaciónes",font=30)
        self.etiqueta_actualizar.place(x=50,y=20)

        self.id_actualizar=Label(self.interface_actualizar,text="ID: ")
        self.id_actualizar.place(x=10,y=50)
        self.entrada_id=Entry(self.interface_actualizar,width=50,textvariable=self.id_entry)
        self.entrada_id.place(x=35,y=50)

        self.actualizar_menuboton=Menubutton(self.interface_actualizar,text="Haga click aqui para seleccionar lo que deseas actualizar")
        self.actualizar_menuboton.place(x=10,y=80)

        self.dentro_menuboton=Menu(self.actualizar_menuboton,tearoff=False)
        self.actualizar_menuboton["menu"]=self.dentro_menuboton

        self.dentro_menuboton.add_command(label="Nombre",command=self.actualizar_nombre)
        self.dentro_menuboton.add_command(label="Precio",command=self.actualizar_precio)
        self.dentro_menuboton.add_command(label="Stock",command=self.actualizar_stock)

        self.boton_actualizar=Button(self.interface_actualizar,text="Actualizar",bg="lightblue",relief="flat",command=self.actualizacion)
        self.boton_actualizar.place(x=100,y=250)

        self.boton_cerrar=Button(self.interface_actualizar,text="Cerrar",bg="grey",relief="flat",command=self.cerrar_actualizacion)
        self.boton_cerrar.place(x=200,y=250)

    def cerrar_actualizacion(self):
        self.interface_actualizar.withdraw()
        self.registro.deiconify()

    def actualizar_nombre(self):

        self.operacion="nombre"

        self.nombre=Label(self.interface_actualizar,text="Nombre: ")
        self.nombre.place(x=10,y=110)
        self.nombre_entrada=Entry(self.interface_actualizar,width=50,textvariable=self.entry_nombre)
        self.nombre_entrada.place(x=70,y=110)
        self.actualizar__empleados=self.entry_nombre.get()


    def actualizar_precio(self):

        self.operacion="precio"

        self.precio=Label(self.interface_actualizar,text="Precio: ")
        self.precio.place(x=10,y=150)
        self.precio_entrada=Entry(self.interface_actualizar,width=50,textvariable=self.entry_precio)
        self.precio_entrada.place(x=70,y=150)
        self.actualizar__empleados=self.entry_precio.get()

    def actualizar_stock(self):

        self.operacion="stock"

        self.stock=Label(self.interface_actualizar,text="Stock: ")
        self.stock.place(x=10,y=190)
        self.stock_entrada=Entry(self.interface_actualizar,width=50,textvariable=self.entry_stock)
        self.stock_entrada.place(x=70,y=190)
        self.actualizar__empleados=self.entry_stock.get()

    def actualizacion(self):
        if self.operacion=="nombre":
            self.producto.actualizar(self.operacion,self.entry_nombre.get(),self.id_entry.get())
        if self.operacion=="precio":
            self.producto.actualizar(self.operacion,self.entry_precio.get(),self.id_entry.get())  
        if self.operacion=="stock":
            self.producto.actualizar(self.operacion,self.entry_stock.get(),self.id_entry.get())          
        self.interface_actualizar.destroy()
        self.nex()

    
    def factura(self):
        self.registro.withdraw()
        self.pantalla= Toplevel()
        self.pantalla.geometry("10000x800")
        self.pantalla.title("PAVL MARKET S.L")
        
        self.tema=Label(self.pantalla,text="PAVL MARKET",font=16)
        self.tema.pack(pady=1)
        
        self.doble1=PanedWindow(self.pantalla,orient="horizontal",width=700,height=700)
        self.doble1.place(x=160,y=50)
        
        self.izquierda=Listbox(self.doble1,relief="raised")
        self.doble1.add(self.izquierda)
        
        self.var_texto = StringVar()
        self.entrada= StringVar()

    
        self.prodtag=Label(self.pantalla,text="Producto: ",font=12)
        self.prodtag.place(x=1020,y=30)
        self.entprod=Entry(self.pantalla,textvar=self.entrada,width=60,borderwidth=5)
        self.entprod.place(x=1120,y=30)
        
        self.peqpan=Label(self.pantalla,width=70,borderwidth=5,height=19,relief="sunken",bg="grey",textvar=self.var_texto)
        self.peqpan.place(x=1020,y=100)
        self.derecho=Frame(self.pantalla,width=500,borderwidth=5,height=450,relief="sunken",bg="grey")
        self.derecho.place(x=1020,y=300)
        
        self.prectag=Label(self.pantalla,text="Precios ",font=12,fg="black")
        self.prectag.place(x=1240,y=720)

        self.boton7=Button(self.pantalla,text=7,bg="black",fg="white",command= lambda:self.botones(7))
        self.boton7.place(x=1025,y=305,width=100,height=100)
        self.boton8=Button(self.pantalla,text=8,bg="black",fg="white",command=lambda: self.botones(8))
        self.boton8.place(x=1130,y=305,width=100,height=100)
        self.boton9=Button(self.pantalla,text=9,bg="black",fg="white",command=lambda: self.botones(9))
        self.boton9.place(x=1235,y=305,width=100,height=100)
        self.boton4=Button(self.pantalla,text=4,bg="black",fg="white",command=lambda: self.botones(4))
        self.boton4.place(x=1025,y=410,width=100,height=100)
        self.boton5=Button(self.pantalla,text=5,bg="black",fg="white",command=lambda: self.botones(5))
        self.boton5.place(x=1130,y=410,width=100,height=100)
        self.boton6=Button(self.pantalla,text=6,bg="black",fg="white",command=lambda: self.botones(6))
        self.boton6.place(x=1235,y=410,width=100,height=100)
        self.boton1=Button(self.pantalla,text=1,bg="black",fg="white",command=lambda: self.botones(1))
        self.boton1.place(x=1025,y=515,width=100,height=100)
        self.boton2=Button(self.pantalla,text=2,bg="black",fg="white",command=lambda: self.botones(2))
        self.boton2.place(x=1130,y=515,width=100,height=100)
        self.boton3=Button(self.pantalla,text=3,bg="black",fg="white",command=lambda: self.botones(3))
        self.boton3.place(x=1235,y=515,width=100,height=100)
        self.boton0=Button(self.pantalla,text=0,bg="black",fg="white",command=lambda: self.botones(0))
        self.boton0.place(x=1025,y=620,width=208,height=100)
        self.borrador=Button(self.pantalla,text="CE",bg="red",fg="white",command=lambda: self.borrar_total())
        self.borrador.place(x=1445,y=305,width=70,height=100)
        self.suma=Button(self.pantalla,text="+",bg="black",fg="white",command= lambda: self.botones("+"))
        self.suma.place(x=1340,y=305,width=100,height=100)
        self.resta=Button(self.pantalla,text="-",bg="black",fg="white",command= lambda: self.botones("-"))
        self.resta.place(x=1340,y=410,width=100,height=100)
        self.multy=Button(self.pantalla,text="*",bg="black",fg="white",command= lambda: self.botones("*"))
        self.multy.place(x=1340,y=515,width=100,height=100)
        self.divi=Button(self.pantalla,text="/",bg="black",fg="white",command= lambda:self.botones("/"))
        self.divi.place(x=1340,y=620,width=100,height=100)
        self.decimal=Button(self.pantalla,text=".",bg="black",fg="white",command= lambda: self.botones("."))
        self.decimal.place(x=1235,y=620,width=100,height=100)
        self.igual_a=Button(self.pantalla,text="=",bg="orange",fg="white",command=lambda: self.igual())
        self.igual_a.place(x=1445,y=410,width=70,height=310)
    
        self.guardar=Button(self.pantalla,text="Guardar",bg="orange",fg="white",command=self.Guardar)
        self.guardar.place(x=885,y=300,width=100,height=100)
        self.salir=Button(self.pantalla,text="Salir",bg="red",fg="white",command=self.salir_factura)
        self.salir.place(x=1410,y=750,width=100,height=40)
        self.limpia=Button(self.pantalla,text="Limpiar",bg="brown",fg="white",command=self.limpiar)
        self.limpia.place(x=500,y=750,width=100,height=40)

    def Guardar(self):
        global texto
        with open("Ventas.txt","a") as self.Archivo:
            self.Entrada=self.entrada.get()
            self.total=str(eval(texto))
            self.cadena=str(list(time.localtime()))
            self.fecha=self.cadena[1:11].replace(",","-")
            self.hora=self.cadena[14:19].replace(",",":")
            self.escribir=self.Archivo.write(f"{self.Entrada}                            {self.total}FCFA                                {self.fecha}         {self.hora}\n")
        with open("Ventas.txt","r") as self.abrrir:
            self.lineas=self.abrrir.readlines()
            for self.i in self.lineas:
                if self.i[0:len(self.Entrada)]==self.Entrada:
                    self.izquierda.insert(1,self.i)
                    
    def botones(self,num_o_sig):
        global texto
        texto= texto + str(num_o_sig)
        self.var_texto.set(texto)
    
    def igual(self):
        global texto
        try:
            self.total=str(eval(texto))
            self.var_texto.set(self.total)
        except SyntaxError:
            self.var_texto.set("Error de calculo")
    
    def borrar_total(self):
        global texto
        texto= " "
        self.var_texto.set(texto)
    
    def limpiar(self):
       self.izquierda.delete(0,END) 

    def salir_factura(self):
        self.pantalla.withdraw()
        self.registro.deiconify()
                
    def empleado(self):
        self.registro.withdraw()
        self.registro2=Toplevel()

        self.registro2.geometry("500x400")

        self.registro2.config(bg="white")
    
        self.bara_menu2=Menu(self.registro2)
        self.registro2.config(menu=self.bara_menu2)

        self.menu_registro2=Menu(self.bara_menu2,tearoff=False)
        self.bara_menu2.add_cascade(label="Registros",menu=self.menu_registro2)
        self.menu_registro2.add_command(label="Productos",command=self.menu)
        
        self.segundo_menu=Menu(self.bara_menu2,tearoff=False)
        self.bara_menu2.add_cascade(label="Operaciones",menu=self.segundo_menu)
        self.segundo_menu.add_command(label="Añadir Empleado",command=self.add_empleado)
        self.segundo_menu.add_command(label="Eliminar Empleado",command=self.interface_eliminar_empleado)
        self.segundo_menu.add_command(label="Actualizar Empleado",command=self.actualizar_empleados)

        self.tabla_sec2=Frame(self.registro2,relief="sunken",height=200,width=480,borderwidth=2,bg="white")
        self.tabla_sec2.place(x=10,y=190)
        
        self.titulo2=Label(self.registro2,text="REGISTROS DE EMPLEADOS",bg="white",font=30)
        self.titulo2.place(x=130,y=100)        
        self.id2=Label(self.tabla_sec2,text="ID    |",bg="white")
        self.id2.place(x=1,y=1)
        self.nombre2=Label(self.tabla_sec2,text="Nombres              |",bg="white")
        self.nombre2.place(x=130,y=1)
        self.usuarios=Label(self.tabla_sec2,text="Usuarios                |",bg="white")
        self.usuarios.place(x=30,y=1)        
        self.precios2=Label(self.tabla_sec2,text="Apellidos                       |",bg="white")
        self.precios2.place(x=228,y=1)    
        self.stock2=Label(self.tabla_sec2,text="Telefono                           ",bg="white")
        self.stock2.place(x=355,y=1)  
    
        self.lis_id2=Listbox(self.tabla_sec2,width=4,height=11,relief="sunken")
        self.lis_id2.place(x=1,y=20)
        self.lis_usuarios=Listbox(self.tabla_sec2,width=20,height=11,relief="sunken")
        self.lis_usuarios.place(x=30,y=20)        
        self.lis_nombre2=Listbox(self.tabla_sec2,width=20,height=11,relief="sunken")
        self.lis_nombre2.place(x=130,y=20)  
        self.lis_apell2=Listbox(self.tabla_sec2,width=20,height=11,relief="sunken")
        self.lis_apell2.place(x=230,y=20) 
        self.lis_contac2=Listbox(self.tabla_sec2,width=27,height=11,relief="sunken")
        self.lis_contac2.place(x=355,y=20) 

        leer_empleados=self.empleados.lee_todo()
        for recorer_empleado in leer_empleados:
            self.lis_id2.insert(1,f"{recorer_empleado[0]}\n")
            self.lis_nombre2.insert(1,f"{recorer_empleado[1]}\n")
            self.lis_usuarios.insert(1,f"{recorer_empleado[2]}\n")
            self.lis_apell2.insert(1,f"{recorer_empleado[4]}\n")   
            self.lis_contac2.insert(1,f"{recorer_empleado[5]}\n")           
    def add_empleado(self):
        self.registro2.withdraw()
        self.n_e=Toplevel()
        self.n_e.geometry("400x400")
        self.n_e.config(bg="white")

        self.id2=IntVar()
        self.nom2=StringVar()
        self.apell2=StringVar()
        self.contac2=IntVar()
        self.code=StringVar()

        self.titulo2=Label(self.n_e,text="NUEVO EMPLEADO",bg="white",font=30)
        self.titulo2.pack()

        self.id_productos=Label(self.n_e,text="ID del Producto: ",bg="white")
        self.id_productos.place(x=10,y=50)       
        self.nombre2=Label(self.n_e,text="Nombre del empleado: ",bg="white")
        self.nombre2.place(x=10,y=90)
        self.precio2=Label(self.n_e,text="Apellidos del empleado: ",bg="white")
        self.precio2.place(x=10,y=140)    
        self.stock2=Label(self.n_e,text="Telefono del empleado: ",bg="white")
        self.stock2.place(x=10,y=190)
        self.contraseña=Label(self.n_e,text="Contraseña del empleado: ",bg="white")
        self.contraseña.place(x=10,y=240)

        self.id_entrada=Entry(self.n_e,width=40,relief="sunken",textvariable=self.id2)
        self.id_entrada.place(x=130,y=50)   
        self.nom_entrada2=Entry(self.n_e,width=40,relief="sunken",textvariable=self.nom2)
        self.nom_entrada2.place(x=140,y=90)
        self.precio_entrada2=Entry(self.n_e,width=40,relief="sunken",textvariable=self.apell2)
        self.precio_entrada2.place(x=140,y=140)
        self.stock_entrada2=Entry(self.n_e,width=40,relief="sunken",textvariable=self.contac2)
        self.stock_entrada2.place(x=140,y=190)
        self.contraseña_entrada=Entry(self.n_e,width=40,relief="sunken",textvariable=self.code)
        self.contraseña_entrada.place(x=150,y=240)

        self.registrar2=Button(self.n_e,text="Registrar",relief="flat",bg="lightblue",command=self.register2)
        self.registrar2.place(x=100,y=300)
        self.cancelar2=Button(self.n_e,text="Cerrar",relief="flat",bg="grey",command=self.cerrar2)
        self.cancelar2.place(x=200,y=300)

    def register2(self): 
        self.tiempo_actual=str(time.localtime()).replace(","," ")
        self.usuario=f"{self.tiempo_actual[25:29]}{self.nom2.get()[0:2]}{self.apell2.get()[0:2]}{self.tiempo_actual[60:62]}"
        self.empleados.crear(self.id2.get(),self.nom2.get(),self.usuario,self.code.get(),self.apell2.get(),self.contac2.get())
        self.lis_id2.insert(1,f"{self.id2.get()}\n")
        self.lis_nombre2.insert(1,f"{self.nom2.get()}\n")
        self.lis_usuarios.insert(1,self.usuario)
        self.lis_apell2.insert(1,f"{self.apell2.get()}\n")
        self.lis_contac2.insert(1,f"{self.contac2.get()}\n")
        self.n_e.destroy()
        self.registro2.deiconify()
    
    def cerrar2(self):
        self.n_e.destroy()
        self.registro2.deiconify()

    def interface_eliminar_empleado(self):
        self.registro2.withdraw()
        self.eliminar=Toplevel()
        self.eliminar.geometry("400x300")

        self.entry_borrador=StringVar()

        self.eliminar_label=Label(self.eliminar,text="Eliminador de Empleados",font=30)
        self.eliminar_label.place(x=90,y=0)

        self.nombre_borrador=Label(self.eliminar,text="Introduzca el ID del Producto: ")
        self.nombre_borrador.place(x=10,y=40)

        self.entrada_borrador=Entry(self.eliminar,width=50,textvariable=self.entry_borrador)
        self.entrada_borrador.place(x=10,y=60)

        self.boton_eliminar=Button(self.eliminar,text="Eliminar",relief="flat",bg="brown",command=self.eliminar_empleado)
        self.boton_eliminar.place(x=100,y=100)
        self.boton_cancelar=Button(self.eliminar,text="Cerrar",relief="flat",bg="grey",command=self.cerrar_eliminar_empleado)
        self.boton_cancelar.place(x=200,y=100) 

    def cerrar_eliminar_empleado(self):
        self.eliminar.destroy()
        self.registro2.deiconify()

    def eliminar_empleado(self):
        self.eliminar.destroy()
        self.eliminador=self.empleados.eliminar(self.entry_borrador.get())
        self.empleado()

    def actualizar_empleados(self):
        self.registro2.withdraw()
        self.interface_actualizar_empleados=Toplevel()
        self.interface_actualizar_empleados.geometry("400x300")

        self.id_entry_empleado=IntVar()
        self.entry_nombre_empleado=StringVar()
        self.entry_apellido_empleado=StringVar()
        self.entry_telefono_empleado=IntVar()
        self.columna_empleado=" "

        self.etiqueta_actualizar_empleado=Label(self.interface_actualizar_empleados,text="Actualizaciónes",font=30)
        self.etiqueta_actualizar_empleado.place(x=50,y=20)

        self.id_actualizar_empleado=Label(self.interface_actualizar_empleados,text="ID: ")
        self.id_actualizar_empleado.place(x=10,y=50)
        self.entrada_id_empleado=Entry(self.interface_actualizar_empleados,width=50,textvariable=self.id_entry_empleado)
        self.entrada_id_empleado.place(x=35,y=50)

        self.actualizar_menuboton_emplados=Menubutton(self.interface_actualizar_empleados,text="Haga click aqui para seleccionar lo que deseas actualizar")
        self.actualizar_menuboton_emplados.place(x=10,y=80)

        self.dentro_menuboton_empleados=Menu(self.actualizar_menuboton_emplados,tearoff=False)
        self.actualizar_menuboton_emplados["menu"]=self.dentro_menuboton_empleados

        self.dentro_menuboton_empleados.add_command(label="Nombre",command=self.actualizar_nombre_empleado)
        self.dentro_menuboton_empleados.add_command(label="Apellido",command=self.actualizar_apellido)
        self.dentro_menuboton_empleados.add_command(label="Telefono",command=self.actualizar_telefono)

        self.boton_actualizar_empleados=Button(self.interface_actualizar_empleados,text="Actualizar",bg="lightblue",relief="flat",command=self.actualizacion_empleado)
        self.boton_actualizar_empleados.place(x=100,y=250)

        self.boton_cerrar_empleados=Button(self.interface_actualizar_empleados,text="Cerrar",bg="grey",relief="flat",command=self.cerrar_actualizacion_empleado)
        self.boton_cerrar_empleados.place(x=200,y=250)

    def cerrar_actualizacion_empleado(self):
        self.interface_actualizar_empleados.withdraw()
        self.registro2.deiconify()

    def actualizar_nombre_empleado(self):
        global actualizar__empleado
        self.columna_empleado="nombre"

        self.nombre_empleado=Label(self.interface_actualizar_empleados,text="Nombre: ")
        self.nombre_empleado.place(x=10,y=110)
        self.nombre_entrada_empleado=Entry(self.interface_actualizar_empleados,width=50,textvariable=self.entry_nombre_empleado)
        self.nombre_entrada_empleado.place(x=70,y=110)

    def actualizar_apellido(self):
        global actualizar__empleado
        self.columna_empleado="apellido"

        self.precio_empleado=Label(self.interface_actualizar_empleados,text="Apellido: ")
        self.precio_empleado.place(x=10,y=150)
        self.precio_entrada_empleado=Entry(self.interface_actualizar_empleados,width=50,textvariable=self.entry_apellido_empleado)
        self.precio_entrada_empleado.place(x=70,y=150)

    def actualizar_telefono(self):
        global actualizar__empleado
        self.columna_empleado="telefono"

        self.stock_empleado=Label(self.interface_actualizar_empleados,text="Telefono: ")
        self.stock_empleado.place(x=10,y=190)
        self.stock_entrada_empleado=Entry(self.interface_actualizar_empleados,width=50,textvariable=self.entry_telefono_empleado)
        self.stock_entrada_empleado.place(x=70,y=190)

    def actualizacion_empleado(self):
        if self.columna_empleado=="nombre":
            self.empleados.actualizar(self.columna_empleado,self.entry_nombre_empleado.get(),self.id_entry_empleado.get())
        if self.columna_empleado=="apellido":
            self.empleados.actualizar(self.columna_empleado,self.entry_apellido_empleado.get(),self.id_entry_empleado.get())
        if self.columna_empleado=="telefono":
            self.empleados.actualizar(self.columna_empleado,self.entry_telefono_empleado.get(),self.id_entry_empleado.get())
        self.interface_actualizar_empleados.destroy()
        self.empleado()


    def menu(self):
        self.registro2.withdraw()
        self.registro.deiconify() 
