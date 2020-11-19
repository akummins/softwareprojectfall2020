import requests
url = 'https://api.jokes.one/jod?category=knock-knock'
api_token = "YOUR API KEY HERE"
headers = {'content-type': 'application/json',
	   'X-JokesOne-Api-Secret': format(api_token)}

response = requests.get(url, headers=headers)
#print(response)
#print(response.text)
jokes=response.json()['contents']['jokes'][0]
print(jokes)

sadthings = ['Snuggle up. Climbing under a soft blanket for a few minutes might make us more relaxed and flexible. Researchers found there’s something about contact with soft things that just makes us feel better.',
'See what day it is at https://nationaldaycalendar.com/what-is-national-today/', 'Meditate. Meditation is a quick, effective way to chill out and improve our outlook, and it might even make us smarter. Just a few minutes of sitting quietly, focusing on the breath, and maybe chanting a few Oms (silently or out loud) can snap us out of a funk',
'Go for a walk','Listen to a happy Song','Hang out with a pet. Cuddling, playing, or just chillin’ with Fido can help us feel happier and less stressed.',
'Achieve a goal. Even small successes can have big mood payoffs. Toss a crumpled ball of paper into the trash can Michael Jordan style, win a game of Solitaire, pick up a pencil off the floor using only your toes—in moments you’ll be basking in the glory of accomplishment.','Laugh. Laughter can cheer us up and decrease anxiety—and the best news is it doesn’t have to be “genuine” to have a positive effect. So even when it seems like there’s absolutely nothing funny in all of this world, busting out a big guffaw might just change your mind. Need help getting started? Check out the latest viral youtube videos, the Greatist tumblr, or anything said by Zack Galifianakis.'
]

happythings = [

]

excitedthings = ['Try a new restaurant, with a fun spin! You know that list you’ve been making of restaurants you’ve been dying to check out but haven’t had time to actually go to? Now’s the time to get it out and make a rez. Just because some kids can be picky doesn’t mean you can’t try to excite them with something new and original.', 'Go lumberjack for the evening. The thought of taking a youngster to throw axes may be scary, but in a supervised environment, it’s the best, most exhilarating activity out there. Plus, at some places, anyone 11 and older can participate!',
'Go to an outdoor group fitness class. Combining the pleasure of being outdoors with learning and great exercise. What could be better? Not a whole lot. You would be surprised by the amount of outdoor yoga, dance and cardio classes that allow people of all ages to participate', 
'Plan a picnic in the park. A picnic is an amazing way to get the whole family together. No matter how old you are, you will surely enjoy the beauty of the outdoors, some great grilled food, and endless fun outdoor activities.', 
'Enjoy a hiking adventure. No matter where you live, you’re never too far away from a hiking trail. Hiking is a fantastic family activity, and a way for your family to see the world together. Some hikes can be challenging so be sure to keep an eye on the weather and bring water and snacks!']


depressedthings = ['Chores: Believe it or not, some people find household chores to be calming and therapeutic. Washing dishes, dusting or reorganizing things allows you to refocus your mind and, in the case of reorganization, flexes your creativity as well.',
'Reading: Sometimes, there’s nothing better than getting lost in a good mystery book or spend some time learning about ancient history.','Take a long shower. Warm water soothes our tired bodies and invigorates our cells.',
' Cry, as much as you need. Crying is good for releasing toxic emotions.', 'Get off Instagram for a while. It already makes you feel like crap about who you are(n’t).']