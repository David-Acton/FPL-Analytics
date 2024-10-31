import requests
import matplotlib.pyplot as plt

def fetch_fpl_data(account_id):

    #Call FPL API
    response = requests.get("https://fantasy.premierleague.com/api/entry/" + account_id + "/history/")

    return response.json()

def process_fpl_data(data):

    #Initialize empty lists to hold gameweek numbers and ranks
    gameweeks = []
    ranks = []

    #Loop through events in current to get data
    for event in data["current"]:
        gameweeks.append(event["event"])
        ranks.append(event["overall_rank"])

        #Print data for each gameweek
        print(f"Gameweek {event['event']}: Rank: {event['overall_rank']}, Points: {event['points']}")

    return gameweeks, ranks

def plot_fpl_rank(gameweeks, ranks):

    #Plot the rank per gameweek using Matplotlib
    plt.plot(gameweeks, ranks, marker='o')
    plt.xlabel('Gameweek')
    plt.ylabel('Overall Rank')
    plt.title('Overall Rank per Gameweek')
    plt.gca().invert_yaxis()                #Invert y-axis to show lower rank at the top
    plt.grid(True)
    plt.show()

def main():

    #Input account ID to retrieve account info
    account_id = input("Please enter your FPL account ID: ")

    #Fetch data & process
    data = fetch_fpl_data(account_id)
    gameweeks, ranks = process_fpl_data(data)

    #Plot rank per gameweek
    plot_fpl_rank(gameweeks, ranks)

if __name__ == "__main__":
    main()