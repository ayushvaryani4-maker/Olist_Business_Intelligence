import streamlit as st

from src.data_loader import load_data
from src.category_analysis import get_category_metrics

st.title("Category Analysis")

data = load_data()

order_items = data["order_items"]
products = data["products"]
category_translation = data["category_translation"]

# Merge order items with product information
category_data = order_items.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left"
)

# Add English category names
category_data = category_data.merge(
    category_translation,
    on="product_category_name",
    how="left"
)

# Category Overview
st.subheader("Category Overview")

category_metrics = get_category_metrics(
    category_data
)

total_categories = category_metrics["total_categories"]
total_products = products["product_id"].nunique()
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Product Categories", total_categories)

with col2:
    st.metric("Total Products", total_products)

# Sales by Category
st.subheader("Sales by Category")

category_sales = category_metrics["category_revenue"]

st.bar_chart(category_sales.head(10))

# Top Categories Table
st.subheader("Top 10 Categories by Sales")

st.dataframe(
    category_sales.head(10).reset_index(name="Sales Value"),
    use_container_width=True
)
# Items Sold by Category

st.subheader("Items Sold by Category")

category_volume = (
    category_data
    .groupby("product_category_name_english")
    .size()
    .sort_values(ascending=False)
)

st.bar_chart(category_volume.head(10))

st.subheader("Top 10 Categories by Sales Volume")

st.dataframe(
    category_volume.head(10).reset_index(name="Items Sold"),
    use_container_width=True
)
# Average Product Price by Category

st.subheader("Average Product Price by Category")

average_category_price = (
    category_data
    .groupby("product_category_name_english")["price"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(
    average_category_price.head(10)
)

st.subheader("Top 10 Categories by Average Price")

st.dataframe(
    average_category_price.head(10)
    .reset_index(name="Average Price"),
    use_container_width=True
)