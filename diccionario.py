import os

class Diccionario:
    palabraIngles=""
    palabraEspañol=""

    def __init__(self):
        self.palabraEspañol = ""
        self.palabraIngles = ""

    def agregarPalabra(self):
        os.system('cls')
        with open("diccionario.txt", "a") as archivo:
            self.palabraEspañol = input("Dame la palabra en Español: ")
            self.palabraIngles = input("Dame la palabra en Ingles: ")
            archivo.write(f"{self.palabraEspañol}:{self.palabraIngles}\n")
        print("Palabras agregada con éxito.")
        input()
        main()

    def buscarPalabra(self):
        os.system('cls')
        print("Buscar: ")
        print("1.- Español a Inglés")
        print("2.- Inglés a Español")
        print("3.- Salir al menu")
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            self.buscarIngles()
        elif opcion == 2:
            self.buscarEspañol()
        elif opcion == 3:
            main()
        else:
            print("Opción no válida.")
            input()
            self.buscarPalabra()

    def buscarIngles(self):
        os.system('cls')
        self.palabraEspañol = input("Dame la palabra en Español: ")
        with open("diccionario.txt", "r") as archivo:
            encontrado = False
            for linea in archivo:
                esp, ing = linea.strip().split(":")
                if esp == self.palabraEspañol:
                    print(f"Traducción = {esp} : {ing}")
                    encontrado = True
                    break
            if not encontrado:
                print("Palabra no encontrada.")
        input()
        main()

    def buscarEspañol(self):
        os.system('cls')
        self.palabraIngles = input("Dame la palabra en Inglés: ")
        with open("diccionario.txt", "r") as archivo:
            encontrado = False
            for linea in archivo:
                esp, ing = linea.strip().split(":")
                if ing == self.palabraIngles:
                    print(f"Traducción = {ing} : {esp}")
                    encontrado = True
                    break
            if not encontrado:
                print("Palabra no encontrada.")
        input()
        main()

def main():
    os.system('cls')
    print("Menú de opciones:")
    print("1.- Capturar palabras")
    print("2.- Buscar palabras")
    print("3.- Salir")
    opcion = int(input("Dame una opción: "))
    diccionario = Diccionario()
    if opcion == 1:
        diccionario.agregarPalabra()
    elif opcion == 2:
        diccionario.buscarPalabra()
    elif opcion == 3:
        exit()
    else:
        print("Opción no válida.")
        input()
        main()

if __name__ == "__main__":
    main()
