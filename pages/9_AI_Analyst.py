import streamlit as st
from src.ai_engine import ask_gemini
from src.data_loader import load_data

from src.customer_analysis import get_customer_metrics
from src.sales_analysis import get_sales_metrics
from src.category_analysis import get_category_metrics
from src.product_analysis import get_product_metrics
from src.seller_analysis import get_seller_metrics
from src.payment_analysis import get_payment_metrics
from src.review_analysis import get_review_metrics
from src.delivery_analysis import get_delivery_metrics

st.title("AI Business Analyst")

st.write(
    "Ask questions about the Olist business data "
    "and get AI-powered business insights."
)

# Load Olist data
data = load_data()

customers = data["customers"]
orders = data["orders"]
order_items = data["order_items"]
products = data["products"]
payments = data["payments"]
reviews = data["reviews"]
sellers = data["sellers"]
category_translation = data["category_translation"]


# --------------------------------------------------
# Create business summary
# --------------------------------------------------

customer_metrics = get_customer_metrics(customers, orders)
sales_metrics = get_sales_metrics(order_items, orders)
product_metrics = get_product_metrics(products, order_items)
seller_metrics = get_seller_metrics(sellers, order_items)
payment_metrics = get_payment_metrics(payments)
review_metrics = get_review_metrics(reviews)
delivery_metrics = get_delivery_metrics(orders)

total_customers = customer_metrics["total_unique_customers"]
total_orders = customer_metrics["total_orders"]

total_products = product_metrics["total_products"]
total_sellers = seller_metrics["total_sellers"]

total_sales = sales_metrics["total_revenue"]
total_freight = order_items["freight_value"].sum()

average_order_value = sales_metrics["average_order_value"]

average_review_score = review_metrics["average_review_score"]
payment_methods = (
    payment_metrics["payment_type_counts"]
    .to_dict()
)

order_status = (
    orders["order_status"]
    .value_counts()
    .to_dict()
)

# Category sales
category_data = order_items.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left"
)

category_data = category_data.merge(
    category_translation,
    on="product_category_name",
    how="left"
)

category_metrics = get_category_metrics(category_data)

top_categories = (
    category_metrics["category_revenue"]
    .head(10)
    .to_dict()
)



# Seller sales

top_sellers = (
    seller_metrics["seller_revenue"]
    .head(10)
    .to_dict()
)

# --------------------------------------------------
# Create context for Gemini
# --------------------------------------------------

business_context = f"""
You are an AI Business Analyst analyzing the Olist Brazilian
e-commerce marketplace dataset.

IMPORTANT:
- Use only the information provided in this business context.
- Do not invent numerical values.
- If the requested information is not available, clearly say so.
- The dataset does not contain actual business profit because
  product costs and operating costs are not available.
- Monetary values are in Brazilian Real (R$).

BUSINESS OVERVIEW

Total Customers: {total_customers}
Total Orders: {total_orders}
Total Products: {total_products}
Total Sellers: {total_sellers}

Total Product Sales Value: R$ {total_sales:,.2f}
Total Freight Value: R$ {total_freight:,.2f}
Average Order Value: R$ {average_order_value:,.2f}

Average Customer Review Score: {average_review_score:.2f} / 5

PAYMENT METHODS

{payment_methods}

ORDER STATUS

{order_status}

TOP 10 CATEGORIES BY SALES

{top_categories}

TOP 10 SELLERS BY SALES

{top_sellers}
"""


# --------------------------------------------------
# Gemini connection
# --------------------------------------------------




# --------------------------------------------------
# AI Analyst interface
# --------------------------------------------------

st.subheader("Ask the AI Analyst")

question = st.text_area(
    "Enter your business question:",
    placeholder=(
        "Example: Which product categories generate "
        "the highest sales and what does this tell us?"
    )
)


if st.button("Ask AI Analyst"):

    if question.strip() == "":
        st.warning("Please enter a question first.")

    else:

        prompt = f"""
{business_context}

USER QUESTION:

{question}

Provide a clear business-focused answer.

Where useful:
- Mention relevant numbers.
- Explain what the numbers mean.
- Identify possible business implications.
- Do not claim that correlation proves causation.
- Do not calculate profit unless the required cost information exists.
"""
        try:

            response = ask_gemini(prompt)

            st.subheader("AI Analyst Response")

            st.write(response)

        except Exception as e:

            st.error(
                "Something went wrong while contacting Gemini."
            )

            st.write(e)
       