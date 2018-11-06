import requests 
Value =input("What would you like to search for? ")
url = "https://icanhazdadjokes.com/search"
res = requests.get(
	url, 
	headers ={"Accept": "application/json"},
	params={"term":Value}
).json()
numberOfJokes = len(res["results"])






