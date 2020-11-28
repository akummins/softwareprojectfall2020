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
        rec = random.choice(excitedthings)
        return "excited." f'We reccomend to: {rec}'
    elif .2 >= negative >= 0 and  .5 >= neutral >= 0 and positive >= .5:
        rec = random.choice(happythings)
        return "happy." #f'{rec}'
    elif negative >= .75 and  .5 >= neutral >= 0 and positive <= .2:
        rec = random.choice(depressedthings)
        return "depressed." f'We reccomend to: {rec}'
    elif negative >= .5 and  .5 >= neutral >= 0 and positive <= .2:
        rec = random.choice(sadthings)
        return "sad." f'We reccomend to: {rec}'
    else:
        return "We don't know what to tell you, bro. Your emotions are too much for us, but we hope your day is better tomorrow."




# def main():
#     mood(entry)
  

# if __name__ == "__main__":
#     main()


