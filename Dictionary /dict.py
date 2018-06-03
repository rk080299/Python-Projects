import json
from difflib import get_close_matches

data = json.load(open("/home/leo/Downloads/data.json"))


def send(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) > 0:
		return ("Did you mean %s instead? Press Yes Or No" %get_close_matches(word, data.keys())[0])

	else:
		return "The word doesn't exist.Please double check it"
