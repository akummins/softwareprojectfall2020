from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thingstodo import *
import nltk
import random
nltk.download('vader_lexicon')
# entry = "awful terrible day"


def mood(entry):
    """Uses Sentiment Analysis to score based on a users inputted journal entry and returns a fact/thing to do/mood booster based on mood"""
    score = SentimentIntensityAnalyzer().polarity_scores(entry)
    negative = score['neg']
    neutral = score['neu']
    positive = score['pos']
    if positive >= .75:
        return excitedthings
    elif positive >= .5:
        return happythings
    elif negative >= .75:
        return depressedthings
    elif negative >= .5:
        return sadthings
    else:
        return "We don't know what to tell you, bro. Your emotions are too much for us, but we hope your day is better tomorrow."




# def main():
#     mood(entry)
  

# if __name__ == "__main__":
#     main()


