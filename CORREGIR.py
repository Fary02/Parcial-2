# Mensaje de bienvenida;

print("----- Bienvenido a Banco Falabella -----");  

# Validacion de rut;

while True:
  
  rut = input("Ingresa tu Rut (Sin puntos ni guion): ");  
  
  if rut.isdigit() and len(rut) == 8: 
    
    break
  
  else:
    
    print("El rut, solo debe tener 8 digitos numericos"); 

# Validacion codigo de verificacion;

while True:
  
  dv = input("Ingresa tu digito verificador: ").upper(); 
  
  if len(dv) == 1 and (dv.isdigit()) or dv == "K":
    
    break

  else:
  
    print("Error"); 
    
  # Nombre;
  
  nombre = input("Ingresa tu nombre: ");  
  
  # Valida compra;
  
  while True:
    
    montos = input("Ingresa el monto de la compra: ");  
    
    if montos.isdigit():
      
      monto = int(montos); 
      
      if monto >= 0:
        
        break
      
      else:
        
        print("Error, el monto es negativo."); 
           
    else:
      
      print("Error, Ingresa solo numero");  
      
# Calculo descuento;

if monto < 10000:
  
  descuento = 0; 
   
  porcentaje = 0; 
  
elif monto <= 50000:

  descuento = monto * 0.10; 
  
  porcentaje = 10;  
  
else:
  
  descuento = monto * 0.20; 
  
  porcentaje = 20;  
  
total =  monto - descuento; 

# Boleta;

print("\n-----Boleta-----");  

print(f"Rut: {rut}-{dv}");  

print(f"Nombre: {nombre}"); 

print(f"Monto: {monto}"); 

print(f"Descuento: {descuento}"); 