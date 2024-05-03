import json
import pathlib
import textwrap


# import os
# from dotenv import load_dotenv
import google.generativeai as genai
import pprint
from load_creds import load_creds

# # client_options.api_key and credentials are mutually exclusive. Commented this out because we're using load_creds
# load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=api_key)

PROJECT_ID = "sound-memory-419502"


# for running the script locally
def main():
    creds = load_creds()

    genai.configure(credentials=creds)


    # json_data = read_json_data(file_path)
    # reviews = parse_json_data(json_data)

    # create your Gemini model and perform training
    # model = genai.GenerativeModel('gemini-pro')
    # # Sanity Check Test
    # response = model.generate_content("What is the meaning of life?")
    # print(response.text)
    
    # Available base models: ['models/chat-bison-001', 'models/text-bison-001', 'models/embedding-gecko-001', 'models/gemini-1.0-pro', 'models/gemini-1.0-pro-001', 'models/gemini-1.0-pro-latest', 'models/gemini-1.0-pro-vision-latest', 'models/gemini-1.5-pro-latest', 'models/gemini-pro', 'models/gemini-pro-vision', 'models/embedding-001', 'models/text-embedding-004', 'models/aqa']
    # print('Available base models:', [m.name for m in genai.list_models()])
    print()
    print('Available base models:', [m.name for m in genai.list_models()])

    # print('Most Recent Tuned models:')

    # most_recent_tuned_model = genai.list_tuned_models()[-1]
    

    # base_model = [
    #     m for m in genai.list_models()
    #     if "createTunedModel" in m.supported_generation_methods][0]
    # base_model

    # version_number = get_latest_version(most_recent_tuned_model)
    # name = ''
    # operation = genai.create_tuned_model(
    #     source_model=base_model.name,
    #     training_data=training_data,
    #     id = name,
    #     epoch_count = 100,
    #     batch_size=4,
    #     learning_rate=0.001,
    # )
    # model = genai.get_tuned_model(f'tunedModels/{name}')

    # print(model)
    # print(model.state)
    # operation.metadata


    # perform training on your Gemini model 

if __name__ == "__main__":
    main()


# def read_json_data(file_path):
#     """Reads JSON data from a file in Cloud Storage."""
#     with tf.io.gfile.GFile(file_path, "r") as f:
#         json_data = json.load(f)
#     return json_data

# def parse_json_data(json_data):
#     """Parses JSON data into a list of dictionaries."""
#     # Assuming your JSON structure is a list of review objects
#     reviews = json_data
#     return reviews

# def create_tuned_reviews_to_insights_model:




# def prepare_data_for_model(reviews):
#     """Prepares data into the format required by your Gemini model."""
#     # Example: Extract relevant fields and create input tensors
#     input_texts = [review["Review Text"] for review in reviews]
#     # ... (Extract other relevant fields and create tensors)

#     # Process the input text for Gemini (e.g., tokenization)
#     # ...

#     # Create input tensors for your model
#     inputs = {
#         "input_text": tf.constant(input_texts),
#         # ... (Add other input tensors)
#     }
#     return inputs

# def training_loop(model, data):
#     """Training loop for your Gemini model."""
#     # ... (Your training logic)

#     # Example: Iterate through batches of data
#     for batch in data:
#         inputs = prepare_data_for_model(batch)
#         # ... (Feed inputs to the model and perform training steps)


file_path = "train_model_reviews_to_insights.json"  # For testing locally
# file_path = "gs://your-bucket/your-data.json"  # Replace with your Cloud Storage path
# json_data = read_json_data(file_path)
# reviews = parse_json_data(json_data)


# # Prepare data for training
# training_data = ...  # Split your data into training, validation, etc.
# training_loop(model, training_data, ...) 



# Template for Training Data Example
# {
#     "Input": {
#         "Target Product": "",
#         "Review": "",
#     },
#     "Output": {
#         "Customer Name": "",
#         "Business as Usual": "",
#         "New Behaviour": "",
#         "Progress the User Wants to Make": "",
#         "Force 1: Push": "",
#         "Force 2: Pull": "",
#         "Force 3: Habits": "",
#         "Force 4: Anxieties": "",
#         "Stage 1: First Thought": "",
#         "Stage 2: Passive Looking": "",
#         "Stage 3: Active Looking": "",
#         "Stage 4: Deciding": "",
#         "Stage 5: Onboarding": "",
#         "Stage 6: Ongoing Use": ""
#     }
# },