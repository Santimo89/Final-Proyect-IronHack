

import streamlit as st
from PIL import Image
from support import load_data, user_input_features, playas, info_mar, grafica_temp, grafica_ola, grafica_temp_ambiente, predicccion_olas



st.write("""
# Prediciones Surf
""")

st.text(""" El principal objetivo de este proyecto es predecir, según algunas variables el mejor mes y comunidad, para ir a surfear al norte de España""")


col1, col2 = st.beta_columns(2)
with col1:
    image = Image.open("Surf_pic.jpg")
    st.image(image, use_column_width = True)

with col2:
    image = Image.open("Sol_Riba.jpg")
    st.image(image, use_column_width = True)


st.sidebar.header('User Input Parameters')
df = user_input_features()
st.table(df)

x = load_data()


st.table()


playas()

st.plotly_chart(grafica_temp())
st.plotly_chart(grafica_ola())
st.plotly_chart(grafica_temp_ambiente())
#st.dataframe(predicccion_olas(df))
