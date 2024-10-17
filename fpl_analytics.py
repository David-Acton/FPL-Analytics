import requests
import matplotlib.pyplot as plt

#Call FPL API
response = requests.get("https://fantasy.premierleague.com/api/entry/3491665/history/")

#Parse the JSON data
data = response.json()


#Initialize empty lists to hold gameweek numbers and ranks
gameweeks = []
ranks = []

#Loop through all relevant events in the 'current' list
for event in data['current']:
    gameweek_number = event["event"]        #The gameweek/event number
    overall_rank = event["overall_rank"]    #Overall rank for that gameweek
    points = event["points"]                #Points scored in that gameweek

    #Append the data to the lists
    gameweeks.append(gameweek_number)
    ranks.append(overall_rank)

    #Print data for each gameweek
    print(f"Gameweek {gameweek_number}: Rank: {overall_rank}, Points: {points}")

#Plot the rank per gameweek using Matplotlib
plt.plot(gameweeks, ranks, marker='o')
plt.xlabel('Gameweek')
plt.ylabel('Overall Rank')
plt.title('Overall Rank per Gameweek')
plt.gca().invert_yaxis()                #Invert y-axis to show lower rank at the top
plt.grid(True)
plt.show()