from textblob import TextBlob

def analyze_sentiment(comments):

    results = []

    positive = 0
    negative = 0
    neutral = 0

    for comment in comments:

        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
            positive += 1

        elif polarity < 0:
            sentiment = "Negative"
            negative += 1

        else:
            sentiment = "Neutral"
            neutral += 1

        results.append({
            "comment": comment,
            "sentiment": sentiment
        })

    return results, positive, negative, neutral