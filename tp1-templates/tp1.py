from binario_balanceado import decimal_a_binario, es_binario_balanceado, \
                      cantidad_binarios_balanceados_entre, siguiente_binario_balanceado, \
                      anterior_binario_balanceado, binario_balanceado_mas_cercano

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario según la siguiente codificación:
        A -> Divisivilidad de dos números;
        B -> Suma de los divisores positivos de un número;
        C -> Test de abundancia de un número;
        D -> Suma de números abundantes entre dos números;
        E -> Abundante más cercano a un número;
        F -> Finalizar;
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios adelante y atrás.
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Desarrollo binario [n]')
    print('B. Es binario balanceado [n]')
    print('C. Cantidad de binarios balanceados entre [n,m]')
    print('D. Siguiente binario balanceado [n]')
    print('E. Anterior binario balanceado [n]')
    print('F. Binario balanceado más cercano [n]')
    print('G. Finalizar')
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()

    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        n:int = int(input('Ingrese n: '))
        print("El binario de " + str(n) + " es " +
        decimal_a_binario(n) + ".")
     
         
    elif opcion_seleccionada == 'B':
        n:int = int(input('Ingrese n: '))
        if es_binario_balanceado(n):
            print("El " + str(n) + " es binario balanceado. ")
        else:
            print("El " + str(n) + " no es binario balanceado. ")
        
        
    elif opcion_seleccionada == 'C':
        n:int = int(input('Ingrese n: '))
        m:int = int(input('Ingrese m: '))
        print( "Hay " + str(cantidad_binarios_balanceados_entre(n,m)) +  " binarios balanceados entre " +
        str(n) + " y " + str(m) + ".")
        
        
    elif opcion_seleccionada == 'D':
         n:int = int(input('Ingrese n: '))
         print("El siguiente binario balanceado de " + str(n) + 
         " es " + (str(siguiente_binario_balanceado(n))))
       
        
    elif opcion_seleccionada == 'E':
         n:int = int(input('Ingrese n: '))
         print("El anterior binario balanceado de " + str(n) + " es "
         + (str(anterior_binario_balanceado(n))))
         
         
    elif opcion_seleccionada == 'F':
         n:int = int(input('Ingrese n: '))
         print("El binario balanceado más cercano a " +
         str(n) + " es " + (str(binario_balanceado_mas_cercano(n))))
    
    
    elif opcion_seleccionada == 'G':
        finalizar = True
   
    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'G':
        input('Presione ENTER para continuar.')
