import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go



st.title(':blue[Conjuntos, funciones y operaciones binarias]')

with open( "styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

txt = r'''
<div style="text-align: justify;">

El conjunto es sinónimo de colección.Los objetos en un conjunto se denominan elementos de
el conjunto.Por lo general, denotamos conjuntos por letras mayusculas, por ejemplo, B, G, T.

Los elementos de un conjunto generalmente serán denotados por pequeñas letras latinas como $s, t, u,$ etc.
Por $s \in S$ Nos referimos a "s es un elemento de S" o "s pertenece a S".
Si s no es un elemento de S, nosotros escribimos $s \notin S$ y  esto se lee como "s no es un elemento de S" o "s no
no pertenece a S " o " s no está en S "



</div>
'''

st.markdown(txt, unsafe_allow_html=True)


txt0 = r'''
Algunos ejemplos de conjuntos son:

1. El conjunto de enteros positivos $\mathbb{N} = \{1, 2, 3, \ldots\}$.

2. El conjunto de enteros no negativos $\mathbb{Z}^+ = \{0, 1, 2, \ldots\}$.

3. El conjunto de todos los enteros $\mathbb{Z}$.

4. El conjunto de números racionales $\mathbb{Q}$.

5. El conjunto de números reales $\mathbb{R}$.

6. El conjunto de números complejos $\mathbb{C}$.

'''

st.write(txt0)




text = r'''



# Unión e Intersección de Conjuntos

## Unión de Conjuntos

<div style="text-align: justify;">

La unión de conjuntos es una operación fundamental en la teoría de conjuntos. Dados dos conjuntos $A$ y $B$, la unión
de ambos, denotada como $A \cup B$, es el conjunto que contiene todos los elementos presentes en $A$, en $B$ o en ambos.
En términos matemáticos, se puede expresar como:

$$ A \cup B = \{x \mid x \in A \text{ o } x \in B\} $$

Por ejemplo, si $A = \{1, 2, 3\}$ y $B = \{3, 4, 5\}$, entonces la unión $A \cup B$ es igual a $\{1, 2, 3, 4, 5\}$, ya
que se incluyen todos los elementos presentes en ambos conjuntos, sin duplicados.

</div>

## Intersección de Conjuntos

<div style="text-align: justify;">

La intersección de conjuntos es otra operación importante que involucra dos conjuntos $A$ y $B$. La intersección,
denotada como $A \cap B$, es el conjunto que contiene todos los elementos que están presentes tanto en $A$ como en $B$.
En términos matemáticos, se expresa como:

$$ A \cap B = \{x \mid x \in A \text{ y } x \in B\} $$

Por ejemplo, si $A = \{1, 2, 3\}$ y $B = \{3, 4, 5\}$, entonces la intersección $A \cap B$ es igual a $\{3\}$, ya que
el único elemento que está en ambos conjuntos es el 3.

</div>

## Propiedades de Unión e Intersección

<div style="text-align: justify;">

- **Conmutatividad**: $A \cup B = B \cup A$ y $A \cap B = B \cap A$
- **Asociatividad**: $(A \cup B) \cup C = A \cup (B \cup C)$ y $(A \cap B) \cap C = A \cap (B \cap C)$
- **Elemento neutro**: $A \cup \emptyset = A$ y $A \cap U = A$, donde $\emptyset$ representa el conjunto vacío y $U$ el
conjunto universal.
- **Ley distributiva**: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

</div>

# Producto Cartesiano

## Definición

<div style="text-align: justify;">

El producto cartesiano es una operación que combina elementos de dos conjuntos diferentes para formar un nuevo conjunto.
Dados dos conjuntos $A$ y $B$, el producto cartesiano $A \times B$ es el conjunto de todas las posibles combinaciones
ordenadas de elementos, donde el primer elemento proviene de $A$ y el segundo elemento proviene de $B$.
Matemáticamente, se representa como:

$$ A \times B = \{(a, b) \mid a \in A \text{ y } b \in B\} $$

</div>

## Ejemplo

<div style="text-align: justify;">

Consideremos dos conjuntos: $A = \{1, 2\}$ y $B = \{3, 4\}$. El producto cartesiano $A \times B$ será:

$$ A \times B = \{(1, 3), (1, 4), (2, 3), (2, 4)\} $$

Cada elemento del producto cartesiano es un par ordenado, donde el primer valor pertenece a $A$ y el segundo valor
pertenece a $B$. En este ejemplo, $A$ tiene dos elementos y $B$ tiene dos elementos, por lo que el producto cartesiano
contiene $2 \times 2 = 4$ pares ordenados.

</div>

## Propiedades


<div style="text-align: justify;">

- **Conmutatividad**: $A \times B = B \times A$
- **Elemento neutro**: $A \times \emptyset = \emptyset$, donde $\emptyset$ representa el conjunto vacío.
- **Ley distributiva**: $A \times (B \cup C) = (A \times B) \cup (A \times C)$

</div>

## Producto Cartesiano de Conjuntos con sí mismos

<div style="text-align: justify;">

Cuando un conjunto se combina consigo mismo en un producto cartesiano, se obtiene un conjunto de pares ordenados que
son todas las posibles combinaciones de elementos del conjunto. Si $A$ es un conjunto con $n$ elementos, entonces el
producto cartesiano $A \times A$ (también denotado como $A^2$) tendrá $n^2$ elementos.

</div>


# Relaciones y Relaciones de Equivalencia

## Relaciones

<div style="text-align: justify;">

En matemáticas, una relación es una asociación entre elementos de dos o más conjuntos. Formalmente, una relación $R$
entre dos conjuntos $A$ y $B$ es un subconjunto del producto cartesiano $A \times B$, donde cada elemento $(a, b)$ en
$R$ indica que el elemento $a$ está relacionado con el elemento $b$.

Existen varios tipos de relaciones, incluyendo:

1. **Relación Binaria**: Es una relación entre dos conjuntos $A$ y $B$.
2. **Relación Reflexiva**: Si para cada elemento $a$ en el conjunto $A$, existe un par $(a, a)$ en la relación $R$.
3. **Relación Simétrica**: Si para cada par $(a, b)$ en la relación $R$, también existe el par $(b, a)$ en $R$.
4. **Relación Transitiva**: Si para cada par $(a, b)$ y $(b, c)$ en la relación $R$, también existe el par $(a, c)$ en $R$.

</div>

## Relaciones de Equivalencia

<div style="text-align: justify;">

Una relación de equivalencia es un tipo especial de relación que cumple tres propiedades importantes: reflexividad,
simetría y transitividad. Si una relación $R$ satisface estas tres propiedades, se dice que es una relación de equivalencia.

Formalmente, una relación de equivalencia $R$ en un conjunto $A$ es una relación binaria que cumple con las siguientes
propiedades para todo $a, b, c \in A$:

1. **Reflexividad**: $a \, R \, a$ para todo $a \in A$.
2. **Simetría**: Si $a \, R \, b$, entonces también $b \, R \, a$.
3. **Transitividad**: Si $a \, R \, b$ y $b \, R \, c$, entonces también $a \, R \, c$.

Las relaciones de equivalencia dividen el conjunto en clases de equivalencia, donde cada clase contiene elementos que
están relacionados entre sí por la relación de equivalencia. Además, estas clases son mutuamente excluyentes y
cubren todo el conjunto $A$.

</div>

## Ejemplos

<div style="text-align: justify;">

1. La relación "es igual a" en el conjunto de números enteros es una relación de equivalencia, ya que cumple con las
tres propiedades: reflexividad (todo número es igual a sí mismo), simetría (si un número es igual a otro, entonces el
otro también es igual al primero) y transitividad (si un número es igual a otro y este otro es igual a un tercero,
entonces el primero también es igual al tercero).

2. La relación "es congruente módulo n" en el conjunto de números enteros es otra relación de equivalencia. En este
caso, dos números son equivalentes si tienen el mismo residuo al dividirse por n.


</div>

# Particiones

## Definición

<div style="text-align: justify;">

En matemáticas, una partición de un conjunto $A$ es una colección de subconjuntos no vacíos y mutuamente excluyentes de
$A$ cuya unión es igual al conjunto original $A$. Es decir, una partición divide el conjunto en subconjuntos disjuntos
que, cuando se unen, vuelven a formar el conjunto original.

</div>

## Características

<div style="text-align: justify;">

Una partición $\mathcal{P}$ de un conjunto $A$ debe cumplir con las siguientes características:

1. **Subconjuntos No Vacíos**: Cada subconjunto en la partición debe contener al menos un elemento del conjunto $A$.
Formalmente, para todo $S \in \mathcal{P}$, $S \neq \emptyset$.

2. **Mutua Exclusividad**: Los subconjuntos en la partición deben ser mutuamente excluyentes, es decir, no pueden tener
elementos en común. Si $S, T \in \mathcal{P}$ y $S \neq T$, entonces $S \cap T = \emptyset$.

3. **Unión Igual al Conjunto Original**: La unión de todos los subconjuntos en la partición debe ser igual al conjunto
original. Matemáticamente, se debe cumplir que $\bigcup_{S \in \mathcal{P}} S = A$.

</div>

## Ejemplo


<div style="text-align: justify;">

Consideremos el conjunto $A = \{1, 2, 3, 4, 5, 6\}$. Una posible partición de $A$ es:

$$ \mathcal{P} = \{\{1, 2, 3\}, \{4, 5\}, \{6\}\} $$

Esta partición cumple con todas las características mencionadas: cada subconjunto es no vacío, los subconjuntos son
mutuamente excluyentes y su unión es igual a $A$.

</div>

## Relación con Relaciones de Equivalencia

<div style="text-align: justify;">

Hay una estrecha relación entre las particiones y las relaciones de equivalencia. Si tenemos una relación de
equivalencia $R$ en un conjunto $A$, los elementos que están relacionados entre sí formarán una clase de equivalencia.
La colección de todas las clases de equivalencia forma una partición de $A$.

En otras palabras, una partición de un conjunto $A$ corresponde a una relación de equivalencia en $A$,
donde los elementos dentro de cada subconjunto de la partición están relacionados entre sí y los elementos en diferentes
subconjuntos no están relacionados.


</div>

# Funciones

## Definición

<div style="text-align: justify;">

En matemáticas, una función es una relación especial entre dos conjuntos, donde cada elemento del primer conjunto
tiene asignado un único elemento del segundo conjunto. Formalmente, una función $f$ de un conjunto $A$ a un conjunto $B$,
denotada como $f: A \rightarrow B$, asigna a cada elemento $a \in A$ un único elemento $b \in B$.

La notación $f(a)$ se utiliza para representar el elemento asignado a $a$ bajo la función $f$. En otras palabras,
$f(a)$ es el valor de la función $f$ evaluada en el elemento $a$.

</div>

## Características

<div style="text-align: justify;">

Las funciones tienen algunas características clave:

1. **Dominio**: Es el conjunto de todos los valores posibles de entrada (argumentos) para la función. En la notación,
el dominio se representa como $\text{dom}(f)$ o simplemente $A$.

2. **Codominio**: Es el conjunto de todos los valores posibles de salida para la función. En la notación, el codominio
se representa como $\text{codom}(f)$ o simplemente $B$.

3. **Imagen**: Es el conjunto de todos los valores reales de salida que la función toma para todos los elementos del
dominio. La imagen se representa como $\text{Im}(f)$.

4. **Inyectividad**: Una función es inyectiva (también conocida como función uno a uno) si cada elemento en el codominio
está relacionado con a lo sumo un elemento en el dominio.

5. **Sobreyectividad**: Una función es sobreyectiva (también conocida como función sobre) si cada elemento en el
codominio está relacionado con al menos un elemento en el dominio.

6. **Biyectividad**: Una función es biyectiva si es tanto inyectiva como sobreyectiva. Esto significa que cada elemento
en el codominio está relacionado con exactamente un elemento en el dominio, y no hay elementos sin asignar.

</div>


## Representación Gráfica

<div style="text-align: justify;">

Las funciones se pueden representar gráficamente en un sistema de coordenadas cartesianas. Si el dominio y el codominio
son conjuntos de números reales, la gráfica de una función $f$ consiste en los puntos
$(a, f(a))$ para cada $a$ en el dominio.


</div>

# Composición de Funciones

## Definición

<div style="text-align: justify;">

La composición de funciones es una operación que combina dos o más funciones para formar una nueva función.
Dadas dos funciones $f: A \rightarrow B$ y $g: B \rightarrow C$, la composición de $f$ y $g$, denotada como $g \circ f$,
es una nueva función que primero aplica $f$ a un elemento del conjunto $A$ y luego aplica $g$ al resultado para obtener
un elemento del conjunto $C$.

Formalmente, la composición de funciones se define como:

$$ (g \circ f)(x) = g(f(x)) $$


</div>

## Características

<div style="text-align: justify;">

Las características importantes de la composición de funciones son:

1. **Dominio y Codominio**: La composición de funciones solo es posible cuando el codominio de $f$ coincide con el
dominio de $g$. En otras palabras, para que la composición $g \circ f$ esté definida, la imagen de $f$ debe estar
completamente contenida en el dominio de $g$.

2. **Orden Importa**: En general, la composición de funciones no es conmutativa, lo que significa que el orden en que
se componen las funciones es relevante. En general, $g \circ f$ no es igual a $f \circ g$.

3. **Asociatividad**: La composición de funciones es asociativa, lo que significa que para tres funciones
$f: A \rightarrow B$, $g: B \rightarrow C$ y $h: C \rightarrow D$, se cumple que
$(h \circ g) \circ f = h \circ (g \circ f)$.

</div>

# Operaciones Binarias

## Definición

<div style="text-align: justify;">

En matemáticas, una operación binaria es una función que toma dos elementos de un conjunto y devuelve un único elemento del mismo conjunto. Formalmente, una operación binaria $\ast$ en un conjunto $A$ se puede representar como:

$$ \ast: A \times A \rightarrow A $$

Esto significa que para cada par ordenado $(a, b)$ en el conjunto $A \times A$, la operación binaria $\ast$ devuelve un único elemento $\ast(a, b)$ en $A$.

</div>

## Ejemplos

<div style="text-align: justify;">

Algunos ejemplos comunes de operaciones binarias son:

1. **Suma**: La suma es una operación binaria en el conjunto de números enteros $\mathbb{Z}$, donde para cada par de
números enteros $a$ y $b$, la suma $a + b$ es otro número entero.

2. **Multiplicación**: La multiplicación es otra operación binaria en el conjunto de números enteros $\mathbb{Z}$,
donde para cada par de números enteros $a$ y $b$, la multiplicación $a \times b$ es otro número entero.

3. **Unión**: La unión es una operación binaria en el conjunto de conjuntos $\mathcal{P}(A)$, donde para cada par de
conjuntos $X$ y $Y$, la unión $X \cup Y$ es otro conjunto.

4. **Intersección**: La intersección es otra operación binaria en el conjunto de conjuntos $\mathcal{P}(A)$, donde
para cada par de conjuntos $X$ y $Y$, la intersección $X \cap Y$ es otro conjunto.

Las tablas de multiplicación son una forma de representar una operación binaria, específicamente la multiplicación,
en un conjunto finito. En este contexto, la operación binaria es la multiplicación entre dos elementos del conjunto,
y las tablas de multiplicación muestran los resultados de todas las posibles combinaciones de elementos.

</div>

## Tabla de Multiplicación en un Conjunto Finito

<div style="text-align: justify;">


Supongamos que tenemos un conjunto finito $A$ con $n$ elementos: $A = \{a_1, a_2, ..., a_n\}$. Si definimos la operación
binaria de multiplicación en $A$, denotada como $\ast$, la tabla de multiplicación mostrará todos los resultados de la
multiplicación de los elementos de $A$ consigo mismos. La tabla tendrá $n \times n$ celdas, y la entrada en la fila $i$
y la columna $j$ será el resultado de la multiplicación de $a_i$ con $a_j$.


</div>

## Ejemplo de Tabla de Multiplicación en un Conjunto Finito

<div style="text-align: justify;">


Consideremos el conjunto $A = \{1, 2, 3\}$ y definamos la operación binaria de multiplicación en $A$. La tabla de
multiplicación sería la siguiente:

</div>

 x | 1 |2  |3
---|---|---|---
 1 | 1 | 2 | 3
 2 | 2 | 4 | 6
 3 | 3 | 6 | 9

<div style="text-align: justify;">


En esta tabla, cada celda muestra el resultado de la multiplicación de los elementos de la fila con los elementos de la
columna. Por ejemplo, la celda en la fila 2 y columna 3 muestra el resultado de $2 \ast 3$, que es igual a 6.


</div>

## Propiedades de la Tabla de Multiplicación

<div style="text-align: justify;">

En la tabla de multiplicación, podemos observar varias propiedades matemáticas importantes:

1. **Elemento Neutro**: Si el conjunto tiene un elemento neutro respecto a la multiplicación, aparecerá en la diagonal
de la tabla. En el ejemplo anterior, el 1 es el elemento neutro, ya que $a \ast 1 = 1 \ast a = a$ para cualquier $a$ en el conjunto.

2. **Elementos Inversos**: Si cada elemento tiene un inverso bajo la multiplicación, aparecerá un elemento
correspondiente en cada fila y en cada columna. En el ejemplo, el inverso de 2 es 0.5, ya que $2 \ast 0.5 = 0.5 \ast 2 = 1$.

</div>



'''
st.write(text,unsafe_allow_html=True)
