from cProfile import label
import numpy
import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

st.title("Title")
st.subheader("Subheader")
st.header("Header")
st.text("Text paragraph")
st.markdown("**Bold**, *italic*, ***B+I*** \n # H1 \n ## H2 \n ### H3 \n > blockquote")
st.markdown("1. Lista \n 2. Lista \n - Lista non ordinata \n - Lista non ordinata")
st.markdown("`code` \n \n --- \n [Titolo Link](https://www.example.com)")
st.caption("Caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
jsonExample={"a":"1,2,3","b":"4,5,6"}
st.json(jsonExample)
codeExample = """
print("Hello world")
def funct():
    return 0;
"""
st.code(codeExample, language="python")

st.metric(label="Wind speed", value="120 m/s", delta="2 m/s")
tableExample=pd.DataFrame({"Colonna 1":[1,2,3],"Colonna 2":[4,5,6]})
st.table(tableExample)
st.dataframe(tableExample)
st.image("logo.jpg", caption='Caption for image', width=500)
checkboxExample=st.checkbox(label="Label checkbox", value=False)
if checkboxExample:
    st.write("It's checked")
else:
    st.write("It's not checked")

def changeCheckBox():
    #print("Changed")
    print(st.session_state.checkerKey)

checkboxExample2=st.checkbox(label="On_change checkbox", value=False, on_change=changeCheckBox, key="checkerKey")

radio_btn = st.radio(label="Label radio button", options=("option a","option b","option c"))
st.write("You chose: " + radio_btn)
btn = st.button(label="Regular button")
selectBox = st.selectbox(label="Label select box", options=("option a","option b","option c"))
multiSelect=st.multiselect(label="Label multiselect box: select one or more", options=("option a","option b","option c"))

imageUploaded = st.file_uploader(label="Upload one or more images", type=["png", "jpg"], accept_multiple_files=True)
if imageUploaded is not None:
    st.image(imageUploaded)

st.slider(label="Label slider", min_value=50, max_value=150, value=69)
st.select_slider(label="Label select-slider", options=[1,2,3,4,5])
st.text_input(label='Text-input label', max_chars=55)
st.text_area(label='Text-area label')
st.date_input(label='Date input label')

def converter(value):
    m,s,mm=value.split(':')
    t_s = int(m)*60+int(s)+int(mm)/1000
    return t_s
valTimer=st.time_input(label='Set Timer', value=time(0,0,0))
if str(valTimer) == '00:00:00':
    st.write('Please set timer > 0')
else: 
    sec=converter(str(valTimer))
    bar=st.progress(0)
    per=sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1)+' %')
        ts.sleep(per)

formExample = st.form('Form 1', clear_on_submit=True)
nameExample=formExample.text_input('Nome e Cognome:')
s_state=formExample.form_submit_button('Submit')
if s_state:
    if nameExample=='':
        st.warning('Nome e cognome vuoti')
    else:
        st.success('Submitted succesfully')


with st.form('Form 2'):
    col1,col2 = st.columns(2)
    col1.text_input(label='Città')
    col2.text_input(label='Data nascita')
    st.text_input('Indirizzo:')
    st.form_submit_button('Submit')

st.sidebar.write('This is my sidebar')
figExample = plt.figure() 
x=np.linspace(0,10,100)
plt.style.use('default')
plt.plot(x, np.sin(x))
st.write(figExample)
optGraphSide=st.sidebar.radio('Select a graph', options=('Cos(x)', 'Bar', 'H-Bar'))
bar_x=np.array([1,2,3,4,5])
if optGraphSide =='Cos(x)':
    st.markdown("<h3 style = 'text-align: center;' >Cos chart:</h3>", unsafe_allow_html=True)
    figExample2 = plt.figure() 
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.plot(x, np.cos(x), '--')
    st.write(figExample2)
elif optGraphSide =='Bar':
    st.markdown("<h3 style = 'text-align: center;' >Bar chart:</h3>",unsafe_allow_html=True)
    figExample2 = plt.figure() 
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.bar(bar_x, bar_x*10)
    st.write(figExample2)
else:
    st.markdown("<h3 style = 'text-align: center;' >Bar chart Horizontal:</h3>", unsafe_allow_html=True)
    figExample2 = plt.figure() 
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.barh(bar_x*10, bar_x)
    st.write(figExample2)