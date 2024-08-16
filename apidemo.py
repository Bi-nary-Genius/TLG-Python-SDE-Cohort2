import requests

url = "https://anapioficeandfire.com/api/characters/583"

http_response = requests.get(url)

requests.get()
requests.post()
requests.delete()
requests.put()

jon_snow_dict = http_response.text

