# Para que el bucle solo se repita 1 vez

for i in range (1):

  # Ciclo en True para que no se salga si es que no se elije la opcion n°8; 
  
  while True:

    # Intenta lo siguiente;
    
    try:

      # Creacion de function con parametros;
      
      def calculo_Promedio(nota1, nota2, nota3, nota4, nota5, cantidad):

        # Valor de retorno;
        
        return (nota1 + nota2 + nota3 + nota4 + nota5) / cantidad; 

  # Mensaje inicial;  

      print("\n******Bienvenido a DuocUC Docente******"); 
      
      # Aca se pide ingresar la nota, para que se pueda consultar mas adelante;
      
      notaM = float(input("Ingresa la calificacion de Nivelacion matematica: ")); 
      notaF = float(input("Ingresa la calificacion de Fundamentos de programacion: ")); 
      notaD = float(input("Ingresa la calificacion de Devops: "));  
      notaIA = float(input("Ingresa la calificacion de IA: ")); 
      notaC = float(input("Ingresa la calificacion de Ciencia de datos: ")); 

      # Si, no se cumple la condicion imprime el mensaje de error y corta el programa;

      if not (1 <= notaM <= 7.0 and 1 <= notaF <= 7.0 and 1 <= notaD <= 7.0 and 1 <= notaIA <= 7.0 and 1 <= notaC <= 7.0):

        print("¡ERROR!, Las notas deben ser entre 1.0 y 7.0"); 

        break; 

      # Menu de interaccion con el usuario;
  
      print("\nAsignaturas disponibles:"); 
  
      print("\n1- Nivelacion matematica"); 
      print("2- Fundamentos de programacion"); 
      print("3- Devops");  
      print("4- IA"); 
      print("5- Ciencia de datos"); 

      # Aca preferi separar parte de el menu para que se entendiera mejor;

      print("\n*****Opciones*****"); 
      print("6- Consultar calificacion"); 
      print("7- Calcular promedio");  
      print("8- Salir");  
   
   # Seleccion de asignatura

      opcion_Asignatura = int(input("\n Selecciona una opcion: ")); 

      # Seleccion de opcion; 
  
      if opcion_Asignatura == 6:
    
        opcion_Asignatura = int(input("Selecciona la asignatura a consultar: ")); 

        # Para que el bucle solo se repita 1 vez; 
      
        for i in range (1): 
            
            # Seleccion de numero de indice de las asignaturas, para consultarlas de forma individual;
    
            if opcion_Asignatura == 1:

              # Mensaje con la nota de forma individual;
      
              print(f"La calificacion de Nivelacion matematica es: {notaM}"); 

            # Aca comenzamos a usar elif, para no abusar de if, ya que eso es una mala practica;
              
            elif opcion_Asignatura == 2:
              
              print(f"La calificacion de Fundamentos de programacion es: {notaF}");  
              
            elif opcion_Asignatura == 3:
              
              print(f"La calificacion de Devops es: {notaD}");  
              
            elif opcion_Asignatura == 4:
              
              print(f"La calificacion de IA es:  {notaIA}");  
              
            elif opcion_Asignatura == 5:
              
               print(f"La calificacion de Ciencia de datos es: {notaC}"); 

            # Finalmente en caso contrario, se avisa al usuario que no puede ver calificaciones de asignaturas inexistentes;
    
            else: print("¡ERROR!, Debes ingresar un numero de asignatura valido"); 
      
      elif opcion_Asignatura == 7:

       # Se imprime el promedio y se finaliza el programa, se ocupa round junto a la function para que redondee la cifra en solo 2 digitos "4.6" y no "4.68";

        print("El promedio de el alumno es:", round(calculo_Promedio(notaM, notaF, notaD, notaIA, notaC, 5), 1)); 

        break;  

      # Opcion de salida de el programa, con su respectivo mensaje y finalizacion de este;
      
      elif opcion_Asignatura == 8:
      
        print("¡Adios, que tenga buena jornada!")
        
        break;  
      
      # Si no, imprime mensaje para comunicarle las opciones disponibles;
      
      else: print("¡ERROR!, Selecciona la OPCION 6, 7 o 8"); 
      
# Mensaje de error en caso de elegir una opcion invalida;  
  
    except ValueError: print("¡ERRROR!, selecciona una opcion valida"); 

    # Finalmente, mensaje de aviso de termino de programa;  

    finally: print("\n******Finalizando programa******"); 