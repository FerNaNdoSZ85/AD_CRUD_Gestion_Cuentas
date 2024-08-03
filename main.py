from lab1_poo import *

def mostrar_menu():
    print("********** Menú de Gestión de Cuentas ***********")
    print('1 - Crear Cuenta Bancaria')
    print('2 - Listar Cuentas Existentes ')
    print('3 - Eliminar Cuentas Existentes ')
    print('4 - Actualizar Saldo de Cuenta ')
    print('5 - Mostrar Cuentas Existentes ')
    print('6 - Salir de la Aplicación ')


def agregar_cuenta(gestion,tipo_cuenta):
    try:
        dni = input('Ingrese DNI del Titular: ')
        num_cuenta = input('Ingrese numero de Cuenta: ')
        titular =  input('Ingrese Nombre y apellido del titular: ')
        saldo = input('Ingrese monto de la cuenta: ')
        cta_cuenta = input('Ingrese el tipo de Cuenta: 1-AHORRO <===> 2 - CORRIENTE: ')

        if cta_cuenta == '1':
            cta_ahorro = 'AHORRO'
            cuenta = CuentaAhorro(dni, num_cuenta, titular, saldo,cta_ahorro)
            gestionar_cuenta.crear_cuenta(cuenta)

        elif cta_cuenta == '2':
            cta_corriente = 'CORRIENTE'
            cuenta = CuentaCorriente(dni, num_cuenta, titular, saldo,cta_corriente)
            gestionar_cuenta.crear_cuenta(cuenta)
        

    except ValueError as error:
        print(f'Error {error}')
    except Exception as error:
        print(f'Error inesperado a la crear al cuenta: ')

def listar_cuentas(self,cuenta):
    try:
        datos = self.leer_datos()
        for i in datos.items():
            print(i)      #! deberia mejorarse esta presentacion de informacion
    except Exception as e:
        print(f'Error al extraer los datos: {e}')

def eliminar_cuenta_dni(gestion):
    dni = input('Ingrese el DNI del titular: ')
    gestion.eliminar_cuenta(dni)
    input('Presione ENTER para continuar ')

def actualizar_cuenta(gestionar_cuenta):
    dni = input('Ingrese el DNI del titular a modificar: ')
    nuevo_saldo = float(input('Ingrese el nuevo Saldo: '))
    gestionar_cuenta.actualizar_saldo(dni,nuevo_saldo)
    input('Presione ENTER para continuar ')

def listar_cuentas(gestionar_cuenta):
    gestionar_cuenta.mostrar_cuentas()



if __name__ == '__main__':
    archivo_cuentas = 'cuentas_db.json'
    gestionar_cuenta = GestionCuentas(archivo_cuentas)

    while True:
        mostrar_menu()
        opcion = input('Seleccione un opcion: ')

        if opcion == '1':
            agregar_cuenta(gestionar_cuenta, opcion)
        elif opcion == '2':
            listar_cuentas(gestionar_cuenta, opcion)
        elif opcion == '3':
            eliminar_cuenta_dni(gestionar_cuenta)
        elif opcion == '4':
            actualizar_cuenta(gestionar_cuenta)
        elif opcion == '5':
            listar_cuentas(gestionar_cuenta)
        elif opcion == '6':
            print(' === FINALIZANDO APLICACION === ')
            break
        else:
            print('opcion no válida')
