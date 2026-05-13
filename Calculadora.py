# Se define la function y se asigna parametros; 

def suma (a,b):
  
  # Se retornan los parametros con su operacion;  

    return a + b; 

def resta (a,b):

    return a - b; 

def multiplicacion (a,b):

    return a * b; 
  
def division (a,b):
  
  # En caso de que se intente dividir por 0;

  if b == 0:
    
    return "¡ERROR!, no se puede dividir por 0"; 
  
  # Si no se divide por 0 retorna los parametros con su operacion; 
  
  return a / b; 

# Menu de calculadora;  

print("******Calculadora******"); 

# Solicitud de ingreso de datos;  

num1 = float(input("Ingresa el primer numero: ")); 

num2 = float(input("Ingresa el segundo numero: ")); 

# Menu de opciones; 

print("\n1. Suma"); 

print("2. Resta"); 

print("3. Multiplicacion"); 

print("4. Division"); 

# Solicitud de ingreso de opcion; 

opcion = input("Ingresa una opcion: "); 

# Si la opcion es la elegida; 

if opcion == "1":
  
  # Imprime el resultado;
  
  print("Resultado:", suma(num1, num2));  
  
elif opcion == "2":
  
  print("Resultado:", resta(num1, num2)); 
  
elif opcion == "3":
  
  print("Resultado:", multiplicacion(num1, num2)); 
  
elif opcion == "4":
  
  print("Resultado:", division(num1, num2)); 
  
# Si ninguna opcion se cumple, imprime el mensaje siguiente;
  
else: 
  
   print("Opcion invalida"); 