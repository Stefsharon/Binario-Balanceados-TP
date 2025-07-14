import unittest

# Se importa el código a testear.
from binario_balanceado import decimal_a_binario, es_binario_balanceado, \
                      cantidad_binarios_balanceados_entre, siguiente_binario_balanceado, \
                      anterior_binario_balanceado, binario_balanceado_mas_cercano

#####################################################################

class TestBinariosBalanceados(unittest.TestCase):
    def test_decimal_a_binario_EjemplosEnunciado(self):
        num_decimal_input: int = 3
        resultado_esperado:str= '11'
        resultado_decisivo:str = decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo,resultado_esperado)
        
        num_decimal_input:int= 11921
        resultado_esperado:str = '10111010010001'
        resultado_decisivo:str = decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    
    def test_decimal_a_binario_MásDeUnDígito(self):
        num_decimal_input:int = 10
        resultado_esperado:str = '1010'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        num_decimal_input:int = 100
        resultado_esperado:str= '1100100'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_decimal_a_binario_NumerosRepetidos(self):
        num_decimal_input: int = 2222
        resultado_esperado: str = '100010101110'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        num_decimal_input:int = 1111
        resultado_esperado: str = '10001010111'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        
    def test_decimal_a_binario_NumerosPares(self):
        num_decimal_input:int= 8
        resultado_esperado:str = '1000'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        num_decimal_input: int = 26
        resultado_esperado: str = '11010'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    def test_decimal_a_binario_NumerosImpares(self):
        num_decimal_input: int = 7
        resultado_esperado:str = '111'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        num_decimal_input: int = 19
        resultado_esperado: str = '10011'
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_decimal_a_binario_PotenciaDeDos(self): #caso borde
        num_decimal_input:int=(2**1) -1
        resultado_esperado:str = '1' #decimal: 1
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        num_decimal_input:int = (2**3) -1
        resultado_esperado: str = '111' #decimal: 7
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        num_decimal_input : int =(2**4) -1
        resultado_esperado:str= '1111'   #decimal: 15
        resultado_decisivo:str= decimal_a_binario(num_decimal_input)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
#####################################################################

    def test_es_binario_balanceado_EjemplosEnunciadosVerdaderos(self):
        n:int= 2 #10
        self.assertTrue(es_binario_balanceado(n))
        
        n:int= 11921  #10111010010001
        self.assertTrue(es_binario_balanceado(n))
    
    def test_es_binario_balanceado_EjemplosEnunciadosFalsos(self):
        n:int = 3 ##11
        self.assertFalse(es_binario_balanceado(n))
        n:int = 54 #110110
        self.assertFalse(es_binario_balanceado(n))
    
    def test_es_binario_balanceado_SoloUnDígito(self):
        n:int = 9 #1001
        self.assertTrue(es_binario_balanceado(n))
        n:int = 8 #1000
        self.assertFalse(es_binario_balanceado(n))
         
    def test_es_binario_balanceado_SoloUnos(self):
        n:int = 11 #1011
        self.assertFalse(es_binario_balanceado(n))
        n: int = 11111 #10101101100111
        self.assertFalse(es_binario_balanceado(n))
    
    def test_es_binario_balanceado_CasiCompletos(self):
        n:int = 4 #100 (2 ceros y solo un uno)
        self.assertFalse(es_binario_balanceado(n))
        n: int = 5 #101 (2 unos y solo un cero)
        self.assertFalse(es_binario_balanceado(n))
        
    def test_es_binario_balanceado_NumerosPares(self):
        n:int= 18 #10010 (2 unos y 3 ceros)
        self.assertFalse(es_binario_balanceado(n)) 
        n: int = 24 #11000 (2 unos y 3 ceros)
        self.assertFalse(es_binario_balanceado(n))
        n: int = 36 #100100 (2 unos y 4 ceros)
        self.assertFalse(es_binario_balanceado(n))
    
    def test_es_binario_balanceadoNumerosImpares(self):
        n:int = 31 #11111 (5 unos, ningún 0)
        self.assertFalse(es_binario_balanceado(n))
        n:int = 81 #1010001 (3 unos y 4 ceros)
        self.assertFalse(es_binario_balanceado(n))
  
        
#####################################################################

    def test_cantidad_binarios_balanceados_entre_EjemplosEnunciado(self):
         n: int = 2
         m: int = 10 
         resultado_esperado: int = 3
         resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
         self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_cantidad_binarios_balanceados_entre_Varios(self):
        n: int = 8
        m: int = 10
        resultado_esperado: int = 2
        resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 12
        m:int = 35
        resultado_esperado: int = 2
        resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_cantidad_binarios_balanceados_entreNumerosFactoriales(self):
        n: int = 1 * 2 * 3 * 4
        m:int= 1*2*3*4*5
        resultado_esperado: int = 10
        resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_cantidad_binarios_balanceados_entre_NumerosCompuestos(self):
        n:int = 4
        m:int = 6
        resultado_esperado: int = 0
        resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        
    def test_cantidad_binarios_balanceados_entre_NumerosPrimos(self):
        n: int = 7 
        m: int = 11
        resultado_esperado: int = 2
        resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    def test_cantidad_binarios_balanceados_IntervaloMínimo(self):
        n: int = 56
        m: int = 56
        resultado_esperado: int = 1
        resultado_decisivo: int = cantidad_binarios_balanceados_entre(n,m)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        
#####################################################################
    
    def test_siguiente_binario_balanceado_EjemplosEnunciado(self):
        n:int = 2
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    def test_siguiente_binario_balanceado_MuchosDígitos(self):
        n: int = 10394000
        resultado_esperado:int = 10394001
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n: int = 9860342
        resultado_esperado: int = 9860359
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        
    def test_siguiente_binario_balanceado_MismosDigitosRepetidos(self):
        n: int = 999
        resultado_esperado:int = 2079
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    def test_siguiente_binario_balanceado_NumerosImpares(self):
        n: int = 151
        resultado_esperado: int = 153
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    def test_siguiente_binario_balanceado_Primeros10(self):  
        n:int = 1
        resultado_esperado: int = 2
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n: int = 2
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n: int = 3
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n: int = 4
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 5
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 6
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 7
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 8
        resultado_esperado: int = 9
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 9
        resultado_esperado: int = 10
        resultado_decisivo: int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 10
        resultado_esperado:int = 12 
        resultado_decisivo:int = siguiente_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)

#####################################################################

    def test_anterior_binario_balanceado_EjemploEnunciado(self):
        n: int = 9
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_anterior_binario_balanceado_Cercanos_y_Alejados(self):
        n: int = 999
        resultado_esperado: int = 992
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 99999
        resultado_esperado: int = 65280
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)

    
    
    def test_anterior_binario_balanceado_Primeros8(self):  
    #empezamos desde n = 3, por las restrincciones de mi requiere. 
        n: int = 3
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n: int = 4
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 5
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 6
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 7
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 8
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 9
        resultado_esperado: int = 2
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int= 10
        resultado_esperado: int = 9
        resultado_decisivo: int = anterior_binario_balanceado(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)

#####################################################################
    
    def test_binario_balanceado_mas_cercano_EjemplosEnunciados(self):
        n:int= 5
        resultado_esperado: int  = 2
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 6
        resultado_esperado: int  = 9
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_binario_balanceado_mas_cercano_CuandoEsBinarioBalanceado(self):
        n:int = 9
        resultado_esperado: int = 9
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int=10
        resultado_esperado:int = 10
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_binario_balanceado_mas_cercano_BinariosPrevios(self):
        n:int = 18
        resultado_esperado: int = 12
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n:int = 22
        resultado_esperado: int = 12
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
    def test_binarios_balanceado_mas_cercano_Binarios_Sucesivos(self):
        n:int = 40
        resultado_esperado: int = 41
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        n: int = 200
        resultado_esperado: int = 201
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
    
    def test_binarios_balanceados_mas_cercano_SucesivoAnteriorIguales(self):
        n:int = 11
        resultado_esperado:int = 12
        resultado_decisivo: int = binario_balanceado_mas_cercano(n)
        self.assertEqual(resultado_decisivo, resultado_esperado)
        
        
        
        
# Y así con el resto de las funciones a testear.

unittest.main()
