import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import re
from itertools import permutations
import os
import base64







with open( "styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
st.title(':blue[Grupoides]')
r'''
**Definición (grupoide o magma):**
Un grupoide es un par $(G,\mu)$ que consiste en un conjunto G no vacío, llamado portador,
y una operación binaria

$$\mu: G \times G \rightarrow G$$,en $G$, tal que es cerrada.



**Definición (Igualdad de groupoides):**
Dos grupos son iguales si y solo si tienen los mismos conjuntos portadores y la misma operación binaria.


Recuerde, una operación binaria se definió como un mapeo y dos asignaciones
son iguales si y solo si tienen el mismo dominio y codominio, y la imagen de cada elemento es la misma al aplicar
cualquiera de los dos mapeos.

**Definición (groupoide conmutativo):**
Un grupoide conmutativo es un grupoide $(G,\mu)$ tal que $(a,b)_\mu=(b,a)_\mu$, para todo $a,b \in G$.

**Definición (groupoide asociativo):**
Un grupoide asociativo es un grupoide $(G,\mu)$ tal que $((a,b)_\mu,c)_\mu = (a,(b,c)_\mu)_\mu$ para todo $a,b,c \in G$.

**Definición (orden de un groupoide):**
El orden de un groupoide $(G,\mu)$ es el número de elementos de $G$ denotado por $|G|$; $(G,\mu)$  es infinito si $|G|$
es infinito y es finito si $|G|$ es finito.

'''

with st.expander('Nota:'):
    textn = r'''
Un grupo se puede considerar como un grupo de transformaciones de simetría que relaciona isomórficamente un objeto
para sí mismo (las simetrías de un objeto, como las isometrías de un poliedro), un grupo es una colección de
Transformaciones de simetría que actúan entre posiblemente más de un objeto.

Por lo tanto, un grupo de groupoide consiste en un conjunto de objetos $x, y ,\ldots, z$ y para cada par de objetos $(x, y)$ hay un conjunto de
transformaciones, generalmente denotadas por flechas
    '''
    st.write(textn)

    st.latex(r"x \xrightarrow{f} y")

    file_ = open("pages/Cdiag-removebg-preview.png", "rb")

    st.write('que puede estar compuesto si son compuestos (es decir, si el primer termina donde el segundo comienza)')

    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()


    st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url}" alt="galois"></div>',
    unsafe_allow_html=True,
    )

    st.write('tal que esta composición es asociativa')


    file1_ = open("pages/cdiag2-removebg-preview.png", "rb")
    contents1 = file1_.read()
    data_url1 = base64.b64encode(contents1).decode("utf-8")
    file1_.close()


    st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url1}" alt="galois"></div>',
    unsafe_allow_html=True,
    )
    text1 =r'''
    y tal que para cada objeto $x$ hay transformación de identidad $x \xrightarrow{Id_X}x $.
    En que este es un elemento neutral para la composición de las transformaciones, siempre que se define.

    Hasta ahora, esta estructura es lo que se llama una categoría pequeña.Lo que hace que esto sea un grupo (pequeño) es que todos estos
    Las transformaciones deben ser "simetrías" en el sentido de que son morfismos invertibles, lo que significa que para cada transformación
    $x \xrightarrow{f} y$ hay una transformación al revés $y \xrightarrow{f^{-1}} x$, tal que

    $$
    f^{-1} \circ f = Id_{x}, f \circ f^{-1} = Id_{y}
    $$

    Si solo hay un objeto $X$, entonces esta definición se reduce a la de un grupo, y en este sentido groupoides
    son "grupos con muchos objetos".Por el contrario, dado cualquier grupo de groupoides y la elección de uno de sus objetos $x$,
    entonces la subcolección de transformaciones de $y$ a $x$ es un grupo, a veces llamado grupo de automorfismo $Aut_G(x)$ de $x$ en $G$.
    '''
    st.write(text1)

st.subheader(':triangular_ruler:')
def is_conmutative(tabb,sett,op):
    """
    The function `is_conmutative` checks if a given set with a binary operation is commutative.

    :param sett: The parameter "sett" represents a set of elements that form a groupoid. It could be a list, tuple, or any
    other iterable containing the elements of the set
    :param op: The parameter "op" represents the binary operation that is being performed on the elements of the set "sett"
    :return: The function is_conmutative returns a tuple containing a boolean value and a string. The boolean value
    indicates whether the groupoid is commutative or not, and the string contains logs or messages related to the
    commutativity of the groupoid.
    """
    logs = ''
    for i in range(len(sett)):
        for j in range(len(sett)):
                if tabb[i,j] == tabb[j,i]:
                    continue
                else:
                    logs += 'El grupoide no es conmutativo: \n'
                    logs +=r'$( '+ str(sett[i])+','+str(sett[j])+')_\mu  \noteq  '+r'( '+ str(sett[j])+','+str(sett[i])+')_\mu  $ '
                    return False,logs
    logs += 'El grupoide es conmutativo $(a,b)_\mu = (b,a)_\mu$'
    return True,logs

def is_asociative(sett,op):
    """
    The function `is_asociative` checks if a given set with an operation is associative or not.

    :param sett: The parameter "sett" represents a set of elements that form a groupoid. It could be a list, tuple, or any
    other iterable containing the elements of the set
    :param op: The parameter "op" represents the binary operation that is defined on the set "sett". The function
    "is_asociative" checks if this binary operation is associative on the given set
    :return: a tuple containing a boolean value and a string. The boolean value indicates whether the groupoid is
    associative or not, and the string contains logs or messages related to the associativity of the groupoid.
    """
    logs = ''
    for i in range(len(sett)):
        for j in range(len(sett)):
            for k in range(len(sett)):
                if op(op(sett[i],sett[j]),sett[k]) == op(sett[i],op(sett[j],sett[k])):
                    continue
                else:
                    logs += 'El grupoide no es Asociativo: \n'
                    logs +=r'$(( '+ str(sett[i])+','+str(sett[j])+')_\mu,'+str(sett[k])+')_\mu   \noteq  '+r'( '+ str(sett[j])+',('+str(sett[i])+','+str(sett[k])+')_\mu)_\mu  $ '
                    return False,logs
    logs += 'El grupoide es Asociativo $((a,b)_\mu,c)_\mu = (a,(b,c)_\mu)_\mu$'
    return True,logs


def is_grupoid(table,sett,op):
    logs = ''
    for i in range(len(table)):
        for j in range(len(table)):
                if table[i,j] in sett:
                    continue
                else:
                    logs += 'La operacion no es cerrada: \n'
                    logs += str(table[i,j]) + r'  $\notin$  {' + str(sett[0])+r', ... ,'+str(sett[-1])+'}\n'
                    return False,logs
    logs+= '''
        El par $(G,\mu)$ es un grupoide.


    '''
    isc = is_conmutative(table,sett,op)

    logs+= isc[1]+ r'''


    '''

    isas = is_asociative(sett,op)
    logs+= isas[1]
    return True,logs




r = st.text_input('Ingrese los elementos :','{0,1,2,3,4}')
fx = st.text_input('Ingrese la operacion binaria','(x+y)%2')

try:
    st.latex(r'\mu: G^{2} \rightarrow G')
    binop = sp.parse_expr(fx)
    lop = sp.lambdify(list(binop.free_symbols),binop)
    st.latex(sp.latex(binop)+r' \rightarrow G')
except:
    pass


if len(r) > 0:
    st.write('$$ G = \{'+r+'\} $$')
else:
    st.write('$$ G = \emptyset $$')

if '...' in r:
    #st.write(':)')
    nums=list(re.split('[^-0-9*]',r))

    b0 = 0
    b1 = 0
    for c in nums:
        if len(c)==0:
            continue
        else:
            if b0 == 0:
                b0 = int(c)
            else:
                b1 = int(c)

    li = list(map(str,list(range(b0,b1+1))))
    try:
        opmat = [[lop(i,j) for i in list(map(int,li))] for j in list(map(int,li))]
    except:
        opmat = np.zeros((len(li),len(li)))
else:
    li = list(re.split('[^-0-9*]',r))
    del li[0],li[-1]
    try:
        opmat = [[lop(i,j) for i in list(map(int,li))] for j in list(map(int,li))]
    except:
        opmat = np.zeros((len(li),len(li)))

st.write(li)
cols = [i for i in li]
mat1 = pd.DataFrame(opmat,columns=cols,index=cols)
st.write('Ingrese la matriz:')
mat2 = st.data_editor(mat1)






m = [[(sp.Matrix(mat2))[i,j] for j in range(len(li))] for i in range(len(li))]
if len(li)< 10:
    st.latex('A = ' + sp.latex(sp.Matrix(m)))
if st.button('Es grupoide?'):
    ans = is_grupoid(np.array(m),np.array(list(map(int,li))),lop)
    if ans[0]:
        st.write('Verdadero')
    else:
        st.write('Falso')
    with st.expander('Mostrar registro'):
        st.write(ans[-1])
