🔍 Demostración de Terminación y Correctitud

🧠 Función es_binario_balanceado(n: int) -> bool

📌 Terminación:
Antes de comenzar el ciclo while, la variable i comienza valiendo 0 (línea 21).

En cada iteración del ciclo, i se incrementa en 1 (línea 33).

Dado que n es un número natural y que conversión_n es la representación binaria de n, su longitud es finita.

Como el valor de n no se modifica dentro del ciclo, eventualmente i alcanzará len(conversión_n), lo que hará que la condición del while sea falsa.

Por lo tanto, el ciclo termina siempre.

✅ Correctitud:
✔️ Invariante propuesto:
0 <= i <= len(conversión_n)

contador_ceros representa la cantidad de '0' en las primeras i posiciones de conversión_n.

contador_unos representa la cantidad de '1' en las primeras i posiciones de conversión_n.

📌 Verificación paso a paso:
(A) Inicio del ciclo:

i = 0, contador_ceros = 0, contador_unos = 0

No se ha recorrido ninguna posición, por lo que ambos contadores están correctamente inicializados.

(B) Justo al entrar al ciclo:

El invariante sigue siendo válido porque i aún no cambió y los contadores tampoco.

(C) Después del cuerpo del ciclo:

Si conversión_n[i] == '0', se incrementa contador_ceros.

Si es '1', se incrementa contador_unos.

Luego, i se incrementa en 1.

Por lo tanto, se mantiene la propiedad:
"Los contadores reflejan correctamente la cantidad de ceros y unos en las primeras i posiciones".

(D) Al salir del ciclo:

i == len(conversión_n)

Se han recorrido todas las posiciones.

Los contadores reflejan la cantidad total de '0' y '1' en conversión_n.

Se compara:
contador_ceros == contador_unos
y se devuelve True o False según corresponda.

✅ Conclusión: el invariante se mantiene durante todo el ciclo y permite asegurar que la función devuelve correctamente si el número binario está balanceado.

🧠 Función siguiente_binario_balanceado(n: int) -> int
📌 Terminación:
Se inicializa la variable binario_balanceado_posterior = n + 1.

En cada iteración del ciclo, se incrementa en 1.

Dado que hay infinitos números binarios balanceados, eventualmente se encontrará uno.

Cuando eso suceda, es_binario_balanceado(...) devolverá True, lo que hará que la condición not es_binario_balanceado(...) sea False y el ciclo termine.

✅ Correctitud:
✔️ Invariante propuesto:
binario_balanceado_posterior >= n + 1

Para todo número j entre n + 1 y binario_balanceado_posterior - 1, se cumple que es_binario_balanceado(j) == False

📌 Verificación paso a paso:
(A) Inicio del ciclo:

binario_balanceado_posterior = n + 1

Todavía no sabemos si es balanceado, pero el invariante se cumple.

(B) Se entra al ciclo porque aún no se ha encontrado un número balanceado.

(C) Se incrementa binario_balanceado_posterior en 1.

Se mantiene el invariante: todos los números entre n + 1 y el actual no son balanceados.

Este proceso se repite hasta hallar un número balanceado.

(D) Al salir del ciclo:

es_binario_balanceado(binario_balanceado_posterior) == True

Por lo tanto, el valor devuelto es efectivamente el siguiente binario balanceado.

✅ Conclusión: el invariante se mantiene en cada iteración, garantizando que se devuelve el siguiente número mayor que n cuyo binario está balanceado.
