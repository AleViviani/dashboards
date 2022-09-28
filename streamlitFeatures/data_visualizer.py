import streamlit as st
import pandas as pd

st.markdown("<h3 style = 'text-align: center;' >Data visualizer</h3>", unsafe_allow_html=True)
st.markdown('---')
file_names=list()
filesEx = st.file_uploader('Upload Multiple files', type=['xlsx'], accept_multiple_files=True)
if filesEx:
    for file in filesEx:
        file_names.append(file.name)
    selected_files = st.multiselect(label='Select files', options=file_names)
    if selected_files:
        option = st.radio(label='Select Entity Against date', options=['None','GPU', 'CPU'])
        if option !='None':
            for file in filesEx:
                if file.name in selected_files:
                    shop_data = pd.read_excel(file, index_col=0)
