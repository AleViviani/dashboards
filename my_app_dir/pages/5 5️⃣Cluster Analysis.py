import streamlit as st
import numpy as np
import os
from PIL import Image

from Sidebar import sidebar1, sidebar2

st.session_state.update(st.session_state)

st.set_page_config(layout="wide")

st.header('Cluster analysis')
st.write('Visualize images of each clusters to compare them')

with st.sidebar:
    sidebar1()
    sidebar2()

compute_button = st.button("Compute")

if compute_button:
    for cluster, col in zip(np.unique(st.session_state['clusters']), st.columns(np.unique(st.session_state['clusters']).size)):
        with col:
            st.title('#' + str(cluster))
            for _, row in st.session_state['df_embedding'].iterrows():
                if row.clusters == cluster:

                    image = Image.open(os.path.join(st.session_state['DATA_FOLDER'], row.gen_path))
                    st.image(image, caption=row.image)