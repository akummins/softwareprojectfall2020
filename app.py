###PYTHON MOOD RING
##User writes something - journal entry
##Sentiment analysis on journal entry
##Bucket sentiment analysis/mood numbers and compare
        ##moods 
            # sad --
            # happy --
            # angry
            # excited --
            # depressed --
            # tired
## "Sounds like you are ____mood_____. ____________________do something___________"

from flask import Flask, render_template, request
from findmood import *
import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def hello():
    if request.method != "POST":
        return render_template('index.html', error=None)
    elif request.method == "POST":
        entry = request.form["entry"]
        yourmood = mood(entry)
        return render_template('mood.html', yourmood=yourmood)