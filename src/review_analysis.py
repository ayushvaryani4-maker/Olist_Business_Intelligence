import pandas as pd


def get_review_metrics(reviews):
    """
    Calculate key review metrics.

    Parameters:
        reviews (pd.DataFrame): Review dataset.

    Returns:
        dict: Review-related metrics.
    """

    total_reviews = reviews["review_id"].nunique()

    average_review_score = reviews["review_score"].mean()

    review_score_counts = reviews["review_score"].value_counts().sort_index()

    most_common_score = (
        review_score_counts.idxmax()
        if not review_score_counts.empty
        else None
    )

    return {
        "total_reviews": total_reviews,
        "average_review_score": average_review_score,
        "most_common_score": most_common_score,
        "review_score_counts": review_score_counts,
    }