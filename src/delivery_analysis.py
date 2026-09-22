import pandas as pd


def get_delivery_metrics(orders):
    """
    Calculate key delivery and fulfilment metrics.

    Parameters:
        orders (pd.DataFrame): Orders dataset.

    Returns:
        dict: Delivery-related metrics.
    """

    orders = orders.copy()

    # Convert date columns to datetime
    orders["order_delivered_customer_date"] = pd.to_datetime(
        orders["order_delivered_customer_date"],
        errors="coerce"
    )

    orders["order_estimated_delivery_date"] = pd.to_datetime(
        orders["order_estimated_delivery_date"],
        errors="coerce"
    )

    # Calculate delivery duration in days
    orders["delivery_duration_days"] = (
        orders["order_delivered_customer_date"]
        - pd.to_datetime(orders["order_purchase_timestamp"], errors="coerce")
    ).dt.total_seconds() / (24 * 60 * 60)

    # Calculate delivery delay in days
    orders["delivery_delay_days"] = (
        orders["order_delivered_customer_date"]
        - orders["order_estimated_delivery_date"]
    ).dt.total_seconds() / (24 * 60 * 60)

    average_delivery_time = orders["delivery_duration_days"].mean()

    average_delivery_delay = orders["delivery_delay_days"].mean()

    on_time_deliveries = (
        (orders["delivery_delay_days"] <= 0).sum()
    )

    delayed_deliveries = (
        (orders["delivery_delay_days"] > 0).sum()
    )

    return {
        "average_delivery_time": average_delivery_time,
        "average_delivery_delay": average_delivery_delay,
        "on_time_deliveries": on_time_deliveries,
        "delayed_deliveries": delayed_deliveries,
    }