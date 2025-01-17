texto=""
archivo=open("archivo.txt","r")

#texto=archivo.read()
#print(texto)
#archivo.seek(0)
#texto=archivo.read()
#print(texto)

#texto=archivo.readline()
#print(texto)
texto=archivo.readlines()
print(texto)

archivo.close()