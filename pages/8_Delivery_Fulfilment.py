
import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.delivery_analysis import get_delivery_metrics

st.title("Delivery & Fulfilment Analysis")

data = load_data()

# Make a copy so the original dataset remains unchanged
orders = data["orders"].copy()
delivery_metrics = get_delivery_metrics(orders)

# Convert date columns into datetime format
date_columns = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

# Keep only delivered orders
delivered_orders = orders[
    orders["order_status"] == "delivered"
].copy()

# Remove rows where required dates are missing
delivered_orders = delivered_orders.dropna(
    subset=[
        "order_purchase_timestamp",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
)

# Calculate actual delivery duration in days
delivered_orders["delivery_days"] = (
    delivered_orders["order_delivered_customer_date"]
    - delivered_orders["order_purchase_timestamp"]
).dt.total_seconds() / 86400

# Calculate delay compared with estimated delivery date
# Positive = late, zero = on time, negative = early
delivered_orders["delay_days"] = (
    delivered_orders["order_delivered_customer_date"]
    - delivered_orders["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

# Exclude impossible negative delivery durations
invalid_delivery_count = (
    delivered_orders["delivery_days"] < 0
).sum()

delivered_orders = delivered_orders[
    delivered_orders["delivery_days"] >= 0
].copy()

# Delivery Overview
st.subheader("Delivery Overview")

total_delivered = len(delivered_orders)

if total_delivered > 0:
    average_delivery_days = delivery_metrics["average_delivery_time"]

    on_time_orders = delivery_metrics["on_time_deliveries"]
    late_orders = delivery_metrics["delayed_deliveries"]
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Delivered Orders", total_delivered)

    with col2:
        st.metric(
            "Average Delivery Time",
            f"{average_delivery_days:.1f} days"
        )

    with col3:
        st.metric("Late Deliveries", int(late_orders))

    # On-time vs Late Delivery
    st.subheader("On-Time vs Late Deliveries")

    delivery_status = pd.Series({
        "On Time or Early": int(on_time_orders),
        "Late": int(late_orders)
    })

    st.bar_chart(delivery_status)

    st.dataframe(
        delivery_status.reset_index(
            name="Number of Orders"
        ),
        use_container_width=True
    )

    # Delivery Time Distribution
    st.subheader("Delivery Time Distribution")

    delivery_distribution = (
        delivered_orders["delivery_days"]
        .round()
        .value_counts()
        .sort_index()
    )

    st.bar_chart(delivery_distribution)

    # Average delay compared with estimated date
    st.subheader("Average Delivery Delay")

    average_delay = delivery_metrics["average_delivery_delay"]

    st.metric(
        "Average Delay vs Estimated Date",
        f"{average_delay:.1f} days"
    )

    st.caption(
        "A positive delay means late delivery; "
        "a negative delay means delivery before the estimated date."
    )

    # Data quality information
    st.subheader("Data Quality Check")

    st.write(
        "Orders excluded due to negative delivery duration:",
        int(invalid_delivery_count)
    )

    # Sample records for verification
    st.subheader("Sample Delivery Records")

    st.dataframe(
        delivered_orders[
            [
                "order_purchase_timestamp",
                "order_delivered_customer_date",
                "order_estimated_delivery_date",
                "delivery_days",
                "delay_days"
            ]
        ].head(10),
        use_container_width=True
    )

else:
    st.warning(
        "No valid delivered orders were found. "
        "Please check the dataset and date columns."
    )
    
st.subheader("Debug: Delivery Date Check")

st.write("Sample original order dates:")

st.dataframe(
    orders[
        [
            "order_status",
            "order_purchase_timestamp",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ].head(20),
    use_container_width=True
)

st.write("Sample calculated delivery durations:")

st.dataframe(
    delivered_orders[
        [
            "order_purchase_timestamp",
            "order_delivered_customer_date",
            "delivery_days"
        ]
    ].head(20),
    use_container_width=True
)

st.write(
    "Minimum delivery duration:",
    delivered_orders["delivery_days"].min()
)

st.write(
    "Maximum delivery duration:",
    delivered_orders["delivery_days"].max()
)

st.write(
    "Average delivery duration:",
    delivered_orders["delivery_days"].mean()
)