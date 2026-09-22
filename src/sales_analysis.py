import pandas as pd


def get_sales_metrics(order_items, orders):
    """
    Calculate key sales metrics.

    Parameters:
        order_items (pd.DataFrame): Order items dataset.
        orders (pd.DataFrame): Orders dataset.

    Returns:
        dict: Sales-related metrics.
    """

    total_revenue = order_items["price"].sum()

    total_orders = orders["order_id"].nunique()

    average_order_value = (
        total_revenue / total_orders
        if total_orders > 0
        else 0
    )

    total_items_sold = len(order_items)

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "total_items_sold": total_items_sold,
    }