""" 
Deyner Fabian Serrano / Luigi Navarro 
MacoWins es una reconocida cadena de ropa formal, con tiendas en muchas ciudades de Argentina.
Recientemente, le han pedido a 2Diseños, nuestra consultora de software, que desarrolle un nuevo
sistema para la gestión de sus ventas y stock.
MacoWins guarda la información de sus productos en una lista con la siguiente forma:
"""


# Productos definidos
buzo_talle_s = {"codigo":100,"nombre":"buzo talle s","categoria":"buzo","precio": 3000,"stock":0}
buzo_talle_m = {"codigo":125,"nombre":"buzo talle m","categoria":"buzo","precio": 4000,"stock":0}
buzo_talle_l = {"codigo":1500,"nombre":"buzo talle l","categoria":"buzo","precio": 5000,"stock":0}
jean_talle_38 = {"codigo":200,"nombre":"jean talle 38","categoria":"jean","precio":8000,"stock":0}
jean_talle_40 = {"codigo":250,"nombre":"jean talle 40","categoria":"jean","precio":9000,"stock":0}
jean_talle_42 = {"codigo":300,"nombre":"jean talle 42","categoria":"jean","precio":10000,"stock":0}

from math import prod
import time
from collections import Counter
productos = []
ventas = []


productos = []
ventas = []



class Prenda:
    def __init__(self, un_nombre, un_codigo, un_precio):
        self.nombre = un_nombre
        self.codigo = un_codigo
        self.precio = un_precio
        self.estado = Nueva()

def precio_total(self):
    if self.estado == "nueva":                   
        return self.precio
    if self.estado == "promocion":
       valor_fijo = 40
       return self.precio - valor_fijo
    if self.estado == "Promocion_al_20":
        valor_fijo = 20
       return self.precio - valor_fijo
    if self.estado == "Liquidacion":
        return self.precio/2 

class Nueva:
    def precio_final(self, precio):
        return precio
class Promocion:
    def  __init__(self, valor):
        self.valor_promo = valor

    def precio_final(self, precio):
        return precio - self.valor_promo    
class Liquidacion:
    def precio_final(self, precio):
        return precio / 2 

def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

def precio_final(self,precio):
        precio_final = self.estado.precio_final(precio)
        return precio_final

def es_de_categoria(self,categoria):
        return categoria in self.categoria                    


# ¿Puede la programación orientada a objetos ayudarnos
# en este punto? ¿Por qué?
# Respuesta: Si, porque estamos trabajando con obejtos,

# ¿Qué objeto debería tener ahora la responsabilidad de resolver
# el problema de calcular el precio final de un producto?
#Respuesta: self.estado(precio)
class Sucursal:
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.gasto_del_dia = 10000

    def registrar_producto(self,nuevo_producto):
        largo_inicial = len(self.productos)
        self.productos.add(nuevo_producto)
        if len(self.productos) == largo_inicial:
            raise ValueError ("El producto ya se encuentra registrado")

    def recargar_stock(self,codigo_producto,cantidad_a_agregar):
        codigo_valido = False
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               codigo_valido = True
               producto.stock += cantidad_a_agregar
        if not codigo_valido:
            raise ValueError ("El codigo no corresponde a un producto registrado")      

    def realizar_compra(self,codigo_producto,cantidad_a_comprar,es_extranjero):
        codigo_valido = False
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               codigo_valido = True
               if self.hay_stock(codigo_producto) and  producto.stock > cantidad_a_comprar:
                  producto.stock -= cantidad_a_comprar
                  monto_total = producto.calcular_precio_final(producto,es_extranjero)*cantidad_a_comprar
                  self.ventas.append({"producto":producto.nombre,"cantidad_vendida":cantidad_a_comprar,"monto":monto_total,"fecha":time.strftime("%d/%m"),"anio":time.strftime("%Y")})
               else:
                  raise ValueError ("No hay suficiente stock para realizar la venta")      
        if not codigo_valido:
           raise ValueError ("El codigo no corresponde a un producto registrado")      
               

    def valor_ventas_del_dia(self):
        valor_total = 0
        for venta in self.ventas:
            if time.strftime("%d/%m") == venta["fecha"]:
               valor_total += venta["monto"]
        return valor_total      

    def ver_productos(self):
        if not len(self.productos) == 0:
           for producto in self.productos:
            print("codigo:"+str(producto.codigo)+" nombre:"+producto.nombre+" precio:"+str(producto.precio)+" stock:"+str(producto.stock)+" categoria/s:"+producto.ver_categorias())
        else:
            raise ValueError ("No hay productos registrados")  
    
    def hay_stock(self,codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               return producto.stock > 0
        return False

    """ 7.Discontinua "elimina" los productos que no tengan stock """
def descontinuar_productos():
    for producto in productos:
        if producto["stock"] <= 0:
            list.remove(productos,producto)
    

    def calcular_precio_final(self,producto,es_extranjero):
        
        valor_final = 0
        valor_final = producto.precio_final(producto.precio)
        
        if es_extranjero and valor_final > 70:
           return valor_final
        else:
           valor_final = valor_final+(21*valor_final)/100
           return valor_final   

    def contar_categorias(self):
        lista_total_categorias = []
        for producto in self.productos:
            for categoria in producto.categoria:
                if not categoria in lista_total_categorias:
                   lista_total_categorias.append(categoria)
        return len(lista_total_categorias) 


    def descontinuar_productos(self):
        for producto in self.productos:
            if producto.stock <= 0:
               self.productos.remove(producto)


    def ventas_del_anio(self):
        ventas_anio = 0
        for venta in self.ventas:
            if time.strftime("%Y") == venta["anio"]:
               ventas_anio += venta["monto"]
        return ventas_anio

    def productos_mas_vendidos(self,cantidad_de_productos):
        productos_vendidos = []
        mas_vendidos = []
        for venta in self.ventas:
            productos_vendidos.append(venta["producto"])
        
            mas_vendidos = Counter(productos_vendidos)
            print ("",mas_vendidos.most_common(cantidad_de_productos))

    def actualizar_precios_por_categoria(self,categoria,porcentaje):
        for producto in self.productos:
            for categoria in producto.categoria:
                if categoria.lower() == categoria:
                   producto.precio += (producto.precio*porcentaje)/100
               
 
    def gastos_del_dia(self):
        return self.gasto_del_dia

    def ganancia_diaria(self):
        return self.valor_ventas_del_dia() - self.gastos_del_dia()    


class SucursalVirtual:
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.gasto_del_dia = 10000
        self.gasto_variable = 1   
    

    def ver_productos(self):
        if not len(self.productos) == 0:
           for producto in self.productos:
            print("codigo:"+str(producto.codigo)+" nombre:"+producto.nombre+" precio:"+str(producto.precio)+" stock:"+str(producto.stock)+" categoria/s:"+producto.ver_categorias())
        else:
            raise ValueError ("No hay productos registrados")    
               
    def registrar_producto(self,nuevo_producto):
        largo_inicial = len(self.productos)
        self.productos.add(nuevo_producto)
        if len(self.productos) == largo_inicial:
            raise ValueError ("El producto ya se encuentra registrado")

    def recargar_stock(self,codigo_producto,cantidad_a_agregar):
        codigo_valido = False
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               codigo_valido = True
               producto.stock += cantidad_a_agregar
        if not codigo_valido:
            raise ValueError ("El codigo no corresponde a un producto registrado")  
                  

    def hay_stock(self,codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               return producto.stock > 0
        return False

    """ 7.Discontinua "elimina" los productos que no tengan stock """
def descontinuar_productos():
    for producto in productos:
        if producto["stock"] <= 0:
            list.remove(productos,producto)
    
        

    def calcular_precio_final(self,producto,es_extranjero):
        
        valor_final = 0
        valor_final = producto.precio_final(producto.precio)
        
        if es_extranjero and valor_final > 70:
           return valor_final
        else:
           valor_final = valor_final+(21*valor_final)/100
           return valor_final   


    def contar_categorias(self):
        lista_total_categorias = []
        for producto in self.productos:
            for categoria in producto.categoria:
                if not categoria in lista_total_categorias:
                   lista_total_categorias.append(categoria)
        return len(lista_total_categorias) 





    def realizar_compra(self,codigo_producto,cantidad_a_comprar,es_extranjero):
        codigo_valido = False
        for producto in self.productos:
            if codigo_producto == producto.codigo:
               codigo_valido = Tru
               if self.hay_stock(codigo_producto) and  producto.stock > cantidad_a_comprar:
                  producto.stock -= cantidad_a_comprar
                  monto_total = producto.calcular_precio_final(producto,es_extranjero)*cantidad_a_comprar
                  self.ventas.append({"producto":producto.nombre,"cantidad_vendida":cantidad_a_comprar,"monto":monto_total,"fecha":time.strftime("%d/%m"),"anio":time.strftime("%Y")})
               else:
                  raise ValueError ("No hay suficiente stock para realizar la venta")      
        if not codigo_valido:
           raise ValueError ("El codigo no corresponde a un producto registrado")

    def descontinuar_productos(self):
        for producto in self.productos:
            if producto.stock <= 0:
               self.productos.remove(producto)

    def valor_ventas_del_dia(self):
        valor_total = 0
        for venta in self.ventas:
            if time.strftime("%d/%m") == venta["fecha"]:
               valor_total += venta["monto"]
        return valor_total

    
    def ventas_del_anio(self):
        ventas_anio = 0
        for venta in self.ventas:
            if time.strftime("%Y") == venta["anio"]:
               ventas_anio += venta["monto"]
        return ventas_anio


    def productos_mas_vendidos(self,cantidad_de_productos):
        productos_vendidos = []
        mas_vendidos = []
        for venta in self.ventas:
            productos_vendidos.append(venta["producto"])
        
            mas_vendidos = Counter(productos_vendidos)
            print ("",mas_vendidos.most_common(cantidad_de_productos))


        mas_vendidos = Counter(productos_vendidos)
        print(" ", mas_vendidos.most_comon(cantidad_de_productos))        

    def actualizar_precios_por_categoria(self,categoria,porcentaje):
        for producto in self.productos:
            for categoria in producto.categoria:
                if categoria.lower() == categoria:
                   producto.precio += (producto.precio*porcentaje)/100

    def gastos_del_dia(self):      #Si total de las ventas es mayor a 100
        if len(self.ventas) > 100: #gastos del dia sera el total de las ventas por el gasto_variable
            return len(self.ventas)*self.gasto_variable

    def ganancia_diaria(self):
        return self.valor_ventas_del_dia() - self.gastos_del_dia()        

    def modificar_gasto_variable(self,nuevo_valor):
        self.gasto_variable = nuevo_valor

    
""" 11. actualizar_precios_por_categoria: toma una categoría y un porcentaje,
y actualiza según ese porcentaje el precio de todos los productos que 
tengan esa categoría. La búsqueda de categoría en este procedimiento no
debe ser exacta: por ejemplo tanto si se pasa como 
argumento "REMERA", " REMERA" o "Remera", deben actualizarse los productos de la categoría "remera".
"""            
"""
def actualizar_precios_por_categoria(categoria, porcentaje):
    for producto in productos:
        if producto["categoria"] == categoria.lower():
            producto["precio"] += producto["precio"] * porcentaje / 100
"""            
            
            
# Reiniciar productos de la tienda
def reiniciar_productos_de_la_tienda():
    productos.clear()
    
# Reiniciar ventas de la tienda 
def reiniciar_ventas_de_la_tienda():
    ventas.clear()            
            
# memoria para dos productos cargados

def lista_de_stock_con_dos_productos():
    reiniciar_productos_de_la_tienda()
    reiniciar_ventas_de_la_tienda()
    registrar_producto(jean_talle_38)
    jean_talle_38[" stock"] = 0
    registrar_producto(buzo_talle_s)
    buzo_talle_s["stock"] = 0
    recargar_stock(200, 50)
    recargar_stock(100, 50)
