import pandas as pd


def get_category_metrics(model):
    """
    Calculate key product category metrics.

    Parameters:
        model (pd.DataFrame): Combined Olist analytical dataset.

    Returns:
        dict: Category-related metrics.
    """

    total_categories = model["product_category_name_english"].nunique()

    category_revenue = (
        model.groupby("product_category_name_english")["price"]
        .sum()
        .sort_values(ascending=False)
    )

    top_category = (
        category_revenue.index[0]
        if not category_revenue.empty
        else None
    )

    top_category_revenue = (
        category_revenue.iloc[0]
        if not category_revenue.empty
        else 0
    )

    return {
        "total_categories": total_categories,
        "top_category": top_category,
        "top_category_revenue": top_category_revenue,
        "category_revenue": category_revenue,
    }