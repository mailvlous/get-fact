import requests

r = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
fact = r.json()['text']

print(fact)