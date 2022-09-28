# Streamlit libraries
import streamlit as st
st.session_state.update(st.session_state)

#if "prova" not in st.session_state:
 #   st.session_state["prova"]=25

slider = st.slider(label='How old are you?', min_value=0, max_value=130, value=25, key="prova")
st.write(st.session_state.prova)
st.write(slider)