"""
Contexto:

Eres el encargado de una tienda de arte.

Tienes una tupla fija de colores_base y una lista de stock de pinceles.

Debes crear una función que reciba un nombre de color y una cantidad,

devuelva un mensaje formateado y actualice un diccionario de ventas

donde se registre la edad del comprador y el producto adquirido.

"""

# Bienvenida y solicitud de datos del cliente;

nombre = input("Bienvenido a Fary's Art Store, por favor ingrese su nombre: "); 

edad = input("Por favor ingrese su edad: ");  

# Array de colores y stock;

colores = ["morado", "carmesi", "verde agua", "negro", "rosa pastel"];  

stock = [20,15,5,25,10];  

# Creacion de Function y  V. seleccion de color, cantidad, mensaje con stock y productos disponibles;

print("Actualmente tenemos pinceles de color:", colores); 

print("Y su stock:", stock);  

seleccion_de_color = input("Escriba el color que desea llevar: "); 

seleccion_cantidad = input("Escriba la cantidad que desea llevar: "); 

def venta_pincel():  
  
  return "usted ha seleccionado el color:", seleccion_de_color, "y la cantidad:", seleccion_cantidad; 

def resumen_cliente_():

  return "Estimado:", nombre, "con", edad,"años", venta_pincel();  


# Creacion de condicion para validar seleccion;

if seleccion_de_color in colores or seleccion_cantidad in stock:

  
  print(resumen_cliente_());  

  print("Gracias por su compra, vuelva pronto!"); 

else:
  print("No tenemos disponible esa cantidad en ese color.")