"""
Enunciado

Una empresa de arriendo de maquinaria necesita un sistema que calcule el costo total del servicio.

El programa debe solicitar:

    Nombre del cliente (mínimo 3 caracteres)
    Teléfono (8 a 9 dígitos)
    Horas de trabajo
    Tipo de equipo
    Cantidad de horas por equipo

Equipos disponibles:

   Equipo

Precio por hora

    Excavadora $200.000
    Grúa  $250.000
    Mezcladora $150.000
    
El sistema debe:

    Validar datos de entrada
    Permitir seleccionar al menos 1 equipo
    Calcular el total

Salida esperada:

Mostrar:

    Nombre
    Teléfono
    Total, de horas
    Detalle de equipos
    Precio total
    
    """


# Mensaje bienvenida;

print ("****** Bienvenido a maquinarias F.A ******");   

# Solicitar nombre;

nombreCliente = str(input("ingrese su nombre (minimo 3 caracteres alfabeticos): ")); 

condicionNombre = len(nombreCliente);   

# Validamos que el nombre cumpla las condiciones;

if nombreCliente.isalpha() == True and condicionNombre >= 3:

    # Solicitar telefono;

    telefonoCliente = str(input("Ingrese su numero de telefono (8 a 9 digitos): ")); 

    # Validamos que el telefono cumpla las condiciones;

    if telefonoCliente.isdigit() == True and len(telefonoCliente) >= 8 and len(telefonoCliente) <= 9:   

         # Solicitar horas de trabajo; 

            horasTrabajo = int(input("Ingrese las horas de trabajo: ")); 

            # Validamos que las horas de trabajo sean mayores a 0;

            if horasTrabajo > 0:
                  
                  # Solicitamos tipo de equipo;

                    tipoEquipo = str(input("Ingrese el tipo de equipo (Excavadora, Grua o Mezcladora): ")); 

                    # Validamos que el tipo de equipo sea correcto;

                    if tipoEquipo == "Excavadora" or tipoEquipo == "Grua" or tipoEquipo == "Mezcladora":
                           
                           # Solicitamos cantidad de horas por equipo;

                           cantidadHorasEquipo = int(input("Ingrese la cantidad de horas por equipo: "));   

                            # Validamos que la cantidad de horas por equipo sea mayor a 0;

                           if cantidadHorasEquipo > 0:
                                  
                                  # Calculamos el total;

                                  if tipoEquipo == "Excavadora":
                                         
                                        precioHora = 200000;    

                                  elif tipoEquipo == "Grua":

                                        precioHora = 250000; 

                                  else:

                                        precioHora = 150000; 
                    
                    # Si el tipo de equipo no es valido, mostramos mensaje de error;

                    else:

                      print("Tipo de equipo no valido, por favor ingrese Excavadora, Grua o Mezcladora"); 

                    total = horasTrabajo * precioHora * cantidadHorasEquipo; 

                    # Mostramos boleta;
                    
                    print(f"Nombre: {nombreCliente}"); 

                    print(f"Telefono: {telefonoCliente}"); 

                    print(f"Total de horas: {horasTrabajo}"); 

                    print(f"Detalle de equipos: {tipoEquipo} - {cantidadHorasEquipo} horas"); 

                    print(f"Precio total: ${total}");   

                   # Mensaje de Agradecimiento;

                    print(f"Gracias por su preferencia {nombreCliente}"); 
            
            # Si las horas de trabajo no son validas, mostramos mensaje de error;

            else:

              print("Horas de trabajo no validas, por favor ingrese un numero mayor a 0");  

    # Si el telefono no es valido, mostramos mensaje de error; 

    else:

      print("Telefono no valido, por favor ingrese un numero de telefono con 8 a 9 digitos"); 

# Si el nombre no es valido, mostramos mensaje de error;

else:

  print("Nombre no valido, por favor ingrese un nombre con minimo 3 caracteres alfabeticos"); 

# TIEMPO DE REALIZACION SUPERIOR A LOS 25 MINUTOS CON 41 SEGUNDOS RESTANTES DEL ANTERIOR EJERCICIO; 