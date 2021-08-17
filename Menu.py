import os
from Pila import Pila_1


class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1,2 o 3]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "3":
    os.system("cls")
    men = Menu("Menu Principal",["1)Operaciones Pila", "2)Operaciones Cola", "3)Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 = ""
        os.system("cls")
        Elementos = int(input("El numero de elementos de la pila funcionara solo en esta seccion para las diferentes alternativas. \nIndicar el numero de elementos: "))
        resultados = Pila_1(Elementos)
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Operaciones Pila",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("<---Pusch--->")
                dato = int(input("Ingrese el dato:"))
                print(resultados.push(dato))
                input("Presione una tecla para continuar...")
                
            elif opc1 == "2":
                os.system("cls")
                print("<---Pop--->")
                dato = resultados.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La lista esta vacia")
                input("Presione una tecla para continuar...")
                    
            elif opc1 == "3":
                os.system("cls")
                print("<---Show--->")
                resultados.show()
                input("Presione una tecla para continuar...")
                
                
            elif opc1 == "4":
                os.system("cls")
                print("<---Longitud--->")
                print("La pila tiene una longitud de: ")
                print(resultados.longitud())
                input("Presione una tecla para continuar...")
                
                
            elif opc1 == "5":
                os.system("cls")
                print("<---Empty--->")
                dato = resultados.empty()
                if dato == True: print("La pila esta Vacia")
                else: print("La pila tiene elementos")
                input("Presione una tecla para continuar...")
    if opc == "2":
        pass  
            # opc1 = ""
            # os.system("cls")
            # Elementos = int(input("El numero de elementos de la pila funcionara solo en esta seccion para las diferentes alternativas. \nIndicar el numero de elementos: "))
            # resultados = Pila_1(Elementos)
            # while opc1 != "6":
            #     os.system("cls")
            #     men1 = Menu("Menu Operaciones Pila",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            #     opc1 = men1.menu()
            #     if opc1 == "1":
            #         os.system("cls")
            #         print("<---Pusch--->")
            #         dato = int(input("Ingrese el dato:"))
            #         print(resultados.push(dato))
            #         input("Presione una tecla para continuar...")
                    
            #     elif opc1 == "2":
            #         os.system("cls")
            #         print("<---Pop--->")
            #         dato = resultados.pop()
            #         if dato: print("El dato eliminado es: {}".format(dato))
            #         else: print("La lista esta vacia")
            #         input("Presione una tecla para continuar...")
                        
            #     elif opc1 == "3":
            #         os.system("cls")
            #         print("<---Show--->")
            #         resultados.show()
            #         input("Presione una tecla para continuar...")
                    
                    
            #     elif opc1 == "4":
            #         os.system("cls")
            #         print("<---Longitud--->")
            #         print("La pila tiene una longitud de: ")
            #         print(resultados.longitud())
            #         input("Presione una tecla para continuar...")
                    
                    
            #     elif opc1 == "5":
            #         os.system("cls")
            #         print("<---Empty--->")
            #         dato = resultados.empty()
            #         if dato == True: print("La pila esta Vacia")
            #         else: print("La pila tiene elementos")
            #         input("Presione una tecla para continuar...") 
                                
    elif opc == "3":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida")

    print("Lo espermos en una proxima ocasión")