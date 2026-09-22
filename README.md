# Olist Business Intelligence & GenAI Dashboard

## Project Overview

The Olist Business Intelligence & GenAI Dashboard is a data analytics application built using Python, Pandas, Streamlit, and Google Gemini.

The project analyzes the Olist Brazilian e-commerce marketplace dataset and provides interactive business insights across customers, sales, products, categories, sellers, payments, reviews, and delivery performance.

The dashboard also includes an AI Business Analyst that allows users to ask natural-language questions about the business data and receive AI-powered insights based on the calculated dataset metrics.
## Project Objective

The main objective of this project is to transform raw e-commerce data into an interactive Business Intelligence dashboard that helps users understand business performance and identify meaningful patterns.

The project focuses on:

- Analyzing customer and order behaviour
- Measuring sales and revenue performance
- Identifying high-performing product categories and products
- Analyzing seller performance
- Understanding payment methods and customer reviews
- Evaluating delivery and fulfilment performance
- Providing AI-assisted business analysis using Google Gemini

## Key Features

### Business Intelligence Dashboard

The dashboard contains nine analytical sections:

1. **Customer Analysis** – Customer and order metrics
2. **Sales & Order Analysis** – Revenue, orders, average order value, and items sold
3. **Category Analysis** – Category-level sales performance
4. **Product Analysis** – Product-level sales performance
5. **Seller Analysis** – Seller-level revenue performance
6. **Payment Analysis** – Payment methods and payment behaviour
7. **Review Analysis** – Customer review scores and ratings
8. **Delivery & Fulfilment Analysis** – Delivery time, delays, and fulfilment performance
9. **AI Business Analyst** – Natural-language business questions answered using Google Gemini
## Technologies Used

- **Python** – Core programming language
- **Pandas** – Data loading, cleaning, transformation, and analysis
- **NumPy** – Numerical computing
- **Streamlit** – Interactive dashboard development
- **Google Gemini** – AI-powered business analysis
- **Git & GitHub** – Version control and project management
- **CSV** – Source data format

## Project Architecture

The project follows a modular structure where data loading, cleaning, business analysis, and AI functionality are separated into different components.

```text
Olist_Business_Intelligence/
│
├── data/
│   └── Olist dataset CSV files
│
├── pages/
│   ├── 1_Customer.py
│   ├── 2_Sales_Order.py
│   ├── 3_Category.py
│   ├── 4_Product.py
│   ├── 5_Seller.py
│   ├── 6_Payment.py
│   ├── 7_Review.py
│   ├── 8_Delivery_Fulfilment.py
│   └── 9_AI_Analyst.py
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── data_model.py
│   ├── customer_analysis.py
│   ├── sales_analysis.py
│   ├── category_analysis.py
│   ├── product_analysis.py
│   ├── seller_analysis.py
│   ├── payment_analysis.py
│   ├── review_analysis.py
│   ├── delivery_analysis.py
│   └── ai_engine.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
## Dataset

This project uses the **Olist Brazilian E-Commerce Public Dataset**.

The dataset contains information related to:

- Customers
- Orders
- Order items
- Products
- Sellers
- Payments
- Reviews
- Geolocation
- Product category translations
The data is used to calculate business metrics and generate insights through the dashboard.
## How to Run the Project
### 1. Clone the repository

```bash
git clone https://github.com/ayushvaryani4-maker/Olist_Business_Intelligence.git
cd Olist_Business_Intelligence
### 2. Create a virtual environment

```bash
python -m venv .venv
On Windows:

```powershell
.venv\Scripts\activate
### 3. Install dependencies

```bash
pip install -r requirements.txt
### 4. Configure the Gemini API
Create the following file:

```text
.streamlit/secrets.toml
Add your Gemini API key to the file:

```toml
GEMINI_API_KEY = "your_api_key_here"
### 5. Run the dashboard

```bash
streamlit run app.py