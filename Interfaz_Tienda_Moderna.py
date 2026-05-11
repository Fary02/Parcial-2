# Mensaje de bienvenida;

print("*****Hola, bienvenido a nuestro sistema de ventas 2.0*****");  

# Inicio de bucle;

for i in range (1):

  while True:

    try:

      # Se almacenan y piden datos; 

      nombre = str(input("Por, favor digite su nombre: ")); 

      rut = (input("Por, favor digite los 8 primeros digitos de su rut: "));  

      valorProducto = 500;  

      producto = (print(f"El valor por unidad del superocho es de: {valorProducto}CLP")); 

      iva = str(print("El iva de cada unidad es de el 19 %"));  

      cantidad_Producto = int(input("Seleccione la cantidad a llevar (limitado a 10 por persona): ")); 

      filtro_rut = len(rut); 

      # Si las condicones se cumplen: ; 

      if filtro_rut == 8 and nombre.isalpha:
      
        subtotal = cantidad_Producto * valorProducto;  

        valorIva = subtotal * 0.19; 

        totalFinal = subtotal + valorIva; 

        print("******Boleta******"); 
        print(f"Su nombre: {nombre}");  
        print(f"Su rut: {rut}");  
        print(f"El valor de el producto es de: ${valorProducto} CLP"); 
        print(f"Cantidad: {cantidad_Producto}");  
        print(f"Su total es de: {totalFinal}"); 
        print(f"El iva de esta compra es de: {valorIva}");  
        print("******Muchas gracias por su compra******");  

        # Termino de ciclo;   

        break;  

      # En caso contrario;

      else:
        
        print("¡ERROR!, El menu se repetira hasta que elija la opcion correcta") 


    # Al colocar finally el ciclo se finaliza con un mensaje se efectue la compra o no

    # Por lo que decidi dejar esta excepcion, a pesar de que el else cumple la misma funcion
      
    except:

      print("¡ERROR!, Ingrese un valor correcto");  