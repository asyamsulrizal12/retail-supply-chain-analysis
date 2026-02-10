import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def prepare_rfm(data, customer_id_col, recency_col, frequency_col, monetary_col):
    """
    Prepare RFM dataframe for clustering.
    """
    rfm = data[[customer_id_col, recency_col, frequency_col, monetary_col]].copy()
    rfm.rename(columns={
        customer_id_col: "CustomerID",
        recency_col: "Recency",
        frequency_col: "Frequency",
        monetary_col: "Monetary"
    }, inplace=True)
    return rfm

def scale_rfm(rfm):
    """
    Scale RFM values for clustering.
    """
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[["Recency", "Frequency", "Monetary"]])
    return rfm_scaled

def run_kmeans(rfm_scaled, n_clusters=3, random_state=42):
    """
    Run KMeans clustering with chosen number of clusters.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(rfm_scaled)
    return clusters, kmeans

def profile_clusters(rfm, clusters):
    """
    Generate cluster profile summary.
    """
    rfm["Cluster"] = clusters
    cluster_profile = rfm.groupby("Cluster").agg({
        "Recency": "mean",
        "Frequency": "mean",
        "Monetary": "mean",
        "CustomerID": "count"
    }).reset_index()
    return cluster_profile