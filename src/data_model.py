import pandas as pd


def create_data_model(data):
    """
    Create a combined analytical dataset from the Olist datasets.

    Parameters:
        data (dict): Dictionary containing the Olist dataframes.

    Returns:
        pd.DataFrame: Combined dataset for analysis.
    """

    orders = data["orders"].copy()
    order_items = data["order_items"].copy()
    products = data["products"].copy()
    customers = data["customers"].copy()
    sellers = data["sellers"].copy()
    payments = data["payments"].copy()
    reviews = data["reviews"].copy()
    category_translation = data["category_translation"].copy()

    # Add product category names in English
    products = products.merge(
        category_translation,
        on="product_category_name",
        how="left"
    )

    # Combine orders with order items
    model = orders.merge(
        order_items,
        on="order_id",
        how="left"
    )

    # Add product information
    model = model.merge(
        products,
        on="product_id",
        how="left"
    )

    # Add seller information
    model = model.merge(
        sellers,
        on="seller_id",
        how="left"
    )

    # Add customer information
    model = model.merge(
        customers,
        on="customer_id",
        how="left"
    )

    return model