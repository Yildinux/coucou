import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Récupération des données depuis un fichier csv
df = pd.read_csv("./car_prices_clean.csv", delimiter = ',', encoding='utf-8')

##########################################################################################################################
# Implémenter la fonctionnalité de tri du jeu de données
##########################################################################################################################


# Menu déroulant des colonnes
colonnes = st.selectbox( 'Trier sur cette colonne :', ['year', 'make', 'model', 'trim', 'body', 'transmission', 'state', 'condition', 'odometer', 'color', 'interior', 'seller', 'mmr', 'sellingprice','saledate'], index = None, placeholder = 'Choisir une colonne' ) # enlever valeur par défaut

# Menu déroulant ascendant/descendant
asc_desc = st.selectbox('Type de tri', ['Croissant', 'Décroissant'], index = None, placeholder = 'Choisir un ordre')

# Tri selon la colonne sélectionnée
if colonnes :
    df = df.sort_values(by = colonnes)

    # Tri selon croissant/décroissant
    if asc_desc == 'Décroissant':
        df = df.sort_values(by = colonnes, ascending = False)

 

##########################################################################################################################
# Implémenter les fonctionnalités de filtre des lignes 
##########################################################################################################################
 

# Filtrer les lignes 

# On change le type de la colonne 'make'
df['make'] = df['make'].astype('category')

#print(df.dtypes)


# Création du input pour la marque et pour le modèle
input_mark = st.text_input ('Marque du véhicule')
if input_mark :
    df = df[df['make'].isin([input_mark])]          # si la valeur dans la colonne est = à la valeur renseignée dans l'input c'est True  +  filtre du df pour filtrer les lignes
    print(df)

    if df.empty :
        st.error(f"Cette marque n'existe pas dans la base")
    else: 
        print("Entrée input marque valide") 
else: 
    print("Marque filtrée")


input_model = st.text_input ('Modèle du véhicule')
if input_model :
    df = df[df['model'].isin([input_model])]
    if df.empty :
        st.error(f"Ce modèle n'existe pas dans la base")
    else: 
        print("Entrée input modèle valide") 
else: 
    print("Modèle filtré")



# Création du input pour le prix
min_price = df['sellingprice'].min()
max_price = df['sellingprice'].max()

input_price = st.slider('Prix', min_value=min_price, max_value=max_price, value=[min_price, max_price])

if input_price :
    df = df[df['sellingprice'].between(input_price[0], input_price[1], inclusive='neither')]

# Creation du input pour les kilometres
min_klm = df['odometer'].min()
max_klm = df['odometer'].max()

input_klm = st.slider('km', min_value=min_klm, max_value=max_klm, value=[min_klm, max_klm])
 
if input_klm:
    df = df[df['odometer'].between(input_klm[0], input_klm[1], inclusive='neither')]

# Création du input pour la date de vente


    # Changement du type
#print(df.dtypes)
df['saledate'] = pd.to_datetime(df['saledate'])
#print(df.dtypes)

   
    # Affichage de la date de vente sans l'heure
column_config = {
    "saledate": st.column_config.DateColumn(
            "saledate",
            help="Date de la vente du véhicule",
            format="DD.MM.YYYY",
            step=1,
        ),
}
df['saledate'] = df['saledate'].dt.tz_localize(None)

min_date = df['saledate'].min()
max_date = df['saledate'].max()

input_date = st.date_input ('Choisir la date de vente', value = [min_date, max_date], format = 'DD.MM.YYYY')
if input_date:
    start_date = pd.to_datetime(input_date[0])
    end_date = pd.to_datetime(input_date[1])
    
    df_filtered = df[df['saledate'].between(start_date, end_date, inclusive='neither')]


st.dataframe(df, use_container_width=True, height=600, 
             hide_index=True,
             column_config=column_config)
    

    # Input
