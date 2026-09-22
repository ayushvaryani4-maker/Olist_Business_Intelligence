import pandas as pd


def get_product_metrics(products, order_items):
    """
    Calculate key product metrics.

    Parameters:
        products (pd.DataFrame): Product dataset.
        order_items (pd.DataFrame): Order items dataset.

    Returns:
        dict: Product-related metrics.
    """

    total_products = products["product_id"].nunique()

    product_sales = (
        order_items.groupby("product_id")["price"]
        .sum()
        .sort_values(ascending=False)
    )

    top_product = (
        product_sales.index[0]
        if not product_sales.empty
        else None
    )

    top_product_revenue = (
        product_sales.iloc[0]
        if not product_sales.empty
        else 0
    )

    return {
        "total_products": total_products,
        "top_product": top_product,
        "top_product_revenue": top_product_revenue,
        "product_sales": product_sales,
    }