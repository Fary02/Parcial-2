# Se declara la variable;

suma = 0; 

# Se llama al bucle;

for i in range (5):
  
  while True:
    
    try:
      
      numero = float(input(f"Ingrese el numero {i + 1}: ")); 
      
      suma = suma + numero; 
      
      break;  
    
    except: 
      
      print("¡ERROR!, Debe ingresar un numero");  
      
print("La suma total es: ", suma);  