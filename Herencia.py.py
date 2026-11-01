#HERENCIA
class producto:
    def __init__(self ,nombre,stock,precio):
        self.nombre=nombre
        self.stock=stock
        self.precio=precio

class legumbres(producto):
    def __init__(self,nombre,stock,precio):
        super().__init__(nombre,stock,precio)

class lecho(producto):
    def __init__(self,nombre,stock,precio):
        super().__init__(nombre,stock,precio)



producto_1=producto("SALSA",10,10.00)
producto_2=producto("HARINA",200,23.00)
producto_3=producto("CARNE",1000,40.00)

print(f'El producto es {producto_1.nombre,producto_1.precio,producto_1.stock}')
print(f'El producto es {producto_2.nombre,producto_2.precio,producto_2.stock}')
print(f'El producto es {producto_3.nombre,producto_3.precio,producto_3.stock}')


