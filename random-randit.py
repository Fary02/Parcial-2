# Importacion de libreria;

from random import randint

# Se solicita ingreso de datos;

num1 = int(input("Ingresa el limite inferior: "));  

num2 = int(input("Ingresa el limite superior: "));  

# Se valida que se cumpla la condicion;

while num1 >= num2:
  
  print("¡ERROR!, el limite inferior debe ser menor al superior");  
  
  num1 = int(input("Ingresa el limite inferior: "));  

  num2 = int(input("Ingresa el limite superior: "));  
  
  
# Se genera numero aleatorio;
  
numeroRandom = randint(num1, num2); 

# Se ajusta en multiplo de 3;

reajuste = (numeroRandom // 3) * 3; 

# Se valida el reajuste;

if reajuste < num1:
  
  reajuste = num1
  
# Primer intento de usuario;
  
  intento1 = int(input("Intenta adivinar: "));  

  if intento1 == reajuste:
  
    print("Felicidades, adivinaste en tu primer intento");  
  
  else:
  
    if intento1 < reajuste:
    
      print("El numero es mayor");  
    
    else: 
    
      print("El numero es menor");  
    
# Segundo intento de usuario;

  intento2 = int(input("Intenta adivinar nuevamente: ")); 
  
  if intento2 == reajuste:
  
    print("Felicidades, adivinaste en tu segundo intento");  
  
  else:
  
    if intento2 < reajuste:
    
      print("El numero es mayor");  
    
    else: 
    
      print("El numero es menor"); 
      
  # Pista para el usuario;
    
  print("Te dare una pista: "); 
    
  dist1 = abs (reajuste - intento1); 
    
  dist2 = abs (reajuste - intento2);  
  
  if dist1 < dist2:
    
    print(f"El numero que buscas es mas cerca de {intento1} que de {intento2}"); 
    
  elif dist2 < dist1:
    
    print(f"El numero que buscas es mas cerca de {intento2} que de {intento1}");  
    
  else:
    
    print("Ambos intentos estan a la misma distancia");  
    
  # Tercer intento de usuario;
  
  intento3 = int(input("Intenta la ultima vez: ")); 
  
  if intento3 == reajuste:
    
    print("Felicidades, adivinaste en tu tercer intento");  
    
  else:
    
    print(f"Lamentamos lo sucedido, el numero era {reajuste}"); 