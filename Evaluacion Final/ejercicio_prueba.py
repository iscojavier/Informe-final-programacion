
#?==========================================sanitizar textos==============================================================================#
import re #todo importamos libreria para sanitizar entradas
import hashlib
import os
def sanitizador_num(x): #funcion para sanitizar texto
        if x == '':
            return None
        else:
            numero_sano = re.sub(r'\D', '', x)  # Elimina todo lo que no sea un dígito
            return numero_sano

        
def sanitizador(x): #funcion para sanitizar texto
        if x == '':
            return None #todo si el campo esta vacio devuelve no
        else:
            sano = re.sub(r'[^a-zA-Z\s]', '', x)
            sano = sano.capitalize().strip() #todo la capitalizamos y eliminas espacios vacios
            return sano

def formato_correo(correo):
    template = r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',correo.lower()
    return bool(re.match(template, correo))


def formato_rut(rut):
    template = r'^\d{1,8}-[0-9Kk]$'
    return bool(re.match(template, rut))
    
#?==========================================================================================================================================#
#?==========================hasheo password========================================================================================================#
def hasheo(contraseña, salt=None):
    if salt is None:
        salt = os.urandom(16)  #todo Genera un salt aleatoria de 16 bytes
    else:
        salt = salt.encode('utf-8')
    # Combina la contraseña y la sal antes de hashear
    contraseñaHash = hashlib.sha256(salt + contraseña.encode('utf-8')).hexdigest()
    return contraseñaHash, salt.hex()

def verificacion_Pass(password, stored_password_hash, salt):
    # Recalcula el hash de la contraseña con la misma sal
    new_password_hash = hashlib.sha256(bytes.fromhex(salt) + password.encode('utf-8')).hexdigest()

    return new_password_hash == stored_password_hash

#?=======================================================anonimizacion=========================================================================================================#
def anonimacion_data(data):
    # Sustituir cada carácter por 'X' para anonimizar los datos
    datoAnonimo = '*' * (len(data))
    return datoAnonimo

#?==============================^trabajo hecho para informe^=========================================================================================================#

clientes = {} #*====> lista vacia
usuarios = {}  #*====> lista vacia x2
idcliente = 0 #*=====> contador id cliente
idusuario = 0 #*=====> Contador idusuario

#*LISTO
def menuprincipal(): #?===========> FUNCION QUE IMPRIME EL MENU PRINCIPAL
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")                                   
    print("       1.- (C) INGRESAR         ")
    print("       2.- (R) MOSTRAR          ")
    print("       3.- (U) MODIFICAR        ")
    print("       4.- (D) ELIMINAR         ")
    print("       5.- (E) Salir            ")
    print("================================")
#*LISTO
def menumostrar():  #?==============> FUNCION QUE IMPRIME EL MENU MOSTRAR
    print("================================")
    print("     M E N Ú  M O S T R A R     ")
    print("================================")
    print("       1.- MOSTRAR TODO         ")
    print("       2.- MOSTRAR UNO          ")
    print("       3.- MOSTRAR PARCIAL      ")
    print("       4.- VOLVER               ")
    print("================================")
#TODO PENDIENTE
def ingresardatos(): #!=========> FUNCION QUE SOLICITA LOS DATOS DEL CLIENTE
    print("=================================")
    print("     INGRESAR DATOS CLIENTE      ")
    print("=================================")
    while True:
        run = input("INGRESE RUN : ") #?=============> VALIDAR FORMATO RUT CON FUNCION FORMATO_RUT °
        r = formato_rut(run)
        if r is True:  #*por el pico la validacion            
            nombre=sanitizador(input("INGRESE NOMBRE : ")) #todo=============> sanitizar entrada de texto   °
            apellido=sanitizador(input("INGRESE APELLIDO : "))  #todo=============> sanitizar entrada de texto  ° 
            direccion=sanitizador(input("INGRESE DIRECCION : ")) #todo=============> sanitizar entrada de texto     °
            fono=sanitizador_num(input("INGRESE TELEFONO : "))#todo=============> sanitizar entrada de texto   °
            correo=sanitizador(input("INGRESE CORREO : ")) #todo=============> sanitizar entrada de texto   °
            cr = formato_correo(correo)
            if cr is not False:
            #!necesitamos validar si los campos no son vacios //
                print(nombre,apellido)
                tipos = [
                        #k    #v
                        [101,"Plata"],[102,"Oro"],[103,"Platino"]
                    ]
                while True: #*================> Creamos un bucle
                    print("--------------------------------------------")
                    for tipo in tipos:
                        print(" CODIGO : {} - {}.".format(tipo[0], tipo[1]))
                        print("--------------------------------------------")
                    try:
                        tipo = sanitizador_num(input("Ingrese el codigo del Tipo de Cliente: "))
                        if tipo in [101, 102, 103]:
                            monto = sanitizador_num(input("INGRESE MONTO CREDITO : "))
                            if monto >= 0:
                                global idcliente    
                                idcliente += 1
                                codigo = idcliente
                                deuda = 0
                                cliente = [codigo, run, nombre, apellido, direccion, fono, correo, tipo, monto, deuda]
                                clientes[idcliente] = cliente
                                print('Cliente añaddo')
                                break
                        else:
                            print("Tipo de cliente no válido. Intente nuevamente.")
                    except ValueError:
                        print("Entrada inválida. Intente nuevamente.")
                break
            else:
                print('Formato de rut invalido')
        else:
            print('correo invalido')
#TODO ====================================================================================================================================
#TODO PENDIENTE
def mostrar():    #?===========> FUNCION PARA LLAMAR TODOS LOS MENUS
    while(True):
        menumostrar()
        try: #______evaluamos errores
            op2 = sanitizador_num(input("  INGRESE OPCIÓN : "))
            if op2 == 1: #?OPCION 1
                mostrartodo()
                input("\n\n PRESIONE ENTER PARA CONTINUAR")
            elif op2 == 2: #?OPCION 2
                mostraruno()
            elif op2 == 3: #?OPCION 3
                mostrarparcial()
            elif op2 == 4: #?OPCION 4
                break
            else:   #?OPCION FUERA DEL RANGO
                print("Opción Fuera de Rango")
        except:
            print('Caracter no valido')
#TODO PENDIENTE
def mostrartodo():  #?===========> FUNCION PARA MOSTRAR LOS CLIENTES
    print("=================================")
    print("  MUESTRA DE TODOS LOS CLIENTES  ")
    print("=================================")
    for cliente,dato in clientes.items():
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
#TODO PENDIENTE
def mostraruno(): #?==================> FUNCION PARA MOSTRAR UN DATO DE UN USUARIO
    print("=================================")
    print("   MUESTRA DE DATOS PARTICULAR   ")
    print("=================================")
    op= sanitizador_num(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
    datos = clientes.get(op)
    print(datos)
    print("\n=======================================")
    print("    MUESTRA  DE  DATOS  DEL   CLIENTE   ")
    print("=======================================")
    print(" ID            : {} ".format(datos[0]))
    print(" RUN           : {} ".format(datos[1]))
    print(" NOMBRE        : {} ".format(datos[2]))
    print(" APELLIDO      : {} ".format(datos[3]))
    print(" DIRECCION     : {} ".format(datos[4]))
    print(" FONO          : {} ".format(datos[5]))
    print(" CORREO        : {} ".format(datos[6]))
    print(" TIPO          : {} ".format(datos[9]))
    print(" MONTO CREDITO : {} ".format(datos[7]))
    print(" DEUDA         : {} ".format(datos[8]))
    print("-----------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")
#TODO PENDIENTE
def mostrarparcial(): #?==================> FUUNCION PARA MOSTRAR CIERTA CANTIDAD DE DATOS
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")
    cant = sanitizador_num(input("\nIngrese la Cantidad de Clientes a Mostrar : "))
    
    datos = list(clientes.items())[:cant]
    for cliente,dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[9], dato[7], dato[8]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    sanitizador(input("\n\n PRESIONE ENTER PARA CONTINUAR"))
#TODO PENDIENTE
#validacion de entrada de usuario con un try-except
def modificardatos(): #?==================>FUNCION PARA MODIFICAR AL CLIENTE SELECCIONADO
    listanuevos=[]
    print("===================================")
    print("      MODULO MODIFICAR CLIENTE     ")
    print("===================================")
    mostrartodo()
    try :
            mod = sanitizador_num(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
            datos = clientes.get(mod)
    
    except ValueError :
        print("error , porfavor ingrese un valor entero para el id de su cliente")
        
    try :
        mod = sanitizador_num(input("/n ingrese el id del cliente que desee modificar :  "))
        datos = clientes.get(mod)
        print(" ID         : {} ".format(datos[0]))
        listanuevos.append(datos[0])
        print(" RUN        : {} ".format(datos[1]))
        listanuevos.append(datos[1])

        opm=sanitizador(input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[2])))
        if opm.lower() == "si":
            nombrenuevo=input("INGRESE NOMBRE : ")
            listanuevos.append(nombrenuevo)
        else:
            listanuevos.append(datos[2])
        opm = sanitizador(input("DESEA MODIFICAR EL APELLIDO : {} - [SI/NO] ".format(datos[3])))
        if opm.lower() == "si":
            apellidonuevo= input("INGRESE APELLIDO : ")
            listanuevos.append(apellidonuevo)
        else:
            listanuevos.append(datos[3])
        opm = sanitizador(input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO] ".format(datos[4])))
        if opm.lower() == "si":
            direcnueva = input("INGRESE DIRECCION : ")
            listanuevos.append(direcnueva)
        else:
            listanuevos.append(datos[4])
        opm = sanitizador_num(input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO] ".format(datos[5])))
        if opm.lower() == "si":
            fononuevo= input("INGRESE TELEFONO : ")
            listanuevos.append(fononuevo)
        else:
            listanuevos.append(datos[5])
        opm = sanitizador(input("DESEA MODIFICAR EL CORREO : {} - [SI/NO] ".format(datos[6])))
        if opm.lower() == "si":
            correonuevo = input("INGRESE EL CORREO : ")
            listanuevos.append(correonuevo)
        else:
            listanuevos.append(datos[6])
        opm = sanitizador(input("DESEA MODIFICAR LA DEUDA : {} - [SI/NO] ".format(datos[9])))
        if opm.lower() == "si":
            deudanuevo= sanitizador_num(input("INGRESE DEUDA : "))
            listanuevos.append(deudanuevo)
        else:
            listanuevos.append(datos[9])
        opm = sanitizador(input("DESEA MODIFICAR EL MONTO DE CREDITO : {} - [SI/NO] ".format(datos[8])))
        if opm.lower() == "si":
            montonuevo= sanitizador_num(input("INGRESE MONTO DE CREDITO : "))
            listanuevos.append(montonuevo)
        else:
            listanuevos.append(datos[8])
        opm = sanitizador(input("DESEA MODIFICAR EL TIPO : {} - [SI/NO] ".format(datos[7])))
        if opm.lower() == "si":
            tipos = [
                [101,"Plata"],[102,"Oro"],[103,"Platino"]
            ]
            print("--------------------------------------------")
            for tipo in tipos:
                print(
                    " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
            print("--------------------------------------------")
            
            tiponuevo = sanitizador_num(input("INGRESE EL TIPO : "))
            listanuevos.append(tiponuevo)
        else:
            listanuevos.append(datos[7])
        
        clientes[mod]=listanuevos
    except:
        print('k xuxa')

#TODO PENDIENTE
def eliminardatos():  #?===============> FUNCION PARA ELIMINAR UN CLIENTE
    print("===================================")
    print("      MODULO ELIMINAR CLIENTE      ")
    print("===================================")
    mostrartodo()
    elim = sanitizador_num(input("Ingrese valor de ID del Cliente que desea Eliminar : "))
    del clientes[elim]

#! --------------------------------------
#* LISTO
def menuUsuarios():    #?==================> FUNCION PARA MOSTRAR MENU INICIO DE SESION
    print("================================")
    print("   M E N Ú  U S U A R I O S     ")
    print("================================")
    print("       1.-  INICIAR SESIÓN      ")
    print("       2.-  REGISTRAR USUARIO   ")
    print("       3.-  Salir               ")
    print("================================")
#TODO PENDIENTE
def ingresoUsuarios():    #?==================> FUNCION PARA REGISTRAR EN MENU INICIAR SESION
    print("=======================================")
    print("        INGRESO DE USUARIO             ")
    print("=======================================")
    while True:
        try: 
                username = sanitizador(input( "INGRESE NOMBRE DE USUARIO:  "))
                if username is not None:
                    clave = sanitizador(input( "INGRESE PASSWORD         : "))
                    if clave is not None:
                        #todo======================================================
                        claveHash, salt = hasheo(clave)
                        #todo==============================================================
                        nombre = sanitizador(input(   "INGRESE NOMBRE           : "))
                        if nombre is not None:
                            apellidos = sanitizador(input("INGRESE APELLIDOS        : "))
                            if apellidos is not None:
                                correo = sanitizador(input(   "INGRESE CORREO           : "))
                                if correo is not None:
                                    print("=======================================")
                                    global idusuario  #?=============> La variable la convierte en globlal para que lo tome el contador de afuera
                                    idusuario += 1
                                    codigo = idusuario
                                    usuario = [codigo,username,claveHash,salt,nombre,apellidos,correo]
                                    usuarios[username] = usuario
                                    break
                                else:
                                    print('No puede estar el campo vacio')
                            else:
                                print('No puede estar el campo vacio')
                        else:
                            print('No puede estar el campo vacio')
                    else:
                        print('No puede estar el campo vacio')
                else:
                    print('No puede estar el campo vacio')
        except ValueError:
            print('Ingrese valor valido')

#TODO PENDIENTE
while True: #?===========> creamos el while del menu y lo mostramos llamando funciones
    menuUsuarios()
    try:
        opUsu = sanitizador_num(input("INGRESE OPCIÓN: ")) #todo=========> Seleccion de opcion
        if opUsu == 1:  #?============> opcion 1 iniciar sesion 
            user = sanitizador(input("Ingrese nombre de usuario: "))
            clave = sanitizador(input("Ingrese password: ")) #todo hay que hacshear encriptar la clave
            if usuarios.get(user):
                usuario = usuarios.get(user)
                r = verificacion_Pass(clave, usuario[2],usuario[3]) #*agregue esto
                if r == True: #todo==============>inicio de sesion con verificacion de Contraseña encriptada 
                    print(f"Bienvenido {usuario[4]} {usuario[5]} - {anonimacion_data(clave)} - id: {usuario[0]}.") #todo=====> anonimizo datos aunque quitaria la linea de codigo
                    sanitizador(input("Presiona ENTRAR para ingresar al Menú Principal."))
                    while True:  #? Bucle para el Menú Principal
                            menuprincipal()
                            try: #todo==========================================> agregamos try para evitar la caida del programa
                                op = sanitizador_num(input("INGRESE OPCIÓN: "))
                                if op == 1:
                                    ingresardatos()
                                elif op == 2:
                                    mostrar()
                                elif op == 3:
                                    modificardatos()
                                elif op == 4:
                                    eliminardatos()
                                elif op == 5:
                                    opSalir = sanitizador(input("¿DESEA SALIR [SI/NO]: "))
                                    if opSalir.lower() == "si":
                                        break  #? Salir del bucle del Menú Principal
                                else:
                                    print("Opción Fuera de Rango")
                            except:
                                print('ERROR')
                    break  #? Salir del bucle del Menú de Usuarios
                else:
                    sanitizador(input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios."))
            else:
                    sanitizador(input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios."))
        elif opUsu == 2: #?=================> opcion crear usuario
            ingresoUsuarios()
        elif opUsu == 3: #?================> opcion salir
            opSalir = sanitizador(input("¿DESEA SALIR [SI/NO]: "))
            if opSalir.lower() == "si":
                break 
        else: #?====================> seleccion fuera de rango
            print("Opción Fuera de Rango")
    except:
        print('rorr')

