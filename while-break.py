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
