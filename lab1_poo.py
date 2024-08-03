"""Desafío 4: Sistema de Gestión de Cuentas Bancarias

Objetivo: Desarrollar un sistema para administrar cuentas bancarias de clientes.

Requisitos:

    Crear una clase base CuentaBancaria con atributos como número de cuenta, saldo, titular de la cuenta, etc.
    Definir al menos 2 clases derivadas para diferentes tipos de cuentas bancarias (por ejemplo, CuentaBancariaCorrientes, CuentaBancariaAhorro) con atributos y métodos específicos.
    Implementar operaciones CRUD para gestionar las cuentas bancarias.
    Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
    Persistir los datos en archivo JSON"""
import json

class CuentaBancaria:
    def __init__(self, dni,num_cuenta,titular,saldo):
        self.__dni = self.validar_dni(dni)  
        self.__num_cuenta= self.validar_cuenta(num_cuenta)
        self.__titular = titular
        self.__saldo = saldo
        
    @property
    def dni(self):
        return self.__dni
    
    @property
    def num_cuenta(self):
        return self.__num_cuenta
    
    @property
    def titular(self):
        return self.__titular.upper()
    
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,nuevo_saldo):
        self.__saldo = nuevo_saldo

    def validar_dni(self, dni):
        try:
            dni_num = int(dni)
            if len(str(dni)) not in [7, 8]:
                raise ValueError("El DNI debe tener 7 u 8 dígitos.")
            if dni_num <= 0:
                raise ValueError("El DNI debe ser numérico positivo.")
            return dni_num
        except ValueError:
            raise ValueError("El DNI debe ser numérico y estar compuesto por 7 u 8 dígitos.")

    def validar_cuenta(self, num_cuenta):
        try:
            cuenta_num = float(num_cuenta)
            if cuenta_num <0:
                raise ValueError('El saldo debe se numero Positivo')
            return cuenta_num
        except ValueError:
            raise ValueError ('El saldo debe ser numero valido')
    
    def to_dict(self):
        return{
            'DNI': self.__dni,
            'N_Cuenta':self.__num_cuenta,
            'Titular':self.__titular,
            'Saldo': self.__saldo
        }

class CuentaAhorro(CuentaBancaria):
    def __init__(self, dni, num_cuenta, titular, saldo,cta_ahorro):
        super().__init__(dni, num_cuenta, titular, saldo)
        self.__cta_ahorro =cta_ahorro

    def to_dict(self):
        data = super().to_dict()
        data['Tipo_cuenta'] = self.__cta_ahorro
        return data
    
class CuentaCorriente(CuentaBancaria):
    def __init__(self, dni, num_cuenta, titular, saldo,cta_corriente):
        super().__init__(dni, num_cuenta, titular, saldo)
        self.__cta_corriente = cta_corriente

    def to_dict(self):
        data = super().to_dict()
        data['Tipo_cuenta'] = self.__cta_corriente
        return data
    

class GestionCuentas:
    def __init__(self,archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise  Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos
        
    def guardar_datos(self,datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos,file, indent=4)      #! datos es la informacion de las cuentas desde el json
        except IOError as error:
            print(f'Error al guardar los datos de la cuenta en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado{ error}')
    
    def crear_cuenta(self,cuenta): #! revisar esta funcion para cuentas multiples
        try:
            datos = self.leer_datos()
            dni = cuenta.dni
            if not str(dni) in datos.keys():
                datos[dni] = cuenta.to_dict()           #! aca debo cambiar este metodo, si deseo agregar mas cuentas a un mismo dNI
                self.guardar_datos(datos)
                print('La Cuenta ha sido creada exitosamente! ')
            else:
                print(f'Este titular ya posee Cuenta')   #! aca deberia preguntar si deseo agregar otro tipo de cuenta
        except Exception as error:
            print(f'Error al intentar crar la cuenta: {error}')

    def eliminar_cuenta(self,dni):
        try:
            datos = self.leer_datos()
            if str(dni) in datos.keys():
                del datos[dni]
                self.guardar_datos(datos)
                print(f'Cuenta N° de: {dni} ha sido eliminada: ')
            else:
                print(f'No se encontro la cuenta de DNI: {dni}')
        except Exception as error:
            print(f'Error al tratar de eliminar cuenta: {error}')

    def actualizar_saldo(self, dni,nuevo_saldo):
        try:
            datos = self.leer_datos()
            if str(dni) in datos.keys():
                datos[dni]['Saldo'] = nuevo_saldo
                self.guardar_datos()
                print(f'Se Actualizo el Saldo de la cuenta: {datos[dni]['N_cuenta']}')
        except Exception as error:
            print(f'Error al actualizar el saldo de la cuenta')
    
    def mostrar_cuentas(self):
        try:
            datos = self.leer_datos().values()
            lista_final = []
            for d in datos:
                titulo = d.keys()
                lista_final.append(d.values())
            print(list(titulo))
            
            for l in lista_final:
                print(l)
                
        except IOError as error:
            print(f'Archivo no encontrado: {error}')