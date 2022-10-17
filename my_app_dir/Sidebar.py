import streamlit as st

def sidebar1():
    st.markdown('## **Settings Recap:** ')
    st.write('**Data Folder:** ', st.session_state['example_experiment'])

def sidebar2():
    st.markdown("<h4 style='text-align: center; color: grey;'>Visualization</h4>", unsafe_allow_html=True)
    if st.session_state['vis_pre_reduction_check']:
        st.write('**Pre-Reduction:** ', st.session_state['vis_pre_reduction_method'])
        st.write('**Output dimensions:** ', st.session_state['vis_pre_reduction_components'])
        if st.session_state['vis_pre_reduction_method'] == "UMAP":
            st.write('**Number of neighbors:** ', st.session_state['vis_pre_reduction_n_neighbors'])
    st.write('**Reduction:** ', st.session_state['vis_reduction_method'])
    st.write('**Output dimensions:** ', st.session_state['vis_reduction_components'])
    if st.session_state['vis_reduction_method'] == "UMAP":
        st.write('**Number of neighbors:** ', st.session_state['vis_reduction_UMAP_n_neighbors'])
        st.write('**Minimum Distance:** ', st.session_state['vis_reduction_UMAP_min_distance'])
    if st.session_state['vis_reduction_method'] == "PACMAP":
        st.write('**Number of neighbors:** ', st.session_state['vis_reduction_PACMAP_n_neighbors'])
        st.write('**Attraction:** ', st.session_state['vis_reduction_PACMAP_MN_ratio'])
        st.write('**Repulsion:** ', st.session_state['vis_reduction_PACMAP_FP_ratio'])

    st.markdown("<h4 style='text-align: center; color: grey;'>Clustering</h4>", unsafe_allow_html=True)
    if st.session_state['clus_pre_reduction_check']:
        st.write('**Pre-Reduction:** ', st.session_state['clus_pre_reduction_method'])
        st.write('**Output dimensions:** ', st.session_state['clus_pre_reduction_components'])
        if st.session_state['clus_pre_reduction_method'] == "UMAP":
            st.write('**Number of neighbors:** ', st.session_state['clus_pre_reduction_n_neighbors'])
    st.write('**Clustering:** ', st.session_state['clus_method'])
    if st.session_state['clus_method'] == "kmeans":
        st.write('**Number of clusters:** ', st.session_state['kmeans_n_clusters'])
    if st.session_state['clus_method'] == "dbscan":
        st.write('**Eps:** ', st.session_state['eps'])
        st.write('**Min samples:** ', st.session_state['dbscan_min_samples'])
    if st.session_state['clus_method'] == "hdbscan":
        st.write('**Min cluster size:** ', st.session_state['hdbscan_min_cluster_size'])
    if st.session_state['clus_method'] == "agglomerative clustering":
        st.write('**Number of clusters:** ', st.session_state['agglom_clus_n_clusters'])
