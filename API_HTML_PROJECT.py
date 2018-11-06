import requests 
import pyfiglet
import termcolor

header = pyfiglet.figlet_format("DAD JOKES.COM")
header = termcolor.colored(header, color="blue")
Value =input("What would you like to search for? ")
url = "https://icanhazdadjokes.com/search"
res = requests.get(
	url, 
	headers ={"Accept": "application/json"},
	params={"term":Value}
).json()
numberOfJokes = res["total_jokes"]

results = res["results"]

if numberOfJokes>1:
	print(f"I have {numberOfJokes} jokes for {Value}. ")
	print(results)
else:
    print(f"No jokes found for {Value}.")
    print("Please try with another keyword")







