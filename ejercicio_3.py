# Declaración de variable global PI con sólo 2 decimales.
pi = 3.14

#Calculo de Area del circulo y Volumen del cilindro
def calcular_area_circulo(radio):

    area =  pi * radio * 2

    return round(area,2)

def main():
    radio = float(input('Ingrese el valor del radio en cm: '))
    altura = float(input('Ingrese el valor de la altura en cm: '))
    print('\n')
    print('El área del circulo es: '+ str(calcular_area_circulo(radio)) +' cm cuadrados\n')
    print('El volumen del cilindro es: '+ str(calcular_area_circulo(radio) * altura) +' cm cubicos\n')

if __name__ == '__main__':
    main()