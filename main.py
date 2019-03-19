import pyttsx3
import random
import tables

engine = pyttsx3.init()

def respond(userSaid):
	for key in tables.responses.keys():
		if key in userSaid.lower():
			if '%s' in tables.responses[key]:
				print(tables.responses[key] % userSaid.lower().replace(key, ''))
				engine.say(tables.responses[key] % userSaid.lower().replace(key, ''))
			else:
				print(tables.responses[key])
				engine.say(tables.responses[key])
			engine.runAndWait()
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