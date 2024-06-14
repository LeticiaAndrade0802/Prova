import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt


st.header("Dados da Empresa")

st.set_page_config(page_title="Prova",)

st.code(code, language='python')
 
arquivo = "https://raw.github.com/LeticiaAndrade0802/Prova/blob/main/projetos%20(1).csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dfe(head(23))


df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st(df1.tail())

fig, ax = colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.groupby('ano')[colunas].sum()
st.pyplot(fig)

df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', color='darkgreen', marker='*')
st.pyplot.show()

df["Projeto1"].plot(kind = 'hist')
df["Projeto4"].plot(kind = 'hist')
plt.show()
st.pyplot(df)

st.list_series('Selic')

selic = ip.timeseries('BM12_TJOVER12', yearGreaterThan=2021, yearSmallerThan=2024)
st.selic

ip.timeseries('BM12_TJOVER12', year=2021).plot("MONTH", "VALUE ((% a.m.))")
ip.timeseries('BM12_TJOVER12', year=2022).plot("MONTH", "VALUE ((% a.m.))")
st.plt.show()


