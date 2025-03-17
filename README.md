
# Automoderator

This is a moderation bot that uses a [Logistic Regression](https://en.m.wikipedia.org/wiki/Logistic_regression) model in NLTK to classify posts as bannable, and then writes/updates the JSON to include an "is_bannable" label.

## How to use:

1. You can activate the necessary modules by running *python -m venv .venv* and calling "./venv/Scripts/activate".

3. To connect to your postgreSQL database, add the connection details in the [query.py](https://github.com/Jackrose320/Automod-Classifier/blob/master/query.py) file.

4. If you would like to change the automod model to view different languages or use less sample data, you must write the changes in automod_model.py and run this file to change [toxic_comment_classifier.pkl](https://github.com/Jackrose320/Automod-Classifier/blob/master/toxic_comment_classifier.pkl).

*Note, this file has already been loaded and is the complete model with all data trained (this is why it is so large!). It would be a pain to download it, so think carefully before downloading without changing the model parameters.*

3. Then, run sh run_all.sh with the necessary JSON files added (and the output JSON changed) in query.py.

## What does this do?

This program takes details for a postgreSQL database that has "post" fields, and creates a json of the post content and post IDs. From there, it turns this data into a json. The classifier reads this json for the post content and declares each post as being "bannable" or not. It gives this label to a new "is_bannable" label in the same json file, corresponding to each post!

## Dataset:
[Larry Freeman multi-lingual Set](https://www.kaggle.com/datasets/larryfreeman/toxic-comments-french-spanish-german-train)
*478713 data points!*
