
import streamlit as st

from src.data_loader import load_data
from src.customer_analysis import get_customer_metrics

st.title("Customer Analysis")

data = load_data()

customers = data["customers"]
orders = data["orders"]

# Basic customer metrics
st.subheader("Customer Dataset")

customer_metrics = get_customer_metrics(customers, orders)

total_customers = customer_metrics["total_unique_customers"]
total_orders = customer_metrics["total_orders"]
st.write("Total Customers:", total_customers)
st.write("Total Orders:", total_orders)

# Customer order frequency
customer_orders = orders.merge(
    customers[["customer_id", "customer_unique_id"]],
    on="customer_id",
    how="left"
)

orders_per_customer = (
    customer_orders.groupby("customer_unique_id")["order_id"]
    .nunique()
)

one_time_customers = (orders_per_customer == 1).sum()
repeat_customers = (orders_per_customer > 1).sum()

st.subheader("Customer Purchase Behaviour")

col1, col2 = st.columns(2)

with col1:
    st.metric("One-Time Customers", one_time_customers)

with col2:
    st.metric("Repeat Customers", repeat_customers)

# Customer order frequency table
st.subheader("Orders per Customer")

frequency_table = (
    orders_per_customer
    .value_counts()
    .sort_index()
    .rename_axis("Number of Orders")
    .reset_index(name="Number of Customers")
)

st.dataframe(frequency_table, use_container_width=True)
st.subheader("Customer Order Frequency")

st.bar_chart(
    frequency_table.set_index("Number of Orders")["Number of Customers"]
)
st.subheader("Customers by State")

customers_by_state = (
    customers.groupby("customer_state")["customer_unique_id"]
    .nunique()
    .sort_values(ascending=False)
)

st.bar_chart(customers_by_state.head(10))

st.subheader("Top 10 Customer States")

st.dataframe(
    customers_by_state.head(10).reset_index(name="Number of Customers"),
    use_container_width=True
)
