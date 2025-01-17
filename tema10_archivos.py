from io import open

texto="una line"
archivo=open("archivo.txt","w")
archivo.write(texto)
texto="\nuna nueva linea"
archivo.write(texto)
texto="\nuna nueva linea tres"
archivo.write(texto)
archivo.close()

texto="\nuna nueva line a"
archivo=open("archivo.txt","a")
archivo.write(texto)