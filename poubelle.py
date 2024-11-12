import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime 
import datetime

# Récupération des données depuis un fichier csv
df = pd.read_csv("./car_prices_clean.csv", delimiter = ',', encoding='utf-8')

# Affichage des données
#st.dataframe(df)

# Menu déroulant des colonnes
colonnes = st.selectbox( 'Trier sur cette colonne :', ['year', 'make', 'model', 'trim', 'body', 'transmission', 'state', 'condition', 'odometer', 'color', 'interior', 'seller','mmr','sellingprice','saledate'], index = None, placeholder = 'Choisir une colonne' ) # enlever valeur par défaut

# Menu déroulant ascendant/descendant
asc_desc = st.selectbox('Type de tri', ['Croissant', 'Décroissant'], index = None, placeholder = 'Choisir un ordre')

input_mark = st.text_input("Marque du vehicule : ").lower()

if input_mark :
    df = df[df['make'].isin([input_mark])]




#finito pipo
input_modele = st.text_input("Modele du vehicule : ")

if input_modele : 
    df = df[df['model'].isin ([input_modele])]
#probleme numpy
#input_prix = st.slider("test :" , value=[df['sellingprice'].min(),df['sellingprice'].max()])
#if input_prix :
  # df = df[df['sellingprice'].isin ([input_prix])]

# Tri selon la colonne sélectionnée
if colonnes == None :
    st.dataframe(df)
elif colonnes :
    df = df.sort_values(by = colonnes)

    # Tri selon croissant/décroissant
    if asc_desc == 'Décroissant':
        df = df.sort_values(by = colonnes, ascending = False)

    st.wrte(df)



df['make'] = df.make.astype('category')
df['saledate'] = pd.to_datetime(df['saledate'], errors = 'coerce')

print(df.dtypes)



#[df['sellingprice'].min(),df['sellingprice'].max()]



# Affichage de la date de vente sans l'heure
column_config = {
    "saledate": st.column_config.DateColumn(
            "saledate",
            help="Date de la vente du véhicule",
            format="DD.MM.YYYY",
            step=1,
        ),
}
st.dataframe(df, use_container_width=True, height=600, 
             hide_index=True,
             column_config=column_config)

min_date = df['saledate'].min()
max_date = df['saledate'].max()

#input_date = st.date_input(
    #"entre quelle date ",value = [min_date , max_date] , format ='DD.MM.YYYY')



