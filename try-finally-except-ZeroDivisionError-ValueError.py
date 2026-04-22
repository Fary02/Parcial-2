# Try (VALIDACION DE ERRORES);

"""
try:
  
  resultado = 10 / 0; 

# Para que no arroje error y se ejecute el programa;
  
except ZeroDivisionError:
  
  print("¡Error!, no debemos dividir entre cero.");  
  
finally:
  
  print("Bloque Finalizado"); 
  
"""
  
try:
  
  num1 = float(input("Por favor, ingresa un numero: "));  
  
  num2 = float(input("Por favor, ingresa un numero: ")); 
  
  
  if num2 == 0:
    
    raise ZeroDivisionError # Lanza el error o provoca el error manual;

    # resultado = num1 / num2;  
    
    # print(f"El resultado de esta division es: {resultado}");  
    
  else: num1 and num2 != ZeroDivisionError # De esta forma podemos hacer que el resultado de la division aparesca siempre y cuando se cumpla la condicion;  
  
  resultado = num1 / num2;  
    
  print(f"El resultado de esta division es: {resultado}");  
     
except  ValueError: # Error de Valor; 
  
  print("¡ERROR! Ingresa un nuevo numero"); 

except ZeroDivisionError: # Error al dividir por 0; 
  
  print("¡Error! No se puede dividir por cero.");  

print("Fin del programa");  