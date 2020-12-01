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
    if positive >= .6:
        return excitedthings
    elif positive >= .5:
        return happythings
    elif negative >= .6:
        return depressedthings
    elif negative >= .4:
        return sadthings
    else:
        return "We can't quite determine what your mood is. Either you aren't feeling much of anything or you need to try again and describe your emotions a bit more."




# def main():
#     mood(entry)
  

# if __name__ == "__main__":
#     main()


