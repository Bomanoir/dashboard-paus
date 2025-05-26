import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Opportunités Immobilières", layout="wide")

st.title("📊 Top 100 Opportunités Immobilières - Bomanoir")
st.markdown("Données extraites automatiquement via le bot Bomanoir basé sur athome.lu")

uploaded_file = "top_100.xlsx"

@st.cache_data
def load_data():
    df = pd.read_excel(uploaded_file)
    return df

df = load_data()

# Filtres interactifs
zones = st.multiselect("Zone prioritaire", options=df["Zone prioritaire"].unique(), default=df["Zone prioritaire"].unique())
renov = st.selectbox("À rénover ?", options=["Tous", "Oui", "Non"])
combles = st.selectbox("Combles aménageables ?", options=["Tous", "Oui", "Non"])
min_score = st.slider("Score minimum", 0, 100, 20)

# Application des filtres
filtered_df = df[
    (df["Zone prioritaire"].isin(zones)) &
    ((df["À rénover"] == renov) if renov != "Tous" else True) &
    ((df["Combles aménageables"] == combles) if combles != "Tous" else True) &
    (df["Score"] >= min_score)
]

st.dataframe(filtered_df, use_container_width=True)