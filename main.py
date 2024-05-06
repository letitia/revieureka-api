from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import aiplatform
from models import Review, RelevantReviewsResponse, Insight, InsightsResponse, reviews_to_insights_model
import google_auth_oauthlib.flow
import googleapiclient.discovery

app = FastAPI()


# TODO!@$#%@^%&%%# Replace with your project and model information
PROJECT_ID = "sound-memory-419502"
MODEL_NAME = "gemini_jtb_model"  # Replace with your actual model name
MODEL_LOCATION = "your-notebook-region"  # Use the region from notebook metadata

# get transcripts from Youtube link youtube_transcript_api
# from youtube_transcript_api import YouTubeTranscriptApi

# YouTubeTranscriptApi.get_transcript(video_id)

origins = [
    "http://localhost:5173",  # Allow requests from your Vue.js frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/reviews-youtube")
async def get_reviews_youtube(target_product: str):
    print("in get_reviews_youtube")
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        type="video",
        q=f"{target_product} review"
    )
    response = request.execute()

    print(response)
    return {"response": response}

@app.get("/get-reviews-transcript")
async def search_reviews_youtube(target_product: str):
    return {"message": "i'm in search_reviews_youtube"}

# async def filter_reviews_and_extract_insights(reviews: list[Review]):
#     # Initialize AI Platform prediction client
#     aiplatform.init(project=PROJECT_ID, location=MODEL_LOCATION)
#     endpoint = aiplatform.Endpoint(MODEL_NAME)

#     # Prepare input for prediction
#     instances = [{"review_text": review.review_text} for review in reviews]

#     # Get predictions from the Gemini model
#     response = endpoint.predict(instances=instances)
#     predictions = response.predictions

#     # Process predictions and create Insight objects
#     results = [Insight(jtb_analysis=prediction[0]) for prediction in predictions]
#     return results

@app.get("/reviews-to-insights")
async def reviews_to_insights(reviews: list[Review], target_product: str):
    
    gemini_input = f"""
    ## Target Product: {target_product}

    """
    for review in reviews:
        gemini_input += f"""
        ### Review: {review.review_title}
        Channel: {review.channel_name}
        {review.review_url}
        {review.text}
        """
    
    response = reviews_to_insights_model.generate_content(gemini_input)
    insights = response.strip()

    # # Initialize AI Platform prediction client
    # aiplatform.init(project=PROJECT_ID, location=MODEL_LOCATION)
    # endpoint = aiplatform.Endpoint(MODEL_NAME)

    # insights = []
    # for review in reviews:
    #     input_data = {"review_text": review.review_text, "target_product": target_product}
    #     prediction = endpoint.predict(input_data)  # Replace with your model prediction logic.

        # Example: Assuming your model generates text with JTBD category labels
        # for jtb_category, insight_text in prediction["jtb_insights"].items():
        #     jtb_insights.append(Insight(jtb_category=jtb_category, insight_text=insight_text))
    
    return InsightsResponse(target_product=target_product, insights=insights)





@app.get("/")
async def root():
    return {"stuff": "Hello Tish"}

# Endpoint 1: TODO after MVP
# @app.post("/filter-reviews")
# async def filter_reviews(target_product: str, reviews: list[Review]):
#     # Implement filtering code here

#     return RelevantReviewsResponse(relevant_reviews=filtered_reviews)

@app.get("/filter-insights")
async def filter_insights():
    return {"message": "i'm in filter_insights"}

@app.get("/generate-report")
async def generate_report():
    return {"message": "i'm in generate_report"}

