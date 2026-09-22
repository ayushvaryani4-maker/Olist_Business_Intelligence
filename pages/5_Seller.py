import streamlit as st

from src.data_loader import load_data
from src.seller_analysis import get_seller_metrics

st.title("Seller Analysis")

data = load_data()

sellers = data["sellers"]
order_items = data["order_items"]

# Seller Overview
st.subheader("Seller Overview")

seller_metrics = get_seller_metrics(sellers, order_items)

total_sellers = seller_metrics["total_sellers"]
total_seller_items = len(order_items)
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sellers", total_sellers)

with col2:
    st.metric("Total Items Sold", total_seller_items)

# Seller Sales
st.subheader("Top Sellers by Sales")

seller_sales = seller_metrics["seller_revenue"]

st.bar_chart(seller_sales.head(10))

st.subheader("Top 10 Sellers by Sales")

st.dataframe(
    seller_sales.head(10)
    .reset_index(name="Sales Value"),
    use_container_width=True
)

# Seller Volume
st.subheader("Top Sellers by Sales Volume")

seller_volume = (
    order_items["seller_id"]
    .value_counts()
)

st.bar_chart(seller_volume.head(10))

st.subheader("Top 10 Sellers by Items Sold")

st.dataframe(
    seller_volume.head(10)
    .reset_index(name="Items Sold"),
    use_container_width=True
)
# Seller Average Sales Value

st.subheader("Seller Average Sales Value")

seller_average_value = (
    order_items
    .groupby("seller_id")["price"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(
    seller_average_value.head(10)
)

st.subheader("Top 10 Sellers by Average Product Value")

st.dataframe(
    seller_average_value.head(10)
    .reset_index(name="Average Product Value"),
    use_container_width=True
)