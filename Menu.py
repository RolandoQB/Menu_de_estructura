import os
from Pila import Pila_1
from Cola import Cola_1
from Lista import Lista_1
class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menu Principal",["1)Operaciones Pila", "2)Operaciones Cola","3)Operacion Lista", "4)Salir"])
    opc = men.menu()
# ______________________________________________________________________________________________________________________
    if opc == "1":
        opc1 = ""
        os.system("cls")
        Elementos = (input("Ingrese tamaño de Pila/ caso contra1rio se elegira un tamaño de 3 valores: "))
        if Elementos  == "":
            ele=3
        else:
            ele= int(Elementos)
        resultados = Pila_1(ele)
# ______________________________________________________________________________________________________________________
        while opc1 != "6":
            os.system("cls")
            men1 = Menu("Menu Operaciones Pila",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
            opc1 = men1.menu()
# ______________________________________________________________________________________________________________________
            if opc1 == "1":
                os.system("cls")
                print("<---Pusch--->")
                dato = int(input("Ingrese el dato:"))
                res=resultados.push(dato)
                if res:
                    print("El Dato esta ingresado")
                else:
                    print("La lista esta llena")
                input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________               
            elif opc1 == "2":
                os.system("cls")
                print("<---Pop--->")
                dato = resultados.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La lista esta vacia")
                input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                   
            elif opc1 == "3":
                os.system("cls")
                print("<---Show--->")
                resultados.show()
                input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                       
            elif opc1 == "4":
                os.system("cls")
                print("<---Longitud--->")
                print("La pila tiene una longitud de: ")
                print(resultados.longitud())
                input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                    
            elif opc1 == "5":
                os.system("cls")
                print("<---Empty--->")
                dato = resultados.empty()
                if dato == True: print("La pila esta Vacia")
                else: print("La pila tiene elementos")
                input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________
    if opc == "2":  

            opc1 = ""
            os.system("cls")
            Elementos = (input("Ingrese tamaño de cola/ caso contrario se elegira un tamaño de 3 valores: "))
            if Elementos  == "":
                ele=3
            else:
                ele= int(Elementos)
            resultados = Cola_1(ele)
# ______________________________________________________________________________________________________________________
            while opc1 != "6":
                os.system("cls")
                men1 = Menu("Menu Operaciones Cola",["1)Push", "2)Pop", "3)Show","4)Longitud", "5)Empty", "6)Salir"])
                opc1 = men1.menu()
# ______________________________________________________________________________________________________________________
                if opc1 == "1":
                    os.system("cls")
                    print("<---Pusch--->")
                    dato = int(input("Ingrese el dato:"))
                    res=resultados.push(dato)
                    if res:
                        print("El valor esta ingresado")
                    else:
                        print("La lista esta llena")
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                 
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Pop--->")
                    dato = resultados.pop()
                    if dato: print("El dato eliminado es: {}".format(dato))
                    else: print("La lista esta vacia")
                    input("Presione una tecla para continuar...")
 # ______________________________________________________________________________________________________________________                       
                elif opc1 == "3":
                    os.system("cls")
                    print("<---Show--->")
                    resultados.show()
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                                 
                elif opc1 == "4":
                    os.system("cls")
                    print("<---Longitud--->")
                    print("La Cola tiene una longitud de: ")
                    print(resultados.longitud())
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                                      
                elif opc1 == "5":
                    os.system("cls")
                    print("<---Empty--->")
                    dato = resultados.empty()
                    if dato == True: print("La Cola esta Vacia")
                    else: print("La Cola tiene elementos")
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________
    if opc == "3":  

            opc1 = ""
            os.system("cls")
            Elementos = (input("Ingrese tamaño de la Lista / caso contrario se elegira un tamaño de 3 Espacios: "))
            if Elementos  == "":
                ele=3
            else:
                ele= int(Elementos)
            resultados = Lista_1(ele)
# ______________________________________________________________________________________________________________________
            while opc1 != "8":
                os.system("cls")
                men1 = Menu("Menu Operaciones Lista",["1)Append", "2)Obtener", "3)Otener eliminado","4)Buscar", "5)Insertar","6)Eliminar", "7)Mostrar","8)Salir"])
                opc1 = men1.menu()
# ______________________________________________________________________________________________________________________
                if opc1 == "1":
                    os.system("cls")
                    print("<---Append--->")
                    dato = (input("Ingrese el dato:"))
                    res=resultados.append(dato)
                    if res:
                        print("El Dato esta ingresado")
                    else:
                        print("La lista esta llena")
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________   
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Obtener--->")
                    resultados.mostrar()
                    print("De acuerdo a la tabla de posiciones escoja la que quiere obtener...  ")
                    posicion=int(input("Ingrese posicion: "))
                    resp=resultados.obtener(posicion)
                    if resp == None:
                        print("La posicion ingresada no se encuentra, verifiquela...")
                    else:
                        print("{} es el elemento en la posicion {}".format(resp,posicion))
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                        
                elif opc1 == "3":
                    os.system("cls")
                    print("<---Obtener eliminado--->")
                    resultados.mostrar()
                    print("De acuerdo a la tabla de posiciones escoja la Posicion ... ")
                    posicion=int(input("Ingrese posicion de elemento a eliminar: "))
                    resp=resultados.obtenerEliminando(posicion)
                    if resp ==None:
                        print("Posicion no valida, Verifique la Lista.....")
                    else:
                        for pos,ele in enumerate(resp):
                            # se guarda el valor eliminado del return
                            if pos==0:
                                num=ele
                            # se guarda la lista del return
                            elif pos==1:
                                num2=ele
                        print("El elemento de la posicion: {} es: {} , su nueva lista es:{}".format(posicion,num,num2))
                        
                    input("Presione una tecla para continuar...")
                    
# ______________________________________________________________________________________________________________________                            
                elif opc1 == "4":
                    os.system("cls")
                    print("<---Buscar--->")
                    dato=input("Ingrese dato a buscar: ")
                    res=resultados.buscar(dato)
                    if res != -1:
                        print("El elemento {}, esta en la posicion [{}].".format(dato,res))
                    else:
                        print("No se encuentra en la lista...")
                    
                    input("Presione una tecla para continuar...")
# ______________________________________________________________________________________________________________________                                   
                elif opc1 == "5":
                    os.system("cls")
                    print("<---Insertar--->")
                    dato=input("Digite su dato a ingresar:")
                    res=resultados.insertar(dato)
                    if res == None:
                        print("Su dato ya se encuentra en la Lista...")
                    else:
                        if res==True:
                            print("Su dato a sido Ingresado")
                        else:
                            print("Lista llena")
                    input("Presione una tecla para continuar...") 
# ______________________________________________________________________________________________________________________                      
                elif opc1 == "6":
                    os.system("cls")
                    print("<---Eliminar--->")
                    dato = input(" Digite su dato a Eliminar:")
                    res= resultados.eliminar(dato)
                    if res== None:
                        print("Su dato ingresado no esta en la Lista, No se puede eliminar.")
                    else:
                        for pos,ele in enumerate(res):
                            # se guarda el valor eliminado del return
                            if pos==0:
                                num=ele
                            # se guarda la lista del return
                            elif pos==1:
                                num2=ele
                        print("Su Dato:{} se eliminó, Su nueva Lista es:{}".format(num,num2))
                    
                    input("Presione una tecla para continuar...") 
                    
                elif opc1 == "7":
                    os.system("cls")
                    print("<---Mostrar--->")
                    resultados.mostrar()
                    
                    input("Presione una tecla para continuar...") 
                    
# ______________________________________________________________________________________________________________________                                       
    elif opc == "4":
        print("Gracias por usar el sistema")
    else:
        print("Opcion no valida")

    print("Lo espermos en una proxima ocasión")