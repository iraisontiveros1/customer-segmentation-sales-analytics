import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA


def plot_elbow(results_df: pd.DataFrame):
    """
    Plot k vs inertia (Elbow method).
    """
    plt.figure()
    plt.plot(results_df["k"], results_df["inertia"], marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia (SSE)")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()


def plot_silhouette(results_df: pd.DataFrame):
    """
    Plot k vs silhouette score.
    """
    plt.figure()
    plt.plot(results_df["k"], results_df["silhouette"], marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Silhouette score")
    plt.title("Silhouette score by k")
    plt.grid(True)
    plt.show()


def plot_clusters_pca(X_scaled, labels, title: str = "Customer segments (PCA 2D)"):
    """
    PCA 2D projection of customers colored by cluster.
    """
    pca = PCA(n_components=2)
    components = pca.fit_transform(X_scaled)

    pca_df = pd.DataFrame(components, columns=["PC1", "PC2"])
    pca_df["cluster"] = labels

    plt.figure()
    for c in sorted(pca_df["cluster"].unique()):
        subset = pca_df[pca_df["cluster"] == c]
        plt.scatter(subset["PC1"], subset["PC2"], alpha=0.7, label=f"Cluster {c}")

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

