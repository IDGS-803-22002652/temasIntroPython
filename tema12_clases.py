class OperasBas:
    #declaracion de propiedades de clase
    num1=0
    num2=0
    res=0
    #declaracion de constructor
    def __init__(self,a,b):
       self.num1=a
       self.num2=b
    
    #declaracion de metodos de la clase
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))
        
def main():
    #creacion de un objeto de la clase OperasBas
    obj1=OperasBas(23,18)
    obj1.suma()

if __name__ == "__main__":
    main()  
