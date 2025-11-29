from typing import Iterable

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def prepare_features(rfm_df: pd.DataFrame, feature_cols: list[str]):
    """
    Select and scale features for clustering.
    """
    X = rfm_df[feature_cols].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


def evaluate_k_range(X_scaled: np.ndarray, k_values: Iterable[int]) -> pd.DataFrame:
    """
    Evaluate different k values using inertia and silhouette score.
    """
    results = []

    for k in k_values:
        model = KMeans(n_clusters=k, random_state=42, n_init="auto")
        labels = model.fit_predict(X_scaled)

        inertia = model.inertia_
        sil = silhouette_score(X_scaled, labels) if k > 1 else np.nan

        results.append({"k": k, "inertia": inertia, "silhouette": sil})

    return pd.DataFrame(results)


def run_kmeans(X_scaled: np.ndarray, n_clusters: int) -> KMeans:
    """
    Fit final K-Means model.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init="auto")
    model.fit(X_scaled)
    return model
