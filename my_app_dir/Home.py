# Streamlit libraries
import streamlit as st

st.session_state.update(st.session_state)

st.set_page_config(layout="wide")

# Initialize Session State Variables

if 'DATA_FOLDER' not in st.session_state:
    st.session_state['DATA_FOLDER'] = "data"

if 'EMBEDDINGS_FILE' not in st.session_state:
    st.session_state['EMBEDDINGS_FILE'] = "embeddings.json"

if 'METADATA_FILE' not in st.session_state:
    st.session_state['METADATA_FILE'] = "metadata.json"

if 'LABELS_FILE' not in st.session_state:
    st.session_state['LABELS_FILE'] = "labels.json"

if 'IMAGES_FOLDER' not in st.session_state:
    st.session_state['IMAGES_FOLDER'] = "images"

if 'GENERATED_FOLDER' not in st.session_state:
    st.session_state['GENERATED_FOLDER'] = "generated"


st.title("Home")

neanias = "https://www.neanias.eu/"
eosc = "https://eosc-portal.eu/"

st.write("""This web app is related to [NEANIAS](%s), an ambitious project to face the challenges proposed by the
        European Open Science Cloud ([EOSC](%s)) program. 
        \n[NEANIAS](%s) promotes Open Science practices and plays an active role in the delivery of innovative 
        services in three major sectors: Underwater research, Atmospheric research and Space research, each 
        engaging many academic and business groups, numerous researchers, professionals and governmental entities.
        """ % (neanias, eosc, neanias))

st.markdown("#### This Web App: ")
st.write("""This web app allows you to analyze a dataset of images through various unsupervised machine learning 
        procedures. 
        \nIn the sidebar on the left are listed the pages composing the app. Navigate through them from top to bottom
        to choose with which dataset work and set parameters and methods to appply. 
        
        """)




