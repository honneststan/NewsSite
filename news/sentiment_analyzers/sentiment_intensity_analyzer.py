from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analyzer(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if pos > neg:
        polarity = "Positive Statement"
    elif pos < neg:
        polarity = "Negative Statement"
    else:
        polarity = "Neutral Vibe"


def sentiment_analyzer(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    if pos > neg:
        polarity = "Positive Sentiment"
    elif pos < neg:
        polarity = "Negative Sentiment"
    else:
        polarity = "Neutral Vibe"
    return [pos, neg, neu, polarity]
