import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import re
from itertools import permutations
st.subheader(':triangular_ruler:')

with open( "styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


def is_conmutative(sett,op):
    logs = ''
    for i in range(len(sett)):
        for j in range(len(sett)):
                if op(sett[i],sett[j]) == op(sett[j],sett[i]):
                    continue
                else:
                    logs += 'El grupoide no es conmutativo: \n'
                    logs +=r'$( '+ str(sett[i])+','+str(sett[j])+')_\mu  \noteq  '+r'( '+ str(sett[j])+','+str(sett[i])+')_\mu  $ '
                    return False,logs
    logs += 'El grupoide es conmutativo'
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
    return True,logs+isc[-1]




r = st.text_input('Ingrese los elementos :','{1,2,3}')
fx = st.text_input('Ingrese la operacion binaria','x+y')

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
