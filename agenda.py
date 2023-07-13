import os
import pickle
import sys

# Definir variables de color
AMARILLO = "\033[93m"
BLANCO = "\033[97m"
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Cabecera visual
def cabecera():
    print(title)
    print(divider)
    print(MAGENTA + "[+] Bienvenido a la Agenda Digital " + RESET)

title = """
                                              $$\           
                                              $$ |          
 $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$ | $$$$$$\  
 \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$ | \____$$\ 
 $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |$$ /  $$ | $$$$$$$ |
$$  __$$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$  __$$ |
\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |\$$$$$$$ |\$$$$$$$ |
 \_______| \____$$ | \_______|\__|  \__| \_______| \_______|
          $$\   $$ |                                        
          \$$$$$$  |                                        
           \______/                              < afsh4ck >
"""

divider = """------------------------------------------------------------
"""

cabecera()

def cargar_agenda():
    try:
        with open("agenda.pickle", "rb") as f:
            contactos = pickle.load(f)
    except:
        contactos = {}
    return contactos

def guardar_agenda(contactos):
    with open("agenda.pickle", "wb") as f:
        pickle.dump(contactos, f)

def agregar_contacto():
    contactos = cargar_agenda()
    nombre = input("- Ingrese el nombre del contacto: ")
    telefono = input("- Ingrese el número de teléfono del contacto: ")
    email = input("- Ingrese el correo electrónico del contacto: ")
    contactos[nombre] = {'telefono': telefono, 'email': email}
    guardar_agenda(contactos)
    print(VERDE + "[+] Contacto agregado correctamente." + "\n" + RESET)
    input(AMARILLO + "Presione Enter para continuar..." + RESET)
    os.system('clear' if os.name == 'posix' else 'cls')
    cabecera()
    menu()

def buscar_contacto():
    contactos = cargar_agenda()
    nombre = input("[+] Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print("[*] Nombre: " + AMARILLO + nombre + RESET)
        print("- Teléfono: ", CYAN + contactos[nombre]['telefono'] + RESET)
        print("- Correo electrónico: ", CYAN + contactos[nombre]['email'] + RESET)
    else:
        print(ROJO + "[!] El contacto no existe en la agenda." + RESET)
        print("\n")
    input(AMARILLO + "Presione Enter para continuar..." + RESET)
    os.system('clear' if os.name == 'posix' else 'cls')
    cabecera()
    menu()

def imprimir_agenda():
    contactos = cargar_agenda()
    if not contactos:
        print(ROJO + "[!] La agenda está vacía." + "\n" + RESET)
    else:
        print(CYAN + "[+] Lista de contactos:" + RESET)
        for nombre in sorted(contactos.keys()):
            print(BLANCO + "[*] Nombre: " + nombre)
            print("    Teléfono: ", contactos[nombre]['telefono'])
            print("    Correo electrónico: ", contactos[nombre]['email'] + "\n" + RESET)
    input(AMARILLO + "Presione Enter para continuar..." + RESET)
    os.system('clear' if os.name == 'posix' else 'cls')
    cabecera()
    menu()

def eliminar_contacto():
    contactos = cargar_agenda()
    nombre = input("[+] Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        guardar_agenda(contactos)
        print(VERDE + "[+] El contacto ha sido eliminado correctamente." + RESET)
    else:
        print(ROJO + "[!] El contacto no existe en la agenda." + RESET)
        print("\n")
    input(AMARILLO + "Presione Enter para continuar..." + RESET)
    os.system('clear' if os.name == 'posix' else 'cls')
    cabecera()

def menu():
    print(CYAN + "[+] Seleccione una opción:" + RESET)
    print("    1. Agregar un contacto")
    print("    2. Buscar un contacto")
    print("    3. Imprimir la lista de contactos")
    print("    4. Eliminar un contacto")
    print("    5. Salir del programa")
    opcion = input("> ")
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        imprimir_agenda()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print(VERDE + "[+] Gracias por usar la Agenda Digital." + RESET)
        sys.exit()
    else:
        print(ROJO + "[!] Opción inválida. Seleccione una opción del 1 al 5." + RESET)
        input(AMARILLO + "Presione Enter para continuar..." + RESET)
        os.system('clear' if os.name == 'posix' else 'cls')
        cabecera()
        menu()

menu()