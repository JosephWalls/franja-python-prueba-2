#Se encarga de revisar uno a uno cual es la palabra más larga
#Si la palabra es la más larga luego de terminar el loop la retorna.

def mayor(array):
    largo = 0
    palabra = ""
    for pal in array: 
        if len(pal) > largo:
            palabra = pal
            largo = len(pal)
    return palabra

n=(input("Ingrese las palabras separadas por un espacio: "))
lista=n.split(" ")    
print("La palabra mas larga es: ")
print(mayor(lista))