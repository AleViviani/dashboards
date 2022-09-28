# Streamlit libraries
import streamlit as st
st.session_state.update(st.session_state)

if "prova" not in st.session_state:
    st.session_state["prova"]=25

st.write(st.session_state["prova"])

btn = st.button(label="Write current session state value")

if btn:
    st.write(st.session_state["prova"])


add_btn = st.button(label="Add 5 to current session state value")
if add_btn:
    st.session_state["prova"] += 5
    st.write(st.session_state["prova"])