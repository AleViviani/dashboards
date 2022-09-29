# Streamlit libraries
import streamlit as st
import pandas as pd

st.session_state.update(st.session_state)

st.set_page_config(layout="wide")

## Widgets and variables

# Page 1

tableExample=pd.DataFrame({"Colonna 1":[1,2,3],"Colonna 2":[4,5,6]})
tableExample2=pd.DataFrame({"Colonna 1":[2,2,3],"Colonna 2":[2,2,6]})


with st.sidebar:
    st.table(tableExample)

tableExample.append(tableExample2, ignore_index=True)

with st.sidebar:
    st.table(tableExample)

"""
for key, value in dict:
    if key not in st.session_state:
        st.session_state[key] = value
"""




if 'data_dir_names' not in st.session_state:
    st.session_state['data_dir_names'] = []
#data_dir_names = st.session_state['data_dir_names']

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

if 'example_experiment' not in st.session_state:
    st.session_state['example_experiment'] = '2_channel_correct'
# example_experiment = st.session_state['example_experiment']
# example_experiment = st.selectbox('Choose data', tuple(experiments), key="example_experiment")

# st.session_state['EXPERIMENT_FOLDER'] = os.path.join(DATA_FOLDER, current_experiment)




# Page 2

if 'vis_pre_reduction_check' not in st.session_state:               # Per usare solo variabile globale session state
    st.session_state['vis_pre_reduction_check'] = False       
# vis_pre_reduction_check = st.session_state['vis_pre_reduction_check']     # Per usare anche variabile locale 
# vis_pre_reduction_check = st.checkbox("Execute Pre-Reduction", value=False, key="vis_pre_reduction_check")      # Definizione originale

if 'vis_pre_reduction_method' not in st.session_state:
    st.session_state['vis_pre_reduction_method'] = 'UMAP'
# vis_pre_reduction_method = st.session_state['vis_pre_reduction_method']
# vis_pre_reduction_method = st.selectbox('Pre-Reduction method', ('UMAP', 'PCA'), key="vis_pre_reduction_method")

if 'vis_pre_reduction_components' not in st.session_state:
    st.session_state['vis_pre_reduction_components'] = 5
# vis_pre_reduction_components = st.session_state['vis_pre_reduction_components']
# vis_pre_reduction_components = st.slider('Output dimensions', key="vis_pre_reduction_components", step=1, min_value=4, max_value=32, value=5)

if 'vis_pre_reduction_n_neighbors' not in st.session_state:
    st.session_state['vis_pre_reduction_n_neighbors'] = 15
# vis_pre_reduction_n_neighbors = st.session_state['vis_pre_reduction_n_neighbors']
# vis_pre_reduction_n_neighbors = st.slider('Number of neighbors', key="vis_pre_reduction_n_neighbors", step=5, min_value=5, max_value=100, value=15)

if 'vis_reduction_method' not in st.session_state:
    st.session_state['vis_reduction_method'] = 'PCA'
# vis_reduction_method = st.session_state['vis_reduction_method']
# vis_reduction_method = st.selectbox('vis_reduction_method', ('PCA', 'UMAP', 'PACMAP'), key="vis_reduction_method")

if 'vis_reduction_components' not in st.session_state:
    st.session_state['vis_reduction_components'] = 2
# vis_reduction_components = st.session_state['vis_reduction_components']
# vis_reduction_components = st.number_input('Output dimensions', key="vis_reduction_components", value=2, min_value=2, max_value=2)

if 'vis_reduction_UMAP_n_neighbors' not in st.session_state:
    st.session_state['vis_reduction_UMAP_n_neighbors'] = 15
# vis_reduction_UMAP_n_neighbors = st.session_state['vis_reduction_UMAP_n_neighbors']
# vis_reduction_UMAP_n_neighbors = st.slider('Number of neighbors', key="vis_reduction_UMAP_n_neighbors", min_value=5, max_value=100, step=5, value=15)

if 'vis_reduction_UMAP_min_distance' not in st.session_state:
    st.session_state['vis_reduction_UMAP_min_distance'] = 0.1
# vis_reduction_UMAP_min_distance = st.session_state['vis_reduction_UMAP_min_distance']
# vis_reduction_UMAP_min_distance = st.slider('Minimum distance between points', key="vis_reduction_UMAP_min_distance", step=0.05, min_value=0.0, max_value=1.0, value=0.1)

if 'vis_reduction_PACMAP_n_neighbors' not in st.session_state:
    st.session_state['vis_reduction_PACMAP_n_neighbors'] = 15
# vis_reduction_PACMAP_n_neighbors = st.session_state['vis_reduction_PACMAP_n_neighbors']
# vis_reduction_PACMAP_n_neighbors = st.slider('Number of neighbors', key="vis_reduction_PACMAP_n_neighbors", min_value=5, max_value=100, step=5, value=15)

if 'vis_reduction_PACMAP_MN_ratio' not in st.session_state:
    st.session_state['vis_reduction_PACMAP_MN_ratio'] = 0.5
# vis_reduction_PACMAP_MN_ratio = st.session_state['vis_reduction_PACMAP_MN_ratio']
# vis_reduction_PACMAP_MN_ratio = st.slider('Attraction between near points', key="vis_reduction_PACMAP_MN_ratio", step=0.1, min_value=0.1, max_value=2.0, value=0.5)
                
if 'vis_reduction_PACMAP_FP_ratio' not in st.session_state:
    st.session_state['vis_reduction_PACMAP_FP_ratio'] = 2.0
# vis_reduction_PACMAP_FP_ratio = st.session_state['vis_reduction_PACMAP_FP_ratio']
# vis_reduction_PACMAP_FP_ratio = st.slider('Repulsion between distance points', key="vis_reduction_PACMAP_FP_ratio", step=0.5, min_value=0.5, max_value=5.0, value=2.0)

if 'clus_pre_reduction_check' not in st.session_state:
    st.session_state['clus_pre_reduction_check'] = False
# clus_pre_reduction_check = st.session_state['clus_pre_reduction_check']
# clus_pre_reduction_check = st.checkbox("Execute Pre-Reduction", value=False, key="clus_pre_reduction_check")

if 'clus_pre_reduction_method' not in st.session_state:
    st.session_state['clus_pre_reduction_method'] = 'UMAP'
# clus_pre_reduction_method = st.session_state['clus_pre_reduction_method']
# clus_pre_reduction_method = st.selectbox('Pre-Reduction method', ('UMAP', 'PCA'), key="clus_pre_reduction_method")

if 'clus_pre_reduction_components' not in st.session_state:
    st.session_state['clus_pre_reduction_components'] = 5
# clus_pre_reduction_components = st.session_state['clus_pre_reduction_components']
# clus_pre_reduction_components = st.slider('Output dimensions', key="clus_pre_reduction_components", step=1, value=5, min_value=4, max_value=32)

if 'clus_pre_reduction_n_neighbors' not in st.session_state:
    st.session_state['clus_pre_reduction_n_neighbors'] = 15
# clus_pre_reduction_n_neighbors = st.session_state['clus_pre_reduction_n_neighbors']
# clus_pre_reduction_n_neighbors = st.slider('Number of neighbors', key="clus_pre_reduction_n_neighbors", step=5, min_value=5, max_value=100, value=15)

if 'clus_method' not in st.session_state:
    st.session_state['clus_method'] = 'kmeans'
# clus_method = st.session_state['clus_method']
# clus_method = st.selectbox('Clustering type', ('kmeans', 'dbscan', 'hdbscan','affinity propagation', 'agglomerative clustering'), key="clus_method")

if 'kmeans_n_clusters' not in st.session_state:
    st.session_state['kmeans_n_clusters'] = 5
# kmeans_n_clusters = st.session_state['kmeans_n_clusters']
# kmeans_n_clusters = st.slider('Number of cluster', key="kmeans_n_clusters", step=1, min_value=2, max_value=20, value=5)
                
if 'eps' not in st.session_state:
    st.session_state['eps'] = 0.1
# eps = st.session_state['eps']
# eps = st.slider('Eps', key="eps", step=0.05, min_value=0.0, max_value=1.0, value=0.1)

if 'dbscan_min_samples' not in st.session_state:
    st.session_state['dbscan_min_samples'] = 5
# dbscan_min_samples = st.session_state['dbscan_min_samples']
# dbscan_min_samples = st.slider('Min samples', key="dbscan_min_samples", step=1, min_value=2, max_value=50, value=5)
                
if 'hdbscan_min_cluster_size' not in st.session_state:
    st.session_state['hdbscan_min_cluster_size'] = 5
# hdbscan_min_cluster_size = st.session_state['hdbscan_min_cluster_size']
# hdbscan_min_cluster_size = st.slider('Min cluster size', key="hdbscan_min_cluster_size", step=1, min_value=2, max_value=50, value=5)
                
if 'agglom_clus_n_clusters' not in st.session_state:
    st.session_state['agglom_clus_n_clusters'] = 5
# agglom_clus_n_clusters = st.session_state['agglom_clus_n_clusters']
# agglom_clus_n_clusters = st.slider('Number of clusters', key='agglom_clus_n_clusters', step=1, min_value=2, max_value=20, value=5)
                
if 'clusterer' not in st.session_state:
    st.session_state['clusterer'] = []
# clusterer = st.session_state['clusterer']



# Page 3

if 'grid_comparison_method' not in st.session_state:
    st.session_state['grid_comparison_method'] = 'UMAP'
# grid_comparison_method = st.session_state['grid_comparison_method']
# grid_comparison_method = st.selectbox('Reduction type', ('UMAP', 'PCA'), key="grid_comparison_method")

if 'grid_neighbors_range' not in st.session_state:
    st.session_state['grid_neighbors_range'] = (25,50)                
# grid_neighbors_range = st.session_state['grid_neighbors_range']
# grid_neighbors_range = st.slider('Select a range of neighbors', 5, 100, (25, 50), key="grid_neighbors_range", step=5)

if 'grid_dist_range' not in st.session_state:
    st.session_state['grid_dist_range'] = (0.3,0.6)                
# grid_dist_range = st.session_state['grid_dist_range']
# grid_dist_range = st.slider('Select a range of distance', 0.0, 0.9, (0.3, 0.6), key="grid_dist_range", step=0.1)

# st.session_state['TRAIN_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['EMBEDDINGS_FILE'])
# st.session_state['LABELS_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['LABELS_FILE'])
# st.session_state['IMAGE_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['IMAGES_FOLDER'])
# st.session_state['GEN_PATH'] = os.path.join(st.session_state['EXPERIMENT_FOLDER'], st.session_state['GENERATED_FOLDER'])

# st.session_state['train_data'] = np.array(load_data(st.session_state['TRAIN_PATH']))
# st.session_state['labels_data'] = load_data(st.session_state['LABELS_PATH'])

# st.session_state['images'] = (st.session_state['labels_data'])['columns']         # Giusto scritto cosi??? Deriva da labels_data['columns']
# st.session_state['labels'] = np.array((st.session_state['labels_data'])['data'])
# st.session_state['labels'] = st.session_state['labels'].flatten()

# st.session_state['df_image_paths']
# st.session_state['df_images_filename']
# st.session_state['df_gen_paths']
# st.session_state['viz_data'] = st.session_state['train_data']
# st.session_state['clus_data'] = st.session_state['train_data']

# st.session_state['reducer']
# st.session_state['df_embedding']
# st.session_state['clusters']


#################################################################################################################
#################################################################################################################

st.title("Home")
st.write("""This web app is related to NEANIAS, an ambitious project to face the challenges proposed by the 
        European Open Science Cloud (EOSC) program.
        \nNEANIAS promotes Open Science practices and plays an active role in the delivery of innovative services 
        in three major sectors: Underwater research, Atmospheric research and Space research, each engaging many 
        academic and business groups, numerous researchers, professionals and governmental entities.
        """)
st.markdown("To know more about it check: [Neanias Homepage](https://www.neanias.eu/)")
st.markdown("#### This Web App: ")
st.write("""Here you can analyze a dataset of images through multiple tools and unsupervised procedures.
        
        """)




