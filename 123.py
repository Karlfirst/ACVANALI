print('Hello Streamlit')
 
import streamlit as st
#cd C:\Users\Admin\Desktop\bigdata\lll.py
st.write("Hello,world! This is a Streamlit app.")
 
st.title("My streamlit App")
st.subheader("Try out the app!")
st.text("This is a simple text element")
 
#Choix dans une list déroulante (dans la sidebar)
graph_type = st.selectbox("Choissisez un type de graphique:",["Ligne","Barres","Aucun"])
 
st.write(f"Vous avez choisi le type de graphique: {graph_type}")
 
#3 UPLOAD CSV FILE
uploaded_file = st.file_uploader("📁 Téléchargez un fichier CSV", type=["csv"])
 
if uploaded_file is not None:
 
    #4 Dispaly panda dataframe
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())
 
    #5 Affichage du graphique en fonction du type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres":
        st.bar_chart(df)
    else:
        st.write("Aucun graphique sélectionné.")
st.write("Merci d'avoir utilisé notre application Streamlit !")

#4 display du graphique en fonction
age=st.slider('quel age vous avez', 0, 100, 25)
st.write(f'vous avez {age} ages,')
import pandas as pd
import numpy as np

#checkbox
if st.checkbox('afficher en tableau aleatoire'):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A','B','C']))