import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import re
from itertools import permutations








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
st.subheader(':triangular_ruler:')
def is_conmutative(sett,op):
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
                if op(sett[i],sett[j]) == op(sett[j],sett[i]):
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
    isc = is_conmutative(sett,op)

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
