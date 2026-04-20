"""

# Se define un array con numeros;

numero = [1,2,3,4,5]; 

# Se agrega un numero al array;

numero.append(6); 

# Se imprime junto a "bool" para que arroje True;

print(bool(numero));  

# Se imprime la posicion de el primer y ante-penultimo numero de el array;

print(numero[0:4]); 


# Tupla;

colores = ("amarillo","rojo","azul");  


print(colores[1]);  

personas = {
  
  "Juan": 25,
  "Maria": 20,
  "Carlos": 19
  
  };  

print("Carlos tiene:", personas["Carlos"], "Años"); 

"""

# Functions;

def saludo(nombre):
  
  # return f"¡Hola!, {nombre}" para formatear, no es necesario el parentesis
  
  return "¡Hola!", nombre + "!";  

# mensaje = saludo("Estudiante: "); 

mensaje = saludo("Bienvenido: "); 

nombre = input("Dime tu nombre: "); 

print(f"{mensaje}, {nombre}"); 
