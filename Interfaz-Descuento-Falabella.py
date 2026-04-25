"""
Acaban de obtener su primer empleo en el retail Falabella

y le solicitan realizar un programa en Python que entregue los descuentos a los clientes

iniciamos solicitando a los clientes el numero de rut

el cual debe validar los 8 dígitos de el mismo

en una casilla posterior validar el código de verificación

posteriormente solicitar el nombre de el cliente

el monto de la compra, para saber si/no obtiene el descuento

toda compra menor a 10.000 no obtiene descuento

toda compra mayor a 10.001 hasta 50.000 obtiene un 10% de descuento

toda compra mayor a 50.000 obtiene un 20% de descuento

que debería calcular el programa

monto de descuento

total a pagar

mostrar en pantalla tipo boleta el numero rut del usuario, nombre, monto de la compra y valor final

"""
# Mensaje de bienvenida;

print("*****Bienvenido a Falabella*****");  

# Intenta;

try: 

  # Definimos SolicitaRut como un entero;
  
  solicitaRut = int(input("Por, favor digite su rut (sin digito verificador): "));  

  #  Si el rut es mayor o igual a 10000000 y menor o igual a 99999999, entonces es un rut valido;
  
  if 10000000 <= solicitaRut <= 99999999: 

    # Mensaje de validacion de rut;

    print("¡Rut valido!");  

    # Definimos numeroVerificacion como un entero;

    numeroVerificacion = int (input("Por, favor digite su numero verificador, si termina en k reemplacela por un 0: ")); 

    # Si el numero de verificacion es mayor o igual a 0 y menor o igual a 9, entonces es un numero de verificacion valido; 
    
    if numeroVerificacion >= 0 or numeroVerificacion <= 9:

      # Definimos nombre como un string;

      nombre = str(input("Por, digite su nombre: ")); 

      # Definimos montoCompra como un entero;

      montoCompra = int(input("Por, favor digite el monto de su compra: "));  

      # Definimos las condiciones para aplicar el descuento;

      if montoCompra <= 100000:

        # Mensaje de aviso de no aplicacion de descuento;

        print("¡Lo sentimos, usted no aplica para el descuento!"); 

        # Boleta de compra sin descuento;

        print(f"***** rut: {solicitaRut}, nombre: {nombre}, Su total es de: ${montoCompra} *****");  
      
      # Condicion para aplicar el descuento del 10%;
      
      if montoCompra > 10001 and montoCompra <= 500000:

        # Mensaje de aviso de aplicacion del 10%;

        print("¡Felicidades, usted aplica para un descuento del 10%"); 

        # Calculo del descuento del 10%;
      
        descuento = montoCompra * 0.10;

        # Definimos el monto final de la compra con el descuento aplicado;

        montoFinal = montoCompra - descuento; 

        # Mensaje de informacion del descuento;

        print(f"Su descuento es de: $", descuento); 

        # Boleta de compra con descuento del 10%;

        print(f"***** rut: {solicitaRut}, nombre: {nombre}, Su total es de: ${montoFinal} *****"); 
        
      # Condicion para aplicar el descuento del 20%;
  
      if montoCompra > 50001:

        # Mensaje de aviso de aplicacion del 20%;

        print("¡Felicidades, usted aplica para un descuento del 20%");  

        # Calculo del descuento del 20%;
  
        descuento = montoCompra * 0.20; 

        # Definimos el monto final de la compra con el descuento aplicado;
  
        montoFinal = montoCompra - descuento; 

        # Mensaje de informacion del descuento;
  
        print(f"Su descuento es de: $", descuento); 

        # Boleta de compra con descuento del 20%;

        print(f"***** rut: {solicitaRut}, nombre: {nombre}, Su total es de: ${montoFinal} *****"); 
  
  # Si el rut no es mayor o igual a 10000000 y menor o igual a 99999999, haz lo siguiente;
  
  else:

    # Mensaje de error de rut invalido;

    print("¡ERROR! recuerde que el rut debe tener exactamente 8 dígitos."); 

# Se captura el error de validacion del numero verificador; 

except ValueError: 

  # Mensaje de error de numero verificador invalido;
  
  print("¡ERROR! recuerde reemplazar la k por un 0"); 

# Finalmente haz lo siguiente;

finally:

  # Mensaje de despedida;

  print("Gracias por su visita, vuelva pronto a Falabella."); 