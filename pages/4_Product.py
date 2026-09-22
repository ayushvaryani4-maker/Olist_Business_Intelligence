import streamlit as st

from src.data_loader import load_data
from src.product_analysis import get_product_metrics

st.title("Product Analysis")

data = load_data()

products = data["products"]
order_items = data["order_items"]

# Product Overview
st.subheader("Product Overview")

product_metrics = get_product_metrics(products, order_items)

total_products = product_metrics["total_products"]
total_order_items = len(order_items)
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Products", total_products)

with col2:
    st.metric("Total Items Sold", total_order_items)

# Product Sales
st.subheader("Top Products by Sales")

product_sales = product_metrics["product_sales"]
st.dataframe(
    product_sales.head(10).reset_index(name="Sales Value"),
    use_container_width=True
)

# Product Sales Chart
st.subheader("Top 10 Products by Sales")

st.bar_chart(product_sales.head(10))

# Product Volume
st.subheader("Top Products by Sales Volume")

product_volume = (
    order_items["product_id"]
    .value_counts()
)

st.dataframe(
    product_volume.head(10)
    .reset_index(name="Items Sold"),
    use_container_width=True
)

st.bar_chart(product_volume.head(10))
# Product Price Analysis

st.subheader("Product Price Analysis")

average_product_price = order_items["price"].mean()
maximum_product_price = order_items["price"].max()
minimum_product_price = order_items["price"].min()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Product Price",
        f"R$ {average_product_price:,.2f}"
    )

with col2:
    st.metric(
        "Highest Product Price",
        f"R$ {maximum_product_price:,.2f}"
    )

with col3:
    st.metric(
        "Lowest Product Price",
        f"R$ {minimum_product_price:,.2f}"
    )