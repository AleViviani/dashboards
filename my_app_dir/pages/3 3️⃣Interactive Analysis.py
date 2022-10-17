import streamlit as st
import pandas as pd
import numpy as np
import json
import os
import pacmap
import umap
from sklearn.decomposition import PCA
from bokeh.plotting import figure, output_file
from bokeh.io import curdoc
from bokeh.palettes import Category20, Category10
from bokeh.models import HoverTool, ColumnDataSource

from Sidebar import sidebar1, sidebar2

st.session_state.update(st.session_state)



st.set_page_config(layout="wide")

@st.cache(hash_funcs={'_json.Scanner': hash})
def load_data(data_path):
    # print(data_path)
    with open(data_path, "r") as file:
        data = json.load(file)
        # print(data[0])
    return data


st.header('Interactive Analysis')

st.write('Compute the previuos selected analysis operations on the dataset. If needed, go back and change them')

compute_button = st.button("Compute", help="Compute all the pipeline and visualize")

st.session_state['TRAIN_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['EMBEDDINGS_FILE'])
st.session_state['LABELS_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['LABELS_FILE'])
st.session_state['IMAGE_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['IMAGES_FOLDER'])
st.session_state['GEN_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['GENERATED_FOLDER'])

st.session_state['train_data'] = np.array(load_data(st.session_state['TRAIN_PATH']))
st.session_state['labels_data'] = load_data(st.session_state['LABELS_PATH'])

st.session_state['images'] = (st.session_state['labels_data'])['columns']         # Giusto scritto cosi??? Deriva da labels_data['columns']
st.session_state['labels'] = np.array((st.session_state['labels_data'])['data'])
st.session_state['labels'] = st.session_state['labels'].flatten()

st.session_state['df_image_paths'] = pd.DataFrame(
    {
        'image_path': map(
            lambda image: os.path.join(
                st.session_state['example_experiment'], st.session_state['IMAGES_FOLDER'], image),
            st.session_state['images']
        )
    })
print(st.session_state['df_image_paths'].head())

st.session_state['df_images_filename'] = pd.DataFrame({'image': st.session_state['images']})
st.session_state['df_images_filename'] = st.session_state['df_images_filename'].join(st.session_state['df_image_paths'])
print(st.session_state['df_images_filename'].head())


st.session_state['df_gen_paths'] = pd.DataFrame(
    {
        'gen_path': map(
            lambda image: os.path.join(
                st.session_state['example_experiment'], st.session_state['GENERATED_FOLDER'], image),
            st.session_state['images']
        )
    })
print(st.session_state['df_gen_paths'].head())


st.session_state['viz_data'] = st.session_state['train_data']
st.session_state['clus_data'] = st.session_state['train_data']


with st.sidebar:
    sidebar1()
    sidebar2()


if compute_button:
    # Visualization
    if st.session_state['vis_pre_reduction_check']:
        if st.session_state['vis_pre_reduction_method'] == "UMAP":
            st.session_state['reducer'] = umap.UMAP(n_neighbors = st.session_state['vis_pre_reduction_n_neighbors'],
                                min_dist=0, n_components = st.session_state['vis_pre_reduction_components'])
            st.session_state['viz_data'] = st.session_state['reducer'].fit_transform(st.session_state['viz_data'])
        elif st.session_state['vis_pre_reduction_method'] == "PCA":
            st.session_state['reducer'] = PCA(n_components=st.session_state['vis_pre_reduction_components'])
            st.session_state['viz_data'] = st.session_state['reducer'].fit_transform(st.session_state['viz_data'])
        

    if st.session_state['vis_reduction_method'] == "UMAP":
        st.session_state['reducer'] = umap.UMAP(n_neighbors=st.session_state['vis_reduction_UMAP_n_neighbors'],
                            min_dist=st.session_state['vis_reduction_UMAP_min_distance'], n_components=st.session_state['vis_reduction_components'])
    elif st.session_state['vis_reduction_method'] == "PACMAP":
        st.session_state['reducer'] = pacmap.PaCMAP(n_components=st.session_state['vis_reduction_components'], n_neighbors=st.session_state['vis_reduction_PACMAP_n_neighbors'],
                                MN_ratio=st.session_state['vis_reduction_PACMAP_MN_ratio'], FP_ratio=st.session_state['vis_reduction_PACMAP_FP_ratio'])
    elif st.session_state['vis_reduction_method'] == 'PCA':
        st.session_state['reducer'] = PCA(n_components=2)
    embedding = st.session_state['reducer'].fit_transform(st.session_state['viz_data'])

    st.session_state['df_embedding'] = pd.DataFrame(embedding)

    if st.session_state['vis_reduction_components'] == 2:
        st.session_state['df_embedding'] = st.session_state['df_embedding'].rename(columns={0: "x", 1: "y"})
    if st.session_state['vis_reduction_components'] == 3:
        st.session_state['df_embedding'] = st.session_state['df_embedding'].rename(columns={0: "x", 1: "y", 2: "z"})

    # Clustering
    if st.session_state['clus_pre_reduction_check']:

        if st.session_state['clus_pre_reduction_method'] == "UMAP":
            st.session_state['reducer'] = umap.UMAP(n_neighbors=st.session_state['clus_pre_reduction_n_neighbors'],
                                min_dist=0, n_components=st.session_state['clus_pre_reduction_components'])
            st.session_state['clus_data'] = st.session_state['reducer'].fit_transform(st.session_state['clus_data'])
        elif st.session_state['clus_pre_reduction_method'] == 'PCA':
            st.session_state['reducer'] = PCA(n_components=st.session_state['clus_pre_reduction_components'])
            st.session_state['clus_data'] = st.session_state['reducer'].fit_transform(st.session_state['clus_data'])


    st.session_state['clusters'] = st.session_state['clusterer'].fit_predict(st.session_state['clus_data'])
    df_clusters = pd.DataFrame(st.session_state['clusters'])
    df_clusters = df_clusters.rename(columns={0: "clusters"})

    st.session_state['df_embedding'] = st.session_state['df_embedding'].join(st.session_state['df_images_filename'])
    st.session_state['df_embedding'] = st.session_state['df_embedding'].join(df_clusters)
    st.session_state['df_embedding'] = st.session_state['df_embedding'].join(st.session_state['df_gen_paths'])

    csv = st.session_state['df_embedding'].drop(['image_path', 'gen_path'], axis=1)
    csv = csv.to_csv().encode('utf-8')
    st.download_button(label="Download clusters data as CSV",
                       data=csv, file_name='Data_clusters.csv', mime='text/csv')

    output_file('plot.html')
    curdoc().theme = 'dark_minimal'

    if np.unique(st.session_state['clusters']).size < 10:
        color = [Category10[10][i+1] for i in st.session_state['df_embedding']['clusters']]
    else:
        color = [Category20[20][i+1] for i in st.session_state['df_embedding']['clusters']]

    datasource = ColumnDataSource(data=dict(index=st.session_state['df_embedding'].index,
                                            x=st.session_state['df_embedding'].x,
                                            y=st.session_state['df_embedding'].y,
                                            image=st.session_state['df_embedding'].image,
                                            clusters=st.session_state['df_embedding'].clusters,
                                            image_path=st.session_state['df_embedding'].image_path,
                                            gen_path=st.session_state['df_embedding'].gen_path,
                                            color=color))

    plot_figure = figure(plot_width=800, plot_height=800,
                         tools=('pan, wheel_zoom, reset, save'))
    #color_mapping = CategoricalColorMapper(factors=[(x) for x in 'clusters'], palette=Category20[3])

    plot_figure.add_tools(HoverTool(tooltips="""
    <div style='text-align:center; border: 2px solid; border-radius: 2px'>
    <div style='display:flex'> 
        <div>
            <img src='@image_path' width="192" style='display: block; margin: 2px auto auto auto;'/>
        </div>
        <div>
            <img src='@gen_path' width="192" style='display: block; margin: 2px auto auto auto;'/>
        </div>
        </div>
        <div style='padding: 2px; font-size: 12px; color: #000000'>
            <span>Cluster:</span>
            <span>@clusters</span><br>
            <span>X:</span>
            <span>@x</span><br>
            <span>Y:</span>
            <span>@y</span><br>
            <span>Image:</span>
            <span>@image</span>
        </div>
    </div>
    """))

    plot_figure.circle('x', 'y', source=datasource, color='color', legend_field='clusters', fill_alpha=0.5, size=12)
    plot_figure.legend.title = "Clusters"
    plot_figure.legend.label_text_color = "black"
    plot_figure.legend.background_fill_color = 'white'
    plot_figure.legend.background_fill_alpha = 0.5


    # show(plot_figure)
    st.bokeh_chart(plot_figure, use_container_width=True)

    


