"""
Una tienda de retail necesita un programa que permita calcular el descuento aplicado a una compra.

El sistema debe:

Solicitar:

    Nombre del cliente (mínimo 3 caracteres)
    Monto de la compra (número entero positivo)

Validaciones:

    Nombre válido
    Monto mayor o igual a 0

Reglas de negocio:

   Monto 
   
   Descuento < 10.000 = 0%

    10.000 - 50.000 = 10%
  
    > 50.000 = 20%
  
"""

# Mensaje de bienvenida;

print("****** Bienvenido a Paribella ******");  

# Solicitar nombre;

nombreCliente = str(input("ingrese su nombre (minimo 3 caracteres alfabeticos): ")); 

condicionNombre = len(nombreCliente); 

# Validamos que el nombre cumpla las condiciones;

if nombreCliente.isalpha() == True and condicionNombre >= 3:

  # Mensaje de bienvenida;

  print(f"Hola {nombreCliente}, bienvenido"); 

  # Solicitar monto de compra;

  montoCompra = int(input("Ingrese el monto de su compra: "));  

  # Validamos que el monto de compra sea mayor o igual a 0;

  if montoCompra >= 0:

    # Calculamos el descuento;

    if montoCompra < 10000:

      descuento = 0;  

    elif montoCompra >= 10000 and montoCompra <= 50000:

      descuento = 0.10; 

    else:

      descuento = 0.20; 

  # Calculamos el monto final;

  montoFinal = montoCompra - (montoCompra * descuento); 

  # Mostramos boleta; 

  print("****** Boleta de Compra ******");  

  print(f"Cliente: {nombreCliente}"); 

  print(f"Monto de compra: {montoCompra}"); 

  print(f"Descuento aplicado: {descuento * 100}%"); 

  print(f"Monto final: {montoFinal}"); 

  # Mensaje de despedida;

  print(f"Gracias tu compra {nombreCliente}. ¡Vuelve pronto!");  

# Mensaje de error para nombre no válido;

else:  

  print("ERROR: El nombre debe contener al menos 3 caracteres alfabeticos.");  

# TIEMPO DE REALIZACION: 19 MINUTOS CON 59 SEGUNDOS, DE 45 MINUTOS ASIGNADOS. ;