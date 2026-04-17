# while

# break (para cerrar)


intento = 3; 

while intento > 0:
  
  password = input("Dime tu clave: ");  
  
  if password == "1234":
    
    print("¡Bienvenido!");  
    
  break

else:
  
  intento  -= 1; 
  
  print(f"Intento fallido. Te falta, {intento}"); 
  
  if intento == 0:
    
    print("Acceso denegado"); 
     
    
    #Ejercicio Lunes:
    
    """
    Estimado programador usted a sido seleccionado para realizar el nuevo sistema de login de banco estado
    el cual le permitirá al usuario intentar un máximo de ingreso de 5 veces, de no lograrlo debe mostrar en pantalla el siguiente mensaje al usuario:
    "Por, favor comuníquese a nuestro call center", de introducir correctamente las credenciales debe mostrar un mensaje de bienvenida o el nombre de el usuario
    
    """