# Definimos op para que se inicia el bucle;

op = 1; 

# Intenta Esto;

try:

  # Si op es igual a 1 haz lo siguiente;

  while op == 1:

    # Definimos la opcion de menu;

    Menu = int(input("Por, favor digita la opcion 3 para acceder al menu: "))

    # Si se cumple la condicion haz lo siguiente; 

    if Menu == 3:

      # Definimos op ahora como 3;

      op = 3; 

      # Si la condicion es correcta haz lo siguiente;

      while op == 3:

        # Solicitud de ingreso de datos;  

        DatoNumerico = int(input("Por, favor ingresa solo numeros: "));  

        DatoTexto = input("Ahora por favor, ingresa tu nombre:  "); 

        # Si DatoNumerico y DatoTexto son del tipo correspondiente haz lo siguiente

        if isinstance(DatoNumerico, int) and isinstance(DatoTexto, str):

          # Mensajes finales de condicion;  

          print("Perfecto muchas gracias"); 

          print(f"Tus datos fueron los siguientes: {DatoNumerico} y {DatoTexto}") 

          # Cierre de ciclo para que no se repita si se cumplen las condiciones;  
        
          break;  

# Si existe un error de valor haz lo siguiente; 

except ValueError: print("¡ERROR!, Inserta los tipos de datos correctos"); 

# Finalmente haz esto;

finally: print("*****Cerrando programa*****");  