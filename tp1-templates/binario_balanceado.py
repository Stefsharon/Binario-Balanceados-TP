def decimal_a_binario(n:int) -> str:
    '''
    Requiere: que n sea un número natural (positivo).
    Devuelve: el resultado de convertir a n 
       de decimal a binario, es decir primero aplicarle
       base 2 a n y agarrar el resto de izquierda
       a derecha.
    '''
    vr:str=''
    while n > 0:
        vr = (str(n%2)) + vr
        n=n//2
    return vr


def es_binario_balanceado(n:int)->bool:
    '''Requiere: que n pertenezca a los números naturales.
       Devuelve: True si n contiene la misma cantidad de 0's y 
       1's y False en caso contrario.
    '''
    i:int=0
    vr:bool= True
    conversión_n:str= decimal_a_binario(n)
    contador_ceros:int = 0
    contador_unos:int = 0
    #A
    while i < (len(conversión_n)):
                    #B
        if conversión_n[i] == '0':
            contador_ceros = contador_ceros + 1
        else:
            contador_unos= contador_unos + 1
        i = i  + 1
        #C
    #D
    if contador_ceros == contador_unos:
        vr = True
    else:
        vr = False
    return vr


def cantidad_binarios_balanceados_entre(n:int, m:int) -> int:
    '''Requiere: n y m sean > 0 y que n sea <=m.
       Devuelve: la cantidad de números que contienen la misma
       cantidad//proporción de 0's y 1's entre n y m.
    '''
    i:int=n
    cuenta_binarios_entre_n_y_m:int=0
    while i <= m:
        if es_binario_balanceado(i):
            cuenta_binarios_entre_n_y_m = cuenta_binarios_entre_n_y_m + 1
        i = i  + 1
    return cuenta_binarios_entre_n_y_m

#COMENTARIO AUXILIAR: n y m no necesariamente tienen que ser balanceados

def siguiente_binario_balanceado(n:int) -> int:
    '''Requiere: que n pertenezca a los números naturales.
        Devuelve: el número más chico que contiene la misma 
        cantidad de 0´s y 1's y que sea > n.
    '''
    binario_balanceado_posterior:int= n + 1
    #A
    while not es_binario_balanceado(binario_balanceado_posterior):
                                    #B
        binario_balanceado_posterior = binario_balanceado_posterior + 1
        #C
    #D
    return binario_balanceado_posterior

    
def anterior_binario_balanceado(n:int) -> int:
    '''Requiere: que n pertenezca a los números naturales
        y específicamente que n sea >=3
        Devuelve: el número más grande que contiene la misma
        cantidad de 0's y 1's y que sea <n    
    '''
    binario_balanceado_previo:int = n - 1
    while not es_binario_balanceado(binario_balanceado_previo):
        binario_balanceado_previo = binario_balanceado_previo - 1
        
    return binario_balanceado_previo



def binario_balanceado_mas_cercano(n:int)->int:
    '''Requiere: n forme parte de los números naturales es 
        decir, que n sea > 0.
        Devuelve: si n es balanceado el resultado es n y en 
        caso que hayan dos más cercanos (uno anterior que n y
        otro mayor que n, a la misma distancia), se espera
        alcanzar el más grande de ellos.
    '''
    sucesivo:int= siguiente_binario_balanceado(n)
    previo:int=anterior_binario_balanceado(n)
    vr:int= 0
    if es_binario_balanceado(n):
        vr = n
    else:
        if n - previo >= sucesivo - n:
            vr = sucesivo
        elif  n-previo < sucesivo - n:
            vr = previo
        
    return vr



# # # #Definir también las funciones auxiliares que se consideren necesarias.
