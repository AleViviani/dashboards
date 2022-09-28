# Streamlit libraries
import streamlit as st

# Data analysis libraries
from sklearn.cluster import KMeans, DBSCAN, AffinityPropagation, AgglomerativeClustering
import hdbscan

st.session_state.update(st.session_state)



st.set_page_config(layout="wide")

st.header('Analysis Settings')
st.write('In this page you can choose which methods and parameters will be used for the analysis\
        \nDone that, select the next page in the sidebar to visualize the result')

visualization_tab, clustering_tab, info_tab = st.tabs(["Visualization", "Clustering", "Info"])

with visualization_tab:

    st.subheader("Visualization pipeline")
    with st.container():
        vis_pre_reduction_check = st.checkbox(
            "Execute Pre-Reduction", value=False, key="vis_pre_reduction_check")

        if vis_pre_reduction_check:
        
            st.markdown('##### Pre-Reduction Options:')
            vis_pre_reduction_method = st.selectbox(
                'Pre-Reduction method',
                ('UMAP', 'PCA'),
                key="vis_pre_reduction_method"
            )

            vis_pre_reduction_components = st.slider(
                'Output dimensions', key="vis_pre_reduction_components", step=1, min_value=4, max_value=32, value=5)

            with st.container():
                if vis_pre_reduction_method == "UMAP":
                    vis_pre_reduction_n_neighbors = st.slider(
                        'Number of neighbors', key="vis_pre_reduction_n_neighbors", step=5, min_value=5, max_value=100, value=15)

                elif vis_pre_reduction_method == "PCA":
                    st.write('No more parameters for PCA')



    with st.container():
        st.markdown('##### Reduction Options:')

        vis_reduction_method = st.selectbox(
            'Reduction type',
            ('PCA', 'UMAP', 'PACMAP'),
            key="vis_reduction_method"
        )

        vis_reduction_components = st.number_input(
            'Output dimensions', key="vis_reduction_components", value=2, min_value=2, max_value=2)

        with st.container():
            if vis_reduction_method == "PCA":
                st.write('No more parameters for PCA')

            elif vis_reduction_method == "UMAP":
                vis_reduction_UMAP_n_neighbors = st.slider(
                    'Number of neighbors', key="vis_reduction_UMAP_n_neighbors", min_value=5, max_value=100, step=5, value=15)
                vis_reduction_UMAP_min_distance = st.slider(
                    'Minimum distance between points', key="vis_reduction_UMAP_min_distance", step=0.05, min_value=0.0, max_value=1.0, value=0.1)

            elif vis_reduction_method == "PACMAP":
                vis_reduction_PACMAP_n_neighbors = st.slider(
                    'Number of neighbors', key="vis_reduction_PACMAP_n_neighbors", min_value=5, max_value=100, step=5, value=15)
                vis_reduction_PACMAP_MN_ratio = st.slider(
                    'Attraction between near points', key="vis_reduction_PACMAP_MN_ratio", step=0.1, min_value=0.1, max_value=2.0, value=0.5)
                vis_reduction_PACMAP_FP_ratio = st.slider(
                    'Repulsion between distance points', key="vis_reduction_PACMAP_FP_ratio", step=0.5, min_value=0.5, max_value=5.0, value=2.0)


with clustering_tab:

    st.subheader("Clustering pipeline")
    with st.container():
        clus_pre_reduction_check = st.checkbox(
            "Execute Pre-Reduction", value=False, key="clus_pre_reduction_check")

        if clus_pre_reduction_check:
   
            st.markdown('##### Clustering Pre-Reduction Options:')
            clus_pre_reduction_method = st.selectbox(
                'Pre-Reduction method',
                ('UMAP', 'PCA'),
                key="clus_pre_reduction_method"
            )

            clus_pre_reduction_components = st.slider(
                'Output dimensions', key="clus_pre_reduction_components", step=1, value=5, min_value=4, max_value=32)

            with st.container():
                if clus_pre_reduction_method == "UMAP":
                    clus_pre_reduction_n_neighbors = st.slider(
                        'Number of neighbors', key="clus_pre_reduction_n_neighbors", step=5, min_value=5, max_value=100, value=15)

                elif clus_pre_reduction_method == "PCA":
                    st.write('No other parameters for PCA')
   

    with st.container():
        st.markdown('##### Clustering Options:')

        clus_method = st.selectbox(
            'Clustering type',
            ('kmeans', 'dbscan', 'hdbscan',
             'affinity propagation', 'agglomerative clustering'),
            key="clus_method"
        )

        with st.container():
            if clus_method == "kmeans":
                kmeans_n_clusters = st.slider('Number of cluster', key="kmeans_n_clusters", step=1, min_value=2, max_value=20, value=5)
                clusterer = KMeans(n_clusters=kmeans_n_clusters, random_state=0)

            elif clus_method == "dbscan":
                eps = st.slider('Eps', key="eps", step=0.05, min_value=0.0, max_value=1.0, value=0.1)
                dbscan_min_samples = st.slider('Min samples', key="dbscan_min_samples", step=1, min_value=2, max_value=50, value=5)
                clusterer = DBSCAN(
                    eps=eps, min_samples=dbscan_min_samples, metric='euclidean')   #???????????

            elif clus_method == "hdbscan":
                hdbscan_min_cluster_size = st.slider(
                    'Min cluster size', key="hdbscan_min_cluster_size", step=1, min_value=2, max_value=50, value=5)
                clusterer = hdbscan.HDBSCAN(min_cluster_size=hdbscan_min_cluster_size)

            elif clus_method == 'affinity propagation':
                clusterer = AffinityPropagation()
                st.write('No parameters for Affinity Propagation')

            elif clus_method == 'agglomerative clustering':
                agglom_clus_n_clusters = st.slider(
                    'Number of clusters', key='agglom_clus_n_clusters', step=1, min_value=2, max_value=20, value=5)
                clusterer = AgglomerativeClustering(n_clusters=agglom_clus_n_clusters)

            st.session_state['clusterer'] = clusterer


with info_tab:
    st.write('Select which operations execute on the dataset between the options available')