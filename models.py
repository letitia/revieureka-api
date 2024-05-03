from pydantic import BaseModel


class Review(BaseModel):
    review_id: str
    review_text: str

class RelevantReviewsResponse(BaseModel):
    relevant_reviews: list[Review]

class Insight(BaseModel):
    target_product: str
    jtbd_heading: str
    insight_text: str

class InsightsResponse(BaseModel):
    insights: list[Insight]

