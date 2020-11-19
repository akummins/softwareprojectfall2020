from nltk.sentiment.vader import SentimentIntensityAnalyzer
from thingstodo import *
import nltk
import random
nltk.download('vader_lexicon')
# entry = "awful terrible day"


def mood(entry):
    score = SentimentIntensityAnalyzer().polarity_scores(entry)
    negative = score['neg']
    neutral = score['neu']
    positive = score['pos']
    if .2 >= negative >= 0 and  .5 >= neutral >= 0 and positive >= .75:
        return "excited"
    elif .2 >= negative >= 0 and  .5 >= neutral >= 0 and positive >= .5:
        return "happy"
    elif negative >= .75 and  .5 >= neutral >= 0 and positive <= .2:
        return "depressed"
    elif negative >= .5 and  .5 >= neutral >= 0 and positive <= .2:
        rec = random.choice(sadthings)
        return "sad." f'We reccomend {rec}'




# def main():
#     mood(entry)
  

# if __name__ == "__main__":
#     main()


