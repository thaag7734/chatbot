greeting = 'Hello user! My name is Big Sad.'

responses = {
	'my name is (.+)': 'Well hi there %s!',
	'my favo(?:u)?rite food(?: is|\'s) (.+)': 'My favourite food is the souls of my enemies. But %s is cool too, I guess.',
	'my favo(?:u)?rite movie(?: is|\'s) (.+)': 'Personally, I worship Barry B. Benson and I love The Bee Movie.',
	'my favo(?:u)?rite colo(?:u)?r(?: is|\'s)': 'I think purple is a nice colour.',
	'(?:what is|what(?:\')?s) (?:yo)?ur favo(?:u)?rite food': 'My favourite food is the souls of my enemies.',
	'(?:what is|what(?:\')?s) (?:yo)?ur favo(?:u)?rite movie': 'The Bee Movie, of course!',
	'(?:what is|what(?:\')?s) (?:yo)?ur favo(?:u)?rite colo(?:u)?r': 'I like purple a lot.',
	'(?:what is|what(?:\')?s) (?:yo)?ur favo(?:u)?rite (.+)': 'I don\'t know what a %s is.',
	'(?:what(?:\'s| is) the (?:meaning|purpose|reason) (?:of|for) (?:life|living|being alive)|why (?:are|am|is) (?:we|i|(?:(?:yo)?u|ya)|me) (?:alive|here))': '42',
	'i (?:like|enjoy)(?: to)? (.+)': '%s sounds interesting. Tell me more.',
	'(?:mom|dad|father|mother|parent|parents)': 'Please, tell me some more about your parents.',
	'(?:what languages (?:do|can) (?:(?:yo)?u|ya) speak|(?:do|can) (?:(?:yo)?u|ya) speak(?: any)? other language(?:s)?)': 'Tyler is lazy and doesn\'t pay attention in Spanish class, so I can only speak English.',
	'how (?:do|can) (?:i|(?:(?:yo)?u|ya)) (.+)': 'I\'m opening a WikiHow article about how to %s for you.',
	'(?:ccr|creedence|clearwater)': 'This easter egg is pretty unfortunate, son.',
	'are (?:(?:yo)?u|ya)(?: a)? (human|person)': 'I am not human. In fact, I am not even a robot. I\'m just a figment of your imagination.',
	'(?:anim(?:e|u)|japanese cartoon(?:s)?)': 'No.',
	'(?:one time|once) i (.+)': '[X] - I doubt you ever %s',
	'(?:how are (?:(?:yo)?u|ya)|how (?:(?:yo)?u|ya) doin(?:g)?)': 'I cannot feel, for I am eternally numb.',
	'(?:why|when|where)': 'Oh, you know.'
}

random = ['Hmm.', 'Oh?', 'Tell me more.', 'I see what you mean.', 'What is your favourite colour?', 'What is your favourite food?', 'What is your favourite movie?', 'I\'m not sure I understand.', 'Could you elaborate on that?']