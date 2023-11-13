import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title('Barra Lateral e Gráficos')
st.markdown('---')
st.sidebar.header('Tipos de gráficos')
graficos=('Linha','Barras','Barras Horizontais')
GRAF=st.sidebar.radio('Selecione um gráfico',options=graficos)
if GRAF=='Linha':
    x=np.linspace(0,1,1000)
    y1=np.sin(2*np.pi*x)
    y2=np.cos(2*np.pi*x)
    st.header('Gráfico de Linha (ou Série Temporal)')
    fig=plt.figure(figsize=(8,4))
    plt.style.use('ggplot')
    plt.plot(x,y1)
    plt.plot(x,y2,'--')
    st.write(fig)
elif GRAF=='Barras':
    x=np.array([2,4,6,8,10])
    y=10*x
    st.header('Gráfico de Barras')
    fig=plt.figure(figsize=(4,2))
    plt.style.use('ggplot')
    plt.bar(x,y)
    st.write(fig)
else:
    x=np.array([2,4,6,8,10])
    y=10*x
    st.header('Gráfico de Barras Horizontais')
    fig=plt.figure(figsize=(4,2))
    plt.style.use('ggplot')
    plt.barh(x,y)
    st.write(fig)
with st.expander('Clique para saber mais!'):
    st.write('Esse texto fica escondido até que o usuário o chame')