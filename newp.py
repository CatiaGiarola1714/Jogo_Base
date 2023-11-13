import streamlit as st
st.title('Título')
st.header('Cabeçalho')
st.subheader('Subcabeçalho')
st.text('Texto')
st.markdown('*Aceita* **formatação** do ***Markdown***')
st.markdown('---')
st.markdown('# :orange[Título]')
st.markdown('## :blue[Subtítulo]')
st.markdown('### :violet[Texto]')
st.markdown('---')
st.latex(r'\Delta = b^2-4*a*c')
st.latex(r'x_{1,2}=\frac{-b\pm \sqrt{\Delta}}{2*a}')
code='''
import numpy as np
rpint('Olá Mundo')
def sen(x):
    a=np.sin(x)
    return a
print(sen(30))
'''
st.code(code,language='python')
st.markdown('---')
st.markdown('[Google](https://www.google.com)')