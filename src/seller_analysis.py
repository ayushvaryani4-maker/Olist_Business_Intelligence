import pandas as pd


def get_seller_metrics(sellers, order_items):
    """
    Calculate key seller metrics.

    Parameters:
        sellers (pd.DataFrame): Seller dataset.
        order_items (pd.DataFrame): Order items dataset.

    Returns:
        dict: Seller-related metrics.
    """

    total_sellers = sellers["seller_id"].nunique()

    seller_revenue = (
        order_items.groupby("seller_id")["price"]
        .sum()
        .sort_values(ascending=False)
    )

    top_seller = (
        seller_revenue.index[0]
        if not seller_revenue.empty
        else None
    )

    top_seller_revenue = (
        seller_revenue.iloc[0]
        if not seller_revenue.empty
        else 0
    )

    return {
        "total_sellers": total_sellers,
        "top_seller": top_seller,
        "top_seller_revenue": top_seller_revenue,
        "seller_revenue": seller_revenue,
    }