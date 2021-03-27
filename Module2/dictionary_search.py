import requests

class Dictionary:
	def __init__(self,word):
		self.url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
		self.Word = word


    # Function to search a given word in dictionary
	def search(self):
		if not self.Word:
			print("Please enter a valid input")
			return

		response = requests.get(self.url+self.Word)
		
		try:
			dictionary = response.json()[0]

			print('\033[1m' + self.Word.capitalize()+".")
			for meaning in dictionary['meanings']:
				result = ''
				partOfSpeech = meaning['partOfSpeech']
				definitions = meaning['definitions'][0]['definition']
				result = partOfSpeech.capitalize() +". "+definitions.capitalize()
				print('\033[0m' + result)
		
		except:
			print('\033[91m' + "Word Not Found"+ '\033[0m')





# Ask word to search from user
word = input("\n Word? ")

# Object of class Dictionary
my_dictionary = Dictionary(word)
my_dictionary.search()
