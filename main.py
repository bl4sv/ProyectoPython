from datetime import date


def CalcularEdad(fechaNacimiento): #2/2/2000
    listAux = fechaNacimiento.split("/")  # ["dd","mm","yyyy"]
    listTemp = []
    listTemp.append([date.today().day, date.today().month, date.today().year])
    if int(listAux[1]) < listTemp[0][1]:  # Ya cumplió años
        return listTemp[0][2] - int(listAux[2])
    elif int(listAux[1]) == listTemp[0][1]:  # Mismo mes
        if int(listAux[0]) <= listTemp[0][0]:  # Ya pasó el día de cumpleaños o bien está de cumpleaños
            return listTemp[0][2] - int(listAux[2])
        elif int(listAux[0]) > listTemp[0][0]:  # Mismo mes, pero aún no llega el día del cumpleaños
            return listTemp[0][2] - int(listAux[2]) - 1
    elif int(listAux[1]) > listTemp[0][1]:  # El mes actual es menor al mes del cumple (aún no cumple años)
        return listTemp[0][2] - int(listAux[2]) - 1


SuperAdministrador = ["Jonathan Mendoza", 2289, "1234", "jonathan20.dev@gmail.com", "Masculino", "02/09/2000"]
LUGARES = ["San José", "Alajuela", "Heredia", "Cartago", "San Carlos", "Puntarenas", "Limón"]


def ValidacionArchivo():
    try:
        # Verifica que admin esté dentro del archivo
        with open('Usuarios.txt', 'r') as archi:
            lineas = [linea.split("[]") for linea in archi]
            for x in lineas:
                x[0] = eval(x[0])
                if x[0][1] == SuperAdministrador[1]:
                    break
            else:  # Si admin no está dentro del archivo lo agrega
                archi = open("Usuarios.txt", "a")
                SuperAdministrador.append(CalcularEdad(SuperAdministrador[-1]))
                archi.write(SuperAdministrador.__str__())  # Guardo toda la lista, completa
                archi.write("\n")
                archi.close()
    except FileNotFoundError:  # Si el archivo no está creado, con este metodo se crea y se agrega al admin
        with open('Usuarios.txt', 'w') as archi:
            SuperAdministrador.append(CalcularEdad(SuperAdministrador[-1]))
            archi.write(SuperAdministrador.__str__())
            archi.write("\n")
            archi.close()
    except SyntaxError as error:
        print(error)
    except:
        print("Algo salió mal")
        ValidacionArchivo()


def Registro():
    listAux = []
    existe = False
    print("\nRegistrate para continuar: \n")
    try:
        # [nombre, cedula, contraseña, correo, genero, fechaNacimiento, edad]
        #   0       1         2          3       4           5           6
        cedula = int(input("Ingresa tú cédula: "))
        with open('Usuarios.txt', 'r') as archi:
            lineas = [linea.split("[]") for linea in archi]
            for x in lineas:
                x[0] = eval(x[0])
                if x[0][1] == cedula:
                    existe = True
        if existe == True:
            print("\nDicho usuario ya está registrado\nIntentalo nuevamente\n\n")
            Registro()
        else:
            contrasenna = input("Ingresa tú contraseña: ")
            nombre = input("Ingresa tú nombre: ")
            correo = input("Ingresa tú correo: ").lower()
            if ("@gmail.com" not in correo):
                aux = False
                while (aux == False):
                    print("\nNo es un correo valido\nDebes agregar una cuenta de gmail\nPor ejemplo: juan@gmail.com\n")
                    correo = input("Correo: ").lower()
                    if ("@gmail.com" in correo):
                        aux = True
            genero = input("Ingresa tú género: ")
            print("\nIngresa tú fecha de nacimiento en el siguiente formato:")
            print("dd/mm/yyyy\n")
            fecha = input("Fecha de nacimiento: ")
            listAux.append([nombre, cedula, contrasenna, correo, genero, fecha, CalcularEdad(fecha)])
            archi = open("Usuarios.txt", "a")  # Editar archivo
            archi.write(listAux[0].__str__())  # Entra Toda la lista
            archi.write("\n")
            archi.close()
    except ValueError:
        print("\n\nLa cédula debe ser un número, intentalo nuevamente\n\n")
        Registro()


def Login():
    existe = False
    try:
        print("Inicio sesion para continuar\n")
        usuario = int(input("Ingresa tú número de cédula: "))
        password = input("Ingresa tú contraseña: ")
        with open('Usuarios.txt', 'r') as archi:
            lineas = [linea.split("[]") for linea in archi]
            for x in lineas:  # Vamos a verificar si existe el usuario
                x[0] = eval(x[0])
                if x[0][1] == usuario and x[0][2] == password:  # [Cédula] & [Password]
                    if usuario == SuperAdministrador[1] and password == SuperAdministrador[2]:
                        print("\nAdministrador: " + x[0][0])
                        MenuPrincipal()
                    else:
                        print("\nViajante: " + x[0][0])
                        MenuPrincipal()
                    existe = True
            if existe == False:
                print("\ndicho usuario NO existe, intentalo nuevamente\n")
                Login()

    except ValueError:
        print("\nPor favor introduce números\n")
        Login()


def MenuInicial():
    opcion = 0
    try:
        while opcion != 3:
            print("\n" + "*" * 5 + " Menú Inicial " + "*" * 5 + "\n")
            print("[1]. Iniciar Sesión.")
            print("[2]. Registrarse.")
            print("[3]. Salir.\n")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                Login()
            if opcion == 2:
                Registro()
            if opcion == 3:
                print("Gracias por utilizar la aplicación, vuelva pronto")
    except ValueError:
        print("\nSolo se admiten números\n")
        MenuInicial()

#################################### TERMINAL #################################################

def ArchivoTerminales():
    try:
        # Verifica que el archivo esté creado
        with open('Terminales.txt', 'r') as archi:
            archi.close()
    except FileNotFoundError:  # Crear el archivo en caso de no estar
        with open('Terminales.txt', 'w') as archi:
            archi.close()
    except:  # Esto no debería de mostrarse nunca, pero por aquello lo agrego
        print("-*-" * 40)
        print("Quizas hiciste algo indebido, por favor intentalo nuevamente")
        print("-*-" * 40)
        Terminales()


def CrearTerminal():
    print("\nPor favor completa la siguiente información\n")
    nombre = input("Nombre de la terminal: ")
    print("Ingresa el número del lugar: ")
    for numero, lugar in enumerate(LUGARES):
        print("[", numero + 1 ,"]", lugar)


def ModificarTerminal():
    existe = False
    try:
        with open('Terminales.txt', 'r') as archi:
            contenido = archi.read()
            if contenido == '':
                print("Aún no hay terminales creadas")
            else:
                print("Terminales: ")
                with open('Terminales.txt', 'r') as archi:
                    lineas = [linea.split("[]") for linea in archi]
                    for x in lineas:
                        x[0] = eval(x[0])
                        print("ID: ",x[0][0],"Nombre: ",x[0][2],"Número: ",x[0][3])
                id = int(input("\nIngresa el ID de la que deseas modificar: "))
                with open('Terminales.txt', 'r') as archi:
                    lineas = [linea.split("[]") for linea in archi]
                    for x in lineas:
                        x[0] = eval(x[0])
                        if(x[0][0]==id):
                            existe = True

                            print("\nModificada Correctamente\n")

                            Terminales()
                    if existe==False:
                        print("\nDicha terminal NO existe\nIntentalo Nuevamente\n")
                        ModificarTerminal()

    except ValueError:
        print("\nSolo se admiten números\n")
        ModificarTerminal()

def EliminarTerminal():
    existe =  False
    try:
        with open('Terminales.txt', 'r') as archi:
            contenido = archi.read()
            if contenido=='':
                print("Aún no hay terminales creadas")
            else:
                print("\nTerminales:\n ")
                with open('Terminales.txt', 'r') as archi:
                    lineas = [linea.split("[]") for linea in archi]
                    for x in lineas:
                        x[0] = eval(x[0])
                        print("ID: ",x[0][0],"Nombre: ",x[0][2],"Número: ",x[0][3])
                id = int(input("\nIngresa el ID de la que deseas eliminar: "))
                with open('Terminales.txt', 'r') as archi:
                    lineas = [linea.split("[]") for linea in archi]
                    for x in lineas:
                        x[0] = eval(x[0])
                        if(x[0][0]==id):
                            existe = True

                            print("\nEliminada correctamente\n")

                            Terminales()
                    if existe==False:
                        print("\nDicha terminal NO existe\nIntentalo Nuevamente\n")
                        EliminarTerminal()
    except ValueError:
        print("\nSolo se admiten números\n")
        EliminarTerminal()


def Terminales():
    ArchivoTerminales()
    opcion = 0
    try:
        while opcion != 5:
            print("\n" + "*" * 5 + " Menú Mantenimiento de Terminales " + "*" * 5 + "\n")
            print("[1]. Crear una terminal.")
            print("[2]. Modificar una terminal.")
            print("[3]. Eliminar Terminal")
            print("[4]. Mostrar Terminales")
            print("[5]. Regresar al menú principal.\n")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                CrearTerminal()
            if opcion == 2:
                ModificarTerminal()
            if opcion == 3:
                EliminarTerminal()
            if opcion == 4:
                pass
            if opcion == 5:
                print("Sesión cerrada correctamente")
                MenuPrincipal()

    except ValueError:
        print("\nSolo se admiten números\n")
        Terminales()


################################## MENU PRINCIPAL #######################################


def MenuPrincipal():
    opcion = 0
    try:
        while opcion != 3:
            print("\n" + "*" * 5 + " Menú Principal " + "*" * 5 + "\n")
            print("[1]. Mantenimiento de Terminales.")
            print("[2]. Mantenimiento de Unidades.")
            print("[3]. Mantenimiento de Rutas.")
            print("[4]. Reportes")
            print("[5]. Cerrar Sesión.\n")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                Login()
            if opcion == 2:
                Registro()
            if opcion == 3:
                print("Gracias por utilizar la aplicación, vuelva pronto")
            if opcion == 4:
                Registro()
            if opcion == 5:
                print("Sesión cerrada correctamente")
                MenuInicial()

    except ValueError:
        print("\nSolo se admiten números\n")
        MenuPrincipal()


ValidacionArchivo()
ModificarTerminal()