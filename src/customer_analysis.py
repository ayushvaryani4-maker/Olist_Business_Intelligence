import pandas as pd


def get_customer_metrics(customers, orders):
    """
    Calculate key customer metrics.

    Parameters:
        customers (pd.DataFrame): Customer dataset.
        orders (pd.DataFrame): Orders dataset.

    Returns:
        dict: Customer-related metrics.
    """

    total_unique_customers = customers["customer_unique_id"].nunique()

    total_orders = orders["order_id"].nunique()

    average_orders_per_customer = (
        total_orders / total_unique_customers
        if total_unique_customers > 0
        else 0
    )

    return {
        "total_unique_customers": total_unique_customers,
        "total_orders": total_orders,
        "average_orders_per_customer": average_orders_per_customer,
    }