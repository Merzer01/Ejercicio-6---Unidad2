import csv
from classViajeroFrecuente import viajerofrecuente

class Manejador:
    __lista = []
    def __init__(self):
        self.__lista = []
    def readArchivo (self):         #lectura del arcchivo y carga
        with open ("viajerofrecuente.csv") as archivo:
            lector = csv.reader(archivo, delimiter=',')
            next(lector)

            for row in lector:
                num = row[0]
                doc = row[1]
                nomb = row[2]
                ap = row[3]
                mill = int(row[4])
                vf = viajerofrecuente(num, doc, nomb, ap, mill)
                self.__lista.append(vf)
    def buscar(self, num):          #busca y evalua el viajero frecuente
        p=0
        band=False
        while p < len(self.__lista) and band == False:
            dato = int(self.__lista[p].numviajero())
            if dato == num:
                band = True
            else: p = p+1
        return p
    def options(self):
        self.__lista = sorted(self.__lista)
        nv = int(input("Ingrese numero de viajero: "))
        p = self.buscar(nv)
        op = int(input("Ingrese opcion: "))
        while True:
            if op == 1:
                max = 0
                pos = 0
                j = 0
                listaux = []
                for i in range(len(self.__lista)):
                    if self.__lista[i].cantidadTotaldeMillas() > max:
                        max = self.__lista[i].cantidadTotaldeMillas()
                for i in range(len(self.__lista)):
                    if self.__lista[i].cantidadTotaldeMillas() == max:
                        listaux.append(self.__lista[i])
                print("LISTADO DE VIAJEROS CON MAYOR CANTIDAD DE MILLAS")
                for i in range(len(listaux)):
                    print(listaux[i])
                print("----------------------------------------")
            elif op == 2:
                dato = int(input("Ingrese cantidad de millas a acumular: "))
                self.__lista[p] += dato
                print("Se agregaron {} millas - Tienes un total de {} millas".format(dato, self.__lista[p].cantidadTotaldeMillas()))
                print("----------------------------------------")
            elif op == 3:
                dato = int(input("Ingrese cantidad de millas a canjear: "))
                self.__lista[p] -= dato
                print("Tienes un total de {} millas".format(self.__lista[p].cantidadTotaldeMillas()))
                print("----------------------------------------")
            elif op == 0:
                print("-----FIN-----")
                break
            else:
                print("Opcion invalida")
            op = int(input("Ingrese opcion: "))
    def mostrar(self):              #imprime los datos (evaluar eliminacion o no)
        for i in range(len(self.__lista)):
            print(self.__lista[i])