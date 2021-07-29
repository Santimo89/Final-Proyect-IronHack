
import pandas as pd 
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map
import plotly.express as px
import h2o



def load_data():
    df = pd.read_csv("ModeloSurf.csv")
    return df

def user_input_features():
    """
    Function to save the info that the user give in the app
    Args: 
        non receive parameters
    Returns:
        A dataframe with the characteristcs given by the user
    """
    Temperatura_del_agua = st.sidebar.slider('Temp_Agua', 10, 24, 17) # the sidebar.slider magic function receive the max, min and default value in out sidebar
    Precipitacion = st.sidebar.slider('Precipitacion', 20, 200, 60)
    Temperatura_ambiente = st.sidebar.slider('Temp_ambiente', 7, 30, 18)
    Periodo_medio_Ola = st.sidebar.slider('Periodo', 4, 16, 12)
    data = {'Temperatura del AguaºC': Temperatura_del_agua,
            'prec': Precipitacion,
            'tmed': Temperatura_ambiente,
            'Periodo_Medio': Periodo_medio_Ola}

    return pd.DataFrame(data, index=[0])

def playas():
    inicial_lat = 44.01
    inicial_long = -4.21
    Norte_España = folium.Map(location = [inicial_lat, inicial_long], zoom_start = 7.4)
     
    Playa_de_Razo_lat = 43.2833
    Playa_de_Razo_long = -8.7166
    Playa_de_Doniños_lat = 43.5
    Playa_de_Doniños_long = -8.317
    Playa_de_Pantín_lat = 43.633
    Playa_de_Pantín_long = -8.1000
    Playa_de_Peñarronda_lat = 43.5516
    Playa_de_Peñarronda_long = -7.0012
    Playa_de_Cadavedo_lat = 43.5519
    Playa_de_Cadavedo_long = -6.3718
    Playa_de_Salinas_lat = 43.5790
    Playa_de_Salinas_long = -5.9577
    Playa_de_Vega_lat = 43.4797
    Playa_de_Vega_long = -5.1395
    Playa_de_Ribadesella_lat = 43.4615
    Playa_de_Ribadesella_long = -5.0591
    Playa_de_Suances_lat = 43.4270
    Playa_de_Suances_long = -4.0606
    Playa_de_La_Maruca_lat = 43.4796
    Playa_de_La_Maruca_long = -3.8364
    Playa_de_Zarautz_lat = 43.2888
    Playa_de_Zarautz_long = -2.1636
    Playa_de_Mundaka_lat = 43.4072
    Playa_de_Mundaka_long = -2.6983
    Playa_de_Plentzia_lat = 43.4111
    Playa_de_Plentzia_long = -2.9461
    Playa_de_Razo = Marker(location = [Playa_de_Razo_lat, Playa_de_Razo_long], tooltip = "Playa de Razo")
    Playa_de_Razo.add_to(Norte_España)
    Playa_de_Doniños = Marker(location = [Playa_de_Doniños_lat, Playa_de_Doniños_long], tooltip = "Playa de Doniños")
    Playa_de_Doniños.add_to(Norte_España)
    Playa_de_Pantín = Marker(location = [Playa_de_Pantín_lat, Playa_de_Pantín_long], tooltip = "Playa de Pantín")
    Playa_de_Pantín.add_to(Norte_España)
    Playa_de_Peñarronda = Marker(location = [Playa_de_Peñarronda_lat, Playa_de_Peñarronda_long], tooltip = "Playa de Peñarronda")
    Playa_de_Peñarronda.add_to(Norte_España)
    Playa_de_Cadavedo = Marker(location = [Playa_de_Cadavedo_lat, Playa_de_Cadavedo_long], tooltip = "Playa de Cadavedo")
    Playa_de_Cadavedo.add_to(Norte_España)
    Playa_de_Salinas = Marker(location = [Playa_de_Salinas_lat, Playa_de_Salinas_long], tooltip = "Playa de Salinas")
    Playa_de_Salinas.add_to(Norte_España)
    Playa_de_Vega = Marker(location = [Playa_de_Vega_lat, Playa_de_Vega_long], tooltip = "Playa de Vega")
    Playa_de_Vega.add_to(Norte_España)
    Playa_de_Ribadesella = Marker(location = [Playa_de_Ribadesella_lat, Playa_de_Ribadesella_long], tooltip = "Playa de Ribadesella")
    Playa_de_Ribadesella.add_to(Norte_España)
    Playa_de_Suances = Marker(location = [Playa_de_Suances_lat, Playa_de_Suances_long], tooltip = "Playa de Suances")
    Playa_de_Suances.add_to(Norte_España)
    Playa_de_La_Maruca = Marker(location = [Playa_de_La_Maruca_lat, Playa_de_La_Maruca_long], tooltip = "Playa de La Maruca")
    Playa_de_La_Maruca.add_to(Norte_España)
    Playa_de_Zarautz = Marker(location = [Playa_de_Zarautz_lat, Playa_de_Zarautz_long], tooltip = "Playa de Zarautz")
    Playa_de_Zarautz.add_to(Norte_España)
    Playa_de_Mundaka = Marker(location = [Playa_de_Mundaka_lat, Playa_de_Mundaka_long], tooltip = "Playa de Mundaka")
    Playa_de_Mundaka.add_to(Norte_España)
    Playa_de_Plentzia = Marker(location = [Playa_de_Plentzia_lat, Playa_de_Plentzia_long], tooltip = "Playa de Plentzia")
    Playa_de_Plentzia.add_to(Norte_España)
    Boya_Galicia1_lat = 43.50
    Boya_Galicia1_long = -9.21
    Boya_Galicia2_lat = 44.12
    Boya_Galicia2_long = -7.68
    Boya_Asturias1_lat = 43.75
    Boya_Asturias1_long = -6.18
    Boya_Asturias2_lat = 43.62
    Boya_Asturias2_long = -5.66
    Boya_Cantabria1_lat = 43.59
    Boya_Cantabria1_long = -3.84
    Boya_PaísVasco1_lat = 43.64
    Boya_PaísVasco1_long = -3.04
    Boya_PaísVasco2_lat = 43.31
    Boya_PaísVasco2_long = -2.16
    Boya_Galicia1 = Marker(location = [Boya_Galicia1_lat, Boya_Galicia1_long], tooltip="Boya de Villano-Sisargas")
    Boya_Galicia1.add_to(Norte_España)
    Boya_Galicia2 = Marker(location = [Boya_Galicia2_lat, Boya_Galicia2_long], tooltip="Boya de Estaca de Bares")
    Boya_Galicia2.add_to(Norte_España)
    Boya_Asturias1 = Marker(location = [Boya_Asturias1_lat, Boya_Asturias1_long], tooltip="Boya de Cabo Peñas")
    Boya_Asturias1.add_to(Norte_España)
    Boya_Asturias2 = Marker(location = [Boya_Asturias2_lat, Boya_Asturias2_long], tooltip="Boya de Gijón")
    Boya_Asturias2.add_to(Norte_España)
    Boya_Cantabria1 = Marker(location = [Boya_Cantabria1_lat, Boya_Cantabria1_long], tooltip="Punto SIMAR 3135036 Santander")
    Boya_Cantabria1.add_to(Norte_España)
    Boya_PaísVasco1 = Marker(location = [Boya_PaísVasco1_lat, Boya_PaísVasco1_long], tooltip="Boya de Bilbao")
    Boya_PaísVasco1.add_to(Norte_España)
    Boya_PaísVasco2 = Marker(location = [Boya_PaísVasco2_lat, Boya_PaísVasco2_long], tooltip="Punto SIMAR 3176032 Zarautz")
    Boya_PaísVasco2.add_to(Norte_España)
    
    return folium_static(Norte_España)

def info_mar():
    return pd.read_csv("ModeloSurf.csv")

 
def grafica_temp():
    df = info_mar()
    df = df.groupby(["Año_left"]).agg("mean").reset_index()
    print(df)
    return px.line(df, x='Año_left', y = "Temperatura del AguaºC", title = "Evolución de la temperatura")

def grafica_ola():
    df = info_mar()
    df = df.groupby(["Año_left"]).agg("mean").reset_index()
    print(df)
    return px.line(df, x='Año_left', y = "Altura_Media_Ola", title = "Evolución de la altura de la ola")

def grafica_temp_ambiente():
    df = info_mar()
    df = df.groupby(["Año_left"]).agg("mean").reset_index()
    print(df)
    return px.line(df, x='Año_left', y = "tmed", title = "Evolución de la altura de la temperatura ambiente")

def predicccion_olas(df):
    h2o.init()
    saved_model = h2o.load_model("XGBoost_1_AutoML_20210729_224845")
    h2o_df = h2o.H2OFrame(df)
    predictions = saved_model.predict(h2o_df)
    #h2o_df["prediction"] = predictions
    #final_df = h2o_df.as_data_frame()

    return predictions