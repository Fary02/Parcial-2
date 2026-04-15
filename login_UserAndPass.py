"""
realizar un login

duoc uc a contratado su servicio para realizar un login en Python

ese login debe validar el usuario y clave

"""

# Escribimos mensajes iniciales;

login = input("Bienvenido/a, por favor ingrese su usuario: "); 

loginPassword = input("Por favor, digite su password: "); 

# Definimos password;

# al ocupar esta Variable el codigo te acepta aunque no sea exacta debido al tipo

# password = 1234;

# Creamos la sentencia y en caso correcto;

if login == "Fary":
  
  print("Hola Fary, bienvenido"); 
  
  # En caso de contraseña correcta;
  
  if loginPassword == "1234":
    
    print("Contraseña correcta"); 
    
    print("¡¡¡Bienvenido Fary!!!"); 
    
  # En caso contrario a contraseña;
    
  else:
    
    print("Contraseña incorrecta"); 
    
  # En caso contrario a usuario;
  
else:
  
  print("Usuario incorrecto"); 
   