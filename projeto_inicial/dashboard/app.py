import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de VENDAS", layout="wide")
st.title("Dashboard de Performance")

try:
    df = pd.read_csv("date/dados_vendas.csv")

    total_leads = df["Leads"].sum()
    media_leads = df["Leads"].mean()

    col1, col2 = st.columns(2)
    col1.metric("Total de Leads", total_leads)
    col2.metric("Média Diária", f"{media_leads:.1f}")

    st.subheader("Evolução no Tempo")
    st.bar_chart(df, x="Data", y="Leads")

except FileNotFoundError:
    st.error('Rode o script de automação primeiro!')
