
# Automoderator

This is a moderation bot that uses a [Logistic Regression](https://en.m.wikipedia.org/wiki/Logistic_regression) model in NLTK to classify posts as bannable, and then writes/updates the JSON to include an "is_bannable" label.

## How to use:

1. You can activate the necessary modules by running "myenv\Scripts\activate".

2. If you would like to change the automod model to view different languages or use less sample data, you must write the changes in automod_model.py and run this file to change [toxic_comment_classifier.pkl](https://github.com/Jackrose320/Automod-Classifier/blob/master/toxic_comment_classifier.pkl).

*Note, this file has already been loaded and is the complete model with all data trained (this is why it is so large!). It would be a pain to download it, so think carefully before downloading without changing the model parameters.*

3. Then, run classify_post.py with the necessary JSON files added (and the output JSON changed).

## Dataset:
[Larry Freeman multi-lingual Set](https://www.kaggle.com/datasets/larryfreeman/toxic-comments-french-spanish-german-train)
*478713 data points!*
