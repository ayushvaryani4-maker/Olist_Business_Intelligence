import streamlit as st

from src.data_loader import load_data
from src.review_analysis import get_review_metrics

st.title("Review Analysis")

data = load_data()

reviews = data["reviews"]

# Review Overview
st.subheader("Review Overview")

review_metrics = get_review_metrics(reviews)

total_reviews = review_metrics["total_reviews"]
average_score = review_metrics["average_review_score"]
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Reviews",
        total_reviews
    )

with col2:
    st.metric(
        "Average Review Score",
        f"{average_score:.2f} / 5"
    )

# Review Score Distribution
st.subheader("Review Score Distribution")

review_scores = review_metrics["review_score_counts"]

st.bar_chart(review_scores)

st.dataframe(
    review_scores
    .reset_index(name="Number of Reviews"),
    use_container_width=True
)

# Positive vs Negative Reviews
st.subheader("Positive vs Negative Reviews")

positive_reviews = (reviews["review_score"] >= 4).sum()
negative_reviews = (reviews["review_score"] <= 2).sum()
neutral_reviews = (reviews["review_score"] == 3).sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Positive Reviews",
        positive_reviews
    )

with col2:
    st.metric(
        "Neutral Reviews",
        neutral_reviews
    )

with col3:
    st.metric(
        "Negative Reviews",
        negative_reviews
    )