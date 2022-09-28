# Streamlit Libraries
import streamlit as st

# File Processing Libraries
from PIL import Image
import json

# Explore File System Libraries
import os

st.session_state.update(st.session_state)


st.set_page_config(layout="wide")

# Function to cache images:
# @st.experimental_memo()
@st.cache(hash_funcs={'_json.Scanner': hash})
def load_image(image):
    img = Image.open(image)
    return img




st.header("Experiment Selection")
st.write("In this page you can choose which dataset will be analyzed.\
        \nDone that, select the next page in the sidebar to configure process settings.")

st.write("Example Datasets to use: ")

experiments = {}
for experiment in os.listdir(st.session_state['DATA_FOLDER']):
    print(experiment)
    if os.path.isdir(os.path.join(st.session_state['DATA_FOLDER'], experiment)):
        # Better in a dictionary with metadata
        with open(os.path.join(st.session_state['DATA_FOLDER'], experiment, st.session_state['METADATA_FILE']), "r") as file:
            metadata = json.load(file)
            experiments[experiment] = metadata
            experiments[experiment]["path"] = os.path.join(
                st.session_state['DATA_FOLDER'], experiment, st.session_state['METADATA_FILE'])

example_experiment = st.selectbox('Choose a data folder', tuple(experiments), key="example_experiment")
st.session_state['EXPERIMENT_FOLDER'] = os.path.join(st.session_state['DATA_FOLDER'], example_experiment)

columns = st.columns(9)

with columns[0]:
    st.write("**Name**")
    st.write(str(experiments[example_experiment]["name"]))
with columns[1]:
    st.write("**Image Size**")
    st.write("{} x {}".format(str(experiments[example_experiment]["image"]["dim"]), str(
        experiments[example_experiment]["image"]["dim"])))
with columns[2]:
    st.write("**Channels #**")
    for channel in experiments[example_experiment]["image"]["channels"]["map"]:
        st.write("{}".format(channel))
with columns[3]:
    st.write("**Image Preview**")
    for channel in experiments[example_experiment]["image"]["channels"]["preview"]:
        st.write("{}: {}".format(
            channel, experiments[example_experiment]["image"]["channels"]["preview"][channel]))
with columns[4]:
    st.write("**Model architecture**")
    st.write("{}".format(
        str(experiments[example_experiment]["architecture"]["name"])))
with columns[5]:
    st.write("**Layers #**")
    for idx, filter in enumerate(experiments[example_experiment]["architecture"]["filters"]):
        st.write("{}".format(
            experiments[example_experiment]["architecture"]["filters"][idx]))
with columns[6]:
    st.write("**Latent Dimension**")
    st.write("{}".format(
        experiments[example_experiment]["architecture"]["latent_dim"]))
with columns[7]:
    st.write("**Epochs**")
    st.write("{}".format(
        experiments[example_experiment]["training"]["epochs"]))
with columns[8]:
    st.write("**Batch size**")
    st.write("{}".format(
        experiments[example_experiment]["training"]["batch_size"]))


