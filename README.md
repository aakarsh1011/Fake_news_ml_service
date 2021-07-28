# fake_news_ml_service

## Overview
People are daily bombarded by various types of new from different resources and sometimes some of them are fake. These fake news can lead to various unpleasant events and hence
has to be stopped. This is an practice approach to process news and classify them using Machine Learning into fake or real.

## Workflow
1. All the news data are extracted using the data_acquire script which are labelled. This data is then processed using NLP techniques like stemming, lemmatization and conversion into vectors for our models to understand them.

2. After preparing the data various classification machine learning algorithm were tried and PassiveAgressiceClassifier came out on top.

Disclaimer: As mentioned, this is a practice project and it not hihghly tuned and should not be treated as a tool to confirm any news.
