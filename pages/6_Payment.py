import streamlit as st

from src.data_loader import load_data
from src.payment_analysis import get_payment_metrics

st.title("Payment Analysis")

data = load_data()

payments = data["payments"]

# Payment Overview
st.subheader("Payment Overview")

payment_metrics = get_payment_metrics(payments)

total_payment_records = len(payments)
total_payment_value = payment_metrics["total_payment_value"]
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Payment Records",
        total_payment_records
    )

with col2:
    st.metric(
        "Total Payment Value",
        f"R$ {total_payment_value:,.2f}"
    )

# Payment Methods
st.subheader("Payment Methods")

payment_methods = payment_metrics["payment_type_counts"]
st.bar_chart(payment_methods)

st.dataframe(
    payment_methods
    .reset_index(name="Number of Payments"),
    use_container_width=True
)

# Payment Value by Method
st.subheader("Payment Value by Payment Method")

payment_value_by_method = (
    payments
    .groupby("payment_type")["payment_value"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(payment_value_by_method)

st.dataframe(
    payment_value_by_method
    .reset_index(name="Payment Value"),
    use_container_width=True
)