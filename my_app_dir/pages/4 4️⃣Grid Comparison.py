import streamlit as st
import umap
import math
import matplotlib.pyplot as plt

from Sidebar import sidebar1, sidebar2

st.session_state.update(st.session_state)

st.set_page_config(layout="wide")

st.header('Grid Comparison')
st.write('Visualize on a grid how different settings choices impact on the clusterization')
grid_comparison_method = st.selectbox('Reduction type', options=("UMAP",), key="grid_comparison_method")

grid_neighbors_range = st.slider('Select a range of neighbors', 5, 100, (25, 50), key="grid_neighbors_range", step=5)
grid_dist_range = st.slider('Select a range of distance', 0.0, 0.9, (0.3, 0.6), key="grid_dist_range", step=0.1)

with st.sidebar:
    sidebar1()
    sidebar2()

compute_button = st.button("Compute", help="Compute grid and visualize")

if compute_button:

    st.write('neighbors: ', min(st.session_state['grid_neighbors_range']), '  ', max(
        st.session_state['grid_neighbors_range']),  'distances: ', min(st.session_state['grid_dist_range']), '  ', max(st.session_state['grid_dist_range']))
    grid_neighbor_range = [min(st.session_state['grid_neighbors_range']), math.floor(
        (min(st.session_state['grid_neighbors_range'])+max(st.session_state['grid_neighbors_range']))/2), max(st.session_state['grid_neighbors_range'])]
    grid_dist_range = [min(st.session_state['grid_dist_range']), round(
        (min(st.session_state['grid_dist_range'])+max(st.session_state['grid_dist_range']))/2, 2), max(st.session_state['grid_dist_range'])]
    fig, axs = plt.subplots(nrows=len(grid_neighbor_range), ncols=len(
        grid_dist_range), figsize=(10, 10), constrained_layout=True)
    fig.text(0.5, -0.03, 'Minimum Distance', ha='center', fontsize='medium')
    fig.text(-0.03, 0.5, 'Number of Neighbors', va='center',
                rotation='vertical', fontsize='medium')
    fig.text(0.5, 1.03, 'Minimum Distance', ha='center', fontsize='medium')
    fig.text(1.03, 0.5, 'Number of Neighbors', va='center',
                rotation='vertical', fontsize='medium')
    for nrow, n in enumerate(grid_neighbor_range):
        for ncol, d in enumerate(grid_dist_range):
            embedding = umap.UMAP(
                n_components=2, n_neighbors=n, min_dist=d, random_state=42)
            st.session_state['reducer'] = embedding.fit_transform(st.session_state['viz_data'])
            axs[nrow, ncol].scatter(
                st.session_state['reducer'][:, 0], st.session_state['reducer'][:, 1], c=st.session_state['df_embedding']['clusters'], s=10, cmap='Spectral')
            axs[nrow, ncol].set_yticklabels([])
            axs[nrow, ncol].set_xticklabels([])
            axs[nrow, ncol].set_title('n_neighbors={} '.format(n) + 'min_dist={}'.format(d), fontsize=8)
    st.pyplot(fig)
