cialities# Sección de importación de módulos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from Modules.UI.Header import show_header
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.hierarchy import fcluster

# =========================================================
# === 1. DEFINICIÓN DE COLUMNAS ===
# =========================================================

COFFEE_COLUMNS = ['Wine',
    'Cocktails',
    'Drinks',
    'Mocktails',
    'Specialities',
    'Destillates']

# Seción para crear la GUI
show_header("Name of Your Event")

url = 'https://raw.githubusercontent.com/Roby20030202/BI_FINAL_PROJECT/refs/heads/main/filtered_yelp_NJ.csv'
# url_mapa ya no es necesario

df = pd.read_csv(url,index_col=0)

# definiendo columnas del dataset
df =  COFFEE_COLUMNS


# Aseguramos que el DataFrame principal solo contenga negocios relevantes


# =========================================================
# === 2. WIDGETS DE FILTRADO ===
# =========================================================

st.sidebar.title("Opciones de Filtrado")

# WIDGET 1: Filtro por Tipo de Establecimiento (MULTISELECT)
categorias_seleccionadas = st.sidebar.multiselect(
    '1. Selecciona el Tipo de Bebida:',
    options=COFFEE_COLUMNS, 
    default=[COFFEE_COLUMNS[0]] # Selecciona 'Coffee & Tea' por defecto
)

# WIDGET 2: Filtro por Estrellas (Slider)
min_stars = st.sidebar.slider(
    'Alcohol Content:',
    min_value=0.0, 
    max_value=10.0, 
    value=3.5, # Valor por defecto
    step=0.5  
)

# =========================================================
# === 3. APLICACIÓN DEL DOBLE FILTRO (Lógica ajustada) ===
# =========================================================

# Manejar el caso donde no hay categorías seleccionadas
st.image("image_bi/bar_menu.jpg", width = 500)

st.write("What do you want to order?")

checked = st.checkbox("Wine")

checked_b = st.checkbox("Cocktail")

checked_c = st.checkbox("Mocktail")

checked_d = st.checkbox("Specialities")

if checked:
    st.write("You selected Wine!")
elif checked_b:
    st.write("You selected Cocktail!")
elif checked_b:
    st.write("You selected Mocktail!")
elif checked_b:
    st.write("You selected Specialities!")
else:
    st.write("You have not select anything yet.")
