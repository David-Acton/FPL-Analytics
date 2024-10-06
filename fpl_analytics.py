import requests

response = requests.get("https://fantasy.premierleague.com/api/entry/3491665/history/")

print(response.status_code)

print(response.json())

rank = response.json()["current"][0]["overall_rank"]
print(rank)