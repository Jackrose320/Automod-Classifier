import pickle
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
from nltk.tokenize import word_tokenize

from sklearn.linear_model import LogisticRegression
from nltk.classify.scikitlearn import SklearnClassifier

import pandas as pd
import kagglehub as kh

# Download latest version
path = kh.dataset_download("larryfreeman/toxic-comments-french-spanish-german-train")

print("Path to dataset files:", path)
dfs = [
    pd.read_csv(f"{path}\\train_de.csv", usecols=['comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'], low_memory=False),
    pd.read_csv(f"{path}\\train_es.csv", usecols=['comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'], low_memory=False),
    pd.read_csv(f"{path}\\train_fr.csv", usecols=['comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'], low_memory=False)
]
df = pd.concat(dfs, ignore_index=True) # Can be removed in place of:
# This can be added to make the training data unilingual:
# df = dfs[1]
print("Concatenated dfs")
df['bannable'] = df['toxic'] + df['severe_toxic'] + df['obscene'] + df['threat'] + df['insult'] + df['identity_hate'] >= 2
print("Created bannable section")
df = df[['comment_text', 'bannable']]
print("Shortened dataset")

def create_feature_set(text):
    words = word_tokenize(text.lower())
    return {word: True for word in words}

df = df.dropna(subset=['comment_text'])
# This can be added to make the training data (much) shorter:
# df = df.sample(n=2000)

training_data = [(create_feature_set(row['comment_text']), row['bannable']) for _, row in df.iterrows()]
print("Created the training data")

lr_classifier = SklearnClassifier(LogisticRegression())
lr_classifier.train(training_data)
print("Trained classifier.")

# reuse model without training again:
with open('toxic_comment_classifier.pkl', 'wb') as model_file:
    pickle.dump(lr_classifier, model_file)