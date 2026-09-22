import pandas as pd


def get_payment_metrics(payments):
    """
    Calculate key payment metrics.

    Parameters:
        payments (pd.DataFrame): Payment dataset.

    Returns:
        dict: Payment-related metrics.
    """

    total_payment_value = payments["payment_value"].sum()

    average_payment_value = payments["payment_value"].mean()

    payment_type_counts = payments["payment_type"].value_counts()

    top_payment_type = (
        payment_type_counts.index[0]
        if not payment_type_counts.empty
        else None
    )

    top_payment_type_count = (
        payment_type_counts.iloc[0]
        if not payment_type_counts.empty
        else 0
    )

    average_installments = payments["payment_installments"].mean()

    return {
        "total_payment_value": total_payment_value,
        "average_payment_value": average_payment_value,
        "top_payment_type": top_payment_type,
        "top_payment_type_count": top_payment_type_count,
        "average_installments": average_installments,
        "payment_type_counts": payment_type_counts,
    }