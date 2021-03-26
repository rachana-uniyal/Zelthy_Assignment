import requests

while 1:
	word = input("\n Word? ")
	if not word:
		print("Please enter a valid input")
		continue

	response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word)
	
	try:
		dictionary = response.json()[0]

		print('\033[1m' + word.capitalize()+".")
		for meaning in dictionary['meanings']:
			result = ''
			partOfSpeech = meaning['partOfSpeech']
			definitions = meaning['definitions'][0]['definition']
			result = partOfSpeech.capitalize() +". "+definitions.capitalize()
			print('\033[0m' + result)
	
	except:
		print('\033[91m' + "Word Not Found"+ '\033[0m')