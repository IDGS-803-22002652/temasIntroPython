import os

def funcion1():
    os.system('cls')
    print("Dame los numeros")
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))
    print("La suma de los dos numeros es: ", num1 + num2)
    input()
    run()

    
def funcion2():
    os.system('cls')
    print("Dame los numeros")
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))
    print("La resta de los dos numeros es: ", num1 - num2)  
    input()
    run() 
    
def funcion3():
    os.system('cls')
    print("Dame los numeros")
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))
    print("La multiplicacion de los dos numeros es: ", num1 * num2)
    input()
    run()

def funcion4():
    os.system('cls')
    print("Dame los numeros")
    num1=int(input("Primer numero: "))
    num2=int(input("Segundo numero: "))
    print("La división de los dos numeros es: ", num1 / num2)
    input()
    run() 
      
def funcion5():
    os.system('cls')
    
def run():
    os.system('cls')
    print("Menu de opciones: ")
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicación")
    print("4.-División")
    print('5.-Salir')
    opcion= int(input("Dame una opcion: "))
    if opcion == 1:
        funcion1()
    if opcion == 2:
        funcion2()
    if opcion == 3:
        funcion3()
    if opcion == 4:
        funcion4()
    if opcion == 5:
        funcion5()
         

#La aplicacion se inicia desde este punto   
run()

if __name__ ==" __main__ ":
    run()
    
