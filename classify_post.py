import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
import json

model_file_path = 'toxic_comment_classifier.pkl' # Classifier
# Note: This should be created using python automod_model.py beforehand.

output_json_path = 'posts.json' # Could replace with original?

# reuse model without training again:
with open(model_file_path, 'rb') as model_file:
    classifier = pickle.load(model_file)

def create_feature_set(text):
    words = word_tokenize(text.lower())
    return {word: True for word in words}

# Example json, replace with actual posts:
with open("posts.json", "r", encoding="utf-8") as json_file:
    post_data = json.load(json_file)

def classify_post(post):
    features = create_feature_set(post['post_text']) # could replace 'post_text' with whatever the post label is
    prediction = classifier.classify(features)
    return prediction

for post in post_data:
    result = classify_post(post)
    post['bannable_detected'] = True if result else False # Adds new field

# Writes the data back to a new JSON file:
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(post_data, json_file, ensure_ascii=False, indent=4)

# REMOVE THIS LINE, ONLY FOR DEBUGGING:
print(json.dumps(post_data, ensure_ascii=False, indent=4))