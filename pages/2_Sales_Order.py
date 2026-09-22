import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.sales_analysis import get_sales_metrics

st.title("Sales & Order Analysis")

data = load_data()

orders = data["orders"]
order_items = data["order_items"]

# Basic order metrics
st.subheader("Order Overview")

total_orders = orders["order_id"].nunique()
total_items = len(order_items)

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Orders", total_orders)

with col2:
    st.metric("Total Order Items", total_items)

# Order status analysis
st.subheader("Orders by Status")

order_status = orders["order_status"].value_counts()

st.bar_chart(order_status)

st.subheader("Order Status Details")

st.dataframe(
    order_status.reset_index(name="Number of Orders"),
    use_container_width=True
)
# Sales Value and Freight Analysis

st.subheader("Sales Value Analysis")

sales_metrics = get_sales_metrics(order_items, orders)

total_sales = sales_metrics["total_revenue"]
total_freight = order_items["freight_value"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales Value", f"R$ {total_sales:,.2f}")

with col2:
    st.metric("Total Freight Value", f"R$ {total_freight:,.2f}")

st.subheader("Sales vs Freight")

sales_freight = {
    "Sales Value": total_sales,
    "Freight Value": total_freight
}

st.bar_chart(sales_freight)
# Monthly Sales Trend

st.subheader("Monthly Sales Trend")

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

monthly_orders = (
    orders.assign(
        month=orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
    )
    .groupby("month")["order_id"]
    .nunique()
)

st.line_chart(monthly_orders)
# Average Order Value

st.subheader("Average Order Value")

average_order_value = sales_metrics["average_order_value"]

st.metric(
    "Average Order Value",
    f"R$ {average_order_value:,.2f}"
)