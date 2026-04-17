"""
login de banco estado

el cual le permitirá al usuario intentar un máximo de ingreso de 5 veces,

de no lograrlo debe mostrar en pantalla el siguiente mensaje al usuario:

"Por, favor comuníquese a nuestro call center"

de introducir correctamente las credenciales debe mostrar un mensaje de bienvenida o el nombre de el usuario

"""

# Mensaje de bienvenida al usuario;

print("---- Bienvenido a Banco Estado ----");  

# Numero de intentos para ingresar;

intento = 5; 

# Ciclo para ingresar user y password;

while intento > 0:

  # Solicitud de ingreso de datos al usuario;
  
  usuario = input("Por favor, ingrese su nombre de usuario: "); 
  password = input("Por favor, ingrese su contraseña: ");  

  # Validación de datos ingresados;
  
  if password == "1234" and usuario == "Fary":
    
    print(f"¡Bienvenido {usuario}!"); 

    # Salida del ciclo;
    
    break

  # En caso de que los datos ingresados sean incorrectos, se resta un intento al contador;
    
  else:
  
    intento  -= 1; 
  
  print(f"Intento fallido. INTENTELO DE NUEVO. Le quedan {intento} intentos."); 

  # En caso de que el usuario se quede sin intentos, se muestra un mensaje de error y se le indica que se comunique con el call center para obtener ayuda;
  
  if intento == 0:
    
    print("Por, favor comuníquese a nuestro call center: 600 200 7000 para obtener ayuda."); 
