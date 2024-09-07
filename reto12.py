#Se abre el texto
file=open("mbox.txt")
texto=file.read()
#Se hace un string de vocales y otro de consonantes, si al recorrer el texto en caracter está en alguno de los strings, se añade 1 al contador
vocales="aeiouáéíóúAEIOUÁÉÍÓÚ"
consonantes="qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM"
total_vocales=0
total_consonantes=0
for i in texto:
    if i in vocales:
        total_vocales+=1
    elif i in consonantes:
        total_consonantes+=1
    else:
        continue
#Se imprime el resultado
print(f"Hay un total de {total_vocales} vocales y ")
print(f"{total_consonantes} consonantes")
#Se reemplazan elementos no deseados por espacios, a fin de separar las palabras posteriormente
caracteres_eliminar=['.', ',', ';', ':', '!', '?', '"', '(', ')', '[', ']', '{', '}', '-', '_', '“', '”', '\n', '\r', '\t']
for t in texto:
    if i in caracteres_eliminar:
        texto.replace(i," ")
palabras=texto.split(" ")
#se hace un diccionario, el cual va añadiendo palabras nuevas, si la palabra ya se encuentra en el diccionario, se añade 1 a su llave
listado={}
for e in palabras:
    if e in listado:
        listado[e]+=1
    else:
        listado[e]=1
#Se ordena la lista con las llaves de mayor a menor
palabras_ordenadas = sorted(listado.items(), key=lambda x: x[1], reverse=True)
print("Las palabras que más se repiten son: ")
#Se imprimen las primeras 50 palabras
base=0
while base<50:
    print(palabras_ordenadas[base])
    base+=1