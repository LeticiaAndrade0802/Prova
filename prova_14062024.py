import pandas as pd  
import matplotlib.pyplot as plt
import streamlit as st


st.header("Dados da empresa 1")
 
arquivo = "https://github.com/LeticiaAndrade0802/Prova/blob/main/empresa1.csv" 
dfe = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe.head(3))

arquivo = "projetos.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.head(23)

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st(df.tail())

colunas = ['Projeto1', 'Projeto2', 'Projeto3', 'Projeto4', 'Projeto5']
st.groupby('ano')[colunas].sum()


