#solo toma los últimos 3 caracteres y retorna el resultado para comprar si las 3 ultimas letras son iguales
#solo se comparan entre 2 palabras

def rima(palabra1,palabra2): 
    return palabra1[-3:] == palabra2[-3:]

while True: 
    n=(input("Ingrese las dos palabras separadas por un espacio: "))
    lista=n.split(" ")     
    if(len(lista) != 2):
        print("Deben ser 2 palabras intente nuevamente")

    else: 
        print("Resultado de la rima es:")
        print(rima(lista[0],lista[1]))
        break