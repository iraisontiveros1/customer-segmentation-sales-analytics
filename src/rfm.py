import pandas as pd
from datetime import datetime


def calculate_rfm(
    df: pd.DataFrame,
    customer_id_col: str,
    date_col: str,
    amount_col: str,
    reference_date: datetime | None = None,
) -> pd.DataFrame:
    """
    Calculate RFM metrics from a transactional dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Transactional data (one row per purchase).
    customer_id_col : str
        Column name for customer ID.
    date_col : str
        Column name for transaction date.
    amount_col : str
        Column name for transaction amount (revenue).
    reference_date : datetime, optional
        Date to compute Recency from. If None, uses max(date_col).

    Returns
    -------
    rfm : pd.DataFrame
        Dataframe with columns: ['Recency', 'Frequency', 'Monetary'].
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    if reference_date is None:
        reference_date = df[date_col].max() + pd.Timedelta(days=1)

    rfm = df.groupby(customer_id_col).agg(
        Recency=(date_col, lambda x: (reference_date - x.max()).days),
        Frequency=(date_col, "count"),
        Monetary=(amount_col, "sum"),
    )

    return rfm.reset_index()


def add_rfm_scores(
    rfm_df: pd.DataFrame,
    recency_col: str = "Recency",
    frequency_col: str = "Frequency",
    monetary_col: str = "Monetary",
    q: int = 5,
) -> pd.DataFrame:
    """
    Add R, F, M scores (1–q) based on quantiles.

    Returns dataframe with extra columns:
    ['R_score', 'F_score', 'M_score', 'RFM_score'].
    """
    rfm = rfm_df.copy()

    # Recency: lower = better (reverse)
    rfm["R_score"] = pd.qcut(rfm[recency_col], q, labels=range(q, 0, -1))

    # Frequency & Monetary: higher = better
    rfm["F_score"] = pd.qcut(rfm[frequency_col].rank(method="first"), q, labels=range(1, q + 1))
    rfm["M_score"] = pd.qcut(rfm[monetary_col].rank(method="first"), q, labels=range(1, q + 1))

    rfm["R_score"] = rfm["R_score"].astype(int)
    rfm["F_score"] = rfm["F_score"].astype(int)
    rfm["M_score"] = rfm["M_score"].astype(int)

    rfm["RFM_score"] = rfm["R_score"] * 100 + rfm["F_score"] * 10 + rfm["M_score"]

    return rfm

