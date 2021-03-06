
# import pprint
import requests

# SAD 
"""Pulls from an API of dog images to generate a random link every time"""
dogurl = 'https://dog.ceo/api/breeds/image/random'
dogresponse = requests.get(dogurl)
dogpic=dogresponse.json()['message']
sadthings= f'Looks like you are sad. Check out this picture of a dog to cheer you up! Copy and paste the link: {dogpic}' 


# HAPPY
"""Pulls from an API of dad jokes to tell a random joke every time"""
try:
    jokeurl = "https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
        'x-rapidapi-key': "1e4059ac59mshbe991e87567eb1ap10e64cjsn039a54f256d6"
        }
    jokeresponse = requests.request("GET", jokeurl, headers=headers)
    jokesetup=jokeresponse.json()['body'][0]['setup']
    jokepunchline=jokeresponse.json()['body'][0]['punchline']
    happythings = f'Looks like you are happy! Here is a Joke! {jokesetup}  {jokepunchline}'
except:
    print("We've reached the limit for calls to the Jokes API today. Try again tomorrow.")

# EXCITED
"""Pulls from an API of taco recipes to share a new recipe every time"""
tacourl='http://taco-randomizer.herokuapp.com/random/?full-taco=true'
tacoresponse = requests.get(tacourl)
taco=tacoresponse.json()['base_layer']['recipe']
excitedthings = f'Looks like you are excited! You know what goes well with excitement? Tacos! Here is a great taco recipe to make with some friends {taco}'

# DEPRESSED
"""Pulls from an API of cat facts to tell a random fact every time"""
caturl='https://cat-fact.herokuapp.com/facts/random'
catresponse=requests.get(caturl)
fact=catresponse.json()['text']
depressedthings = f'Looks like you are depressed! Here is a cat fact to help cheer you up: {fact}'