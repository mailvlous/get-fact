import requests
import pyperclip

r = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
fact = r.json()['text']

pyperclip.copy(fact)

print(fact)