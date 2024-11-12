import streamlit as st
import pandas as pd
import numpy as np


# Récupération des données depuis un fichier csv
df = pd.read_csv("./car_prices_clean.csv", delimiter = ',', encoding='utf-8')

# Affichage des données
#st.dataframe(df)

# Menu déroulant des colonnes
colonnes = st.selectbox( 'Trier sur cette colonne :', ['year', 'make', 'model', 'trim', 'body', 'transmission', 'state', 'condition', 'odometer'], index = None, placeholder = 'Choisir une colonne' ) # enlever valeur par défaut

# Menu déroulant ascendant/descendant
asc_desc = st.selectbox('Type de tri', ['Croissant', 'Décroissant'], index = None, placeholder = 'Choisir un ordre')

# Tri selon la colonne sélectionnée
if colonnes == None :
    st.dataframe(df)
elif colonnes :
    df = df.sort_values(by = colonnes)

    # Tri selon croissant/décroissant
    if asc_desc == 'Décroissant':
        df = df.sort_values(by = colonnes, ascending = False)

    st.write(df)