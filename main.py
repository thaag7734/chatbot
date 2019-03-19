import pyttsx3
import random
import tables
import re

engine = pyttsx3.init()

favouriteFood = 'I don\'t know your favourite food.'
favouriteMovie = 'I don\'t know your favourite movie.'
favouriteColour = 'I don\'t know your favourite colour.'

def respond(userSaid):
	global favouriteFood
	global favouriteMovie
	global favouriteColour
	matched = False

	whatfood = re.search('(what is|what(?:\')?s) my favo(?:u)?rite food', userSaid, re.IGNORECASE)
	foodmatch = re.search('my favo(?:u)?rite food is ', userSaid, re.IGNORECASE)
	whatmovie = re.search('(what is|what(?:\')?s) my favo(?:u)?rite movie', userSaid, re.IGNORECASE)
	moviematch = re.search('my favo(?:u)?rite movie is ', userSaid, re.IGNORECASE)
	whatcolour = re.search('(what is|what(?:\')?s) my favo(?:u)?rite colour', userSaid, re.IGNORECASE)
	colourmatch = re.search('my favo(?:u)?rite colo(?:u)?r is ', userSaid, re.IGNORECASE)

	if whatfood:
		print(favouriteFood)
		engine.say(favouriteFood)
		engine.runAndWait()
		matched = True
	elif foodmatch:
		favouriteFood = 'You told me that your favourite food is %s.' % re.search('my favo(?:u)rite food is (.*?)([^a-zA-Z0-9_ -]|$)', userSaid, re.IGNORECASE).group(1)
	elif whatmovie:
		print(favouriteMovie)
		engine.say(favouriteMovie)
		engine.runAndWait()
		matched = True
	elif moviematch:
		favouriteMovie = 'You told me that your favourite movie is %s.' % re.sub('my favo(?:u)rite movie is (.*?)([^a-zA-Z0-9_ -]|$)', userSaid, re.IGNORECASE).group(1)
	elif whatcolour:
		print(favouriteColour)
		engine.say(favouriteColour)
		engine.runAndWait()
		matched = True
	elif colourmatch:
		favouriteColour = 'You told me that your favourite colour is %s.' % re.sub('my favo(?:u)?rite colo(?:u)?r is (.*?)([^a-zA-Z0-9_ -]|$)', userSaid, re.IGNORECASE).group(1)
	
	for key in tables.responses.keys():

		match = re.search(key, userSaid, re.IGNORECASE)
		if match:
			if '%s' in tables.responses[key]:
				print(tables.responses[key] % re.sub(key, '', userSaid, flags=re.IGNORECASE))
				engine.say(tables.responses[key] % re.sub(key, '', userSaid, flags=re.IGNORECASE))
			else:
				print(tables.responses[key])
				engine.say(tables.responses[key])
			engine.runAndWait()
			matched = True
	if matched:
		return getInput()
	return respondRandom()

def respondRandom():
	response = tables.random[random.randint(0, len(tables.random) - 1)]
	print(response)
	engine.say(response)
	engine.runAndWait()
	return getInput()

def getInput():
	userSaid = input('> ')
	respond(userSaid)

print(tables.greeting)
engine.say(tables.greeting)
engine.runAndWait()
getInput()