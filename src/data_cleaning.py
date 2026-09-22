import pandas as pd


def clean_data(df):
    """
    Clean the Olist dataset.

    Parameters:
        df (pd.DataFrame): Raw dataframe

    Returns:
        pd.DataFrame: Cleaned dataframe
    """

    # Make a copy so the original dataframe is not modified
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert column names to lowercase
    df.columns = df.columns.str.lower().str.strip()

    # Remove leading/trailing spaces from string columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Convert common date columns to datetime
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "shipping_limit_date",
        "review_creation_date",
        "review_answer_timestamp"
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    # Convert numeric columns where applicable
    numeric_columns = [
        "price",
        "freight_value",
        "payment_value",
        "payment_installments",
        "review_score"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # Reset index after cleaning
    df = df.reset_index(drop=True)

    return df