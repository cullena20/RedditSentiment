from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re


def analyze_posts(posts):
    sia = SentimentIntensityAnalyzer()
    results = list()
    for post in posts:
        pol_score = sia.polarity_scores(post.title)
        pol_score['headline'] = post.title
        results.append(pol_score)
    return results


def sentiment_to_df(analyzed_posts):
    df = pd.DataFrame.from_records(analyzed_posts)
    return df


def label_df(df):
    df['label'] = 0  # creates label column
    df.loc[df['compound'] > 0.2, 'label'] = 1  # if compound score is greater than 0.2 we label it as positive
    df.loc[df['compound'] < -0.2, 'label'] = -1  # if compound score is less than -0.2 we label it as positive
    return df


def plot_sentiment(sentiment_df):
    percentages = sentiment_df.label.value_counts(normalize=True) * 100
    sns.barplot(x=percentages.index, y=percentages)
    plt.xlabel = ['Negative', 'Neutral', 'Positive']
    plt.plot()
    plt.show()


def sentiment(sentiment_df):
    percentages = sentiment_df.label.value_counts(normalize=True) * 100
    print("Count:")
    print(sentiment_df.label.value_counts())
    print()
    print("Percentages:")
    print(percentages)
    print()


def get_most_positive(df):
    pd.options.display.max_colwidth = 200
    sorted_df = df.sort_values(by='compound')
    return re.sub(' +', ' ', sorted_df.tail(5)['headline'].to_string(index=False))


def get_most_negative(df):
    pd.options.display.max_colwidth = 200
    sorted_df = df.sort_values(by='compound')
    return re.sub(' +', ' ', sorted_df.head(5)['headline'].to_string(index=False))
