from classManejador import Manejador
from classViajeroFrecuente import viajerofrecuente


#AGREGAR EL INGRESO DE UN DATO INT(NUMERO DE VIAJERO) Y LLAMAR A pos=m.buscar(el dato)

def menu(m):
        print("-----MENU DE OPCIONES-----")
        print("1- Viajero con mayor cantidad de millas")
        print("2- Acumular millas")
        print("3- Canjear Millas")
        print("0- Salir")
        print("----------------------------------------")
        print("\n")
        m.options()


if __name__ == '__main__':
    m = Manejador()
    m.readArchivo()
    m.mostrar()
    menu(m)