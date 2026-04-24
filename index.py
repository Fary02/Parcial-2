print("*****Bienvenido a Falabella*****");  



try: 
  
  solicitaRut = [int(input("Por, favor digite su rut si termina en k reemplacela por un 0: "))]; 
  
  limiteRut = [8];  
  
  


except ValueError: 
  
  print("¡ERROR! recuerde reemplazar la k por un 0"); 
  
if solicitaRut == limiteRut.count(8):
  
  numeroVerificacion = [int (input("Por, favor digite su numero verificador: "))];  
  

