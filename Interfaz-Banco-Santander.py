"""

Estimado estudiante usted a sido seleccionado para realizar la interfaz de usuario de los cajeros automaticos del grupo santander

El programa debe solicitar al usuario:

numero de rut

el cual debe ser validado con su numero de verificacion (numero despues de el guion)

posteriormente a eso

el usuario debe introducir su clave

que no deberia ser ni mayor ni menor a 10 digitos

"""

# Mensaje de bienvenida;

print("----- Bienvenido al cajero automatico del Banco Santander -----"); 


# Intentamos;

try:

  # Solicitamos al usuario su numero de rut y numero de verificacion;

  numero_rut = int(input("Ingrese su numero de rut sin puntos ni guion, si termina en k reemplacelo por un 0: "));  

  numero_verificador = int(input("ingrese su numero de verificacion, si es k reemplacelo por un 0:"));  

  # Validamos el numero de rut y numero de verificacion;

  if numero_verificador >= 0 and numero_verificador <= 9 or numero_rut >= 100000000 and numero_rut <= 999999999:

    print("Rut valido"); 
  
  # De lo contrario, lanzamos un error y mostramos un mensaje de error;
  
  else:

    raise ValueError
  
    print("Error ingrese un valor valido"); 
  
  # Solicitamos la clave;

  clave = int(input("Ingrese su clave de 10 digitos: ")); 

  # Validamos la clave;

  if clave >= 0000000000 or clave <= 9999999999:

    print("----- Acceso concedido -----");  

  else:

    # De lo contrario, lanzamos un error y mostramos un mensaje de error;

    raise ValueError
  
    print("Error ingrese un valor valido"); 
    
# Finalmente, mostramos un mensaje de despedida;

finally:
  
  print("----- Gracias por usar el cajero automatico del Banco Santander -----"); 