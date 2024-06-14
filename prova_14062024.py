import pandas as pd  
import ipeadatapy as ip
import streamlit as st
 
st.header("Dados da empresa 14 06 2024")
 
arquivo = "https://raw.githubusercontent.com/LeticiaAndrade0802/prova/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))
 
fig, ax = plt.subplots()
dfe.plot(ax=ax)
st.pyplot(fig)
 
fig, ax = plt.subplots()
dfe.plot(kind = 'scatter', x = 'EBITDA', y = 'Lucro operacional',ax=ax)
st.pyplot(fig)
 
fig, ax = plt.subplots()
dfe["Lucro do período"].plot(kind = 'hist')
st.pyplot(fig)
 
 
st.write(dfe.groupby('Ano').mean())
