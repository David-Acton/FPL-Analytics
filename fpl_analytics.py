import requests
import matplotlib.pyplot as plt

def fetch_fpl_data(account_id):

    #FPL URL
    url = "https://fantasy.premierleague.com/api/entry/" + account_id + "/history/"

    try:

        #Call API
        response = requests.get(url)

        #Raise HTTP Error
        response.raise_for_status()

        #Parse & return JSON data
        return response.json()
    
    #Raise exceptions for possible errors
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your network and try again.")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
    except requests.exceptions.RequestException as err:
        print(f"An error occured: {err}")
    except ValueError:
        print(f"Failed to parse JSON data. There may be an issue with the API response.")

    return None


def process_fpl_data(data):

    #Initialize empty lists to hold gameweek numbers and ranks
    gameweeks = []
    ranks = []

    if data is None:
        print("No data to process.")
        return gameweeks, ranks
    
    try:
        #Loop through events in current to get data
        for event in data["current"]:
            gameweeks.append(event["event"])
            ranks.append(event["overall_rank"])

            #Print data for each gameweek
            print(f"Gameweek {event['event']}: Rank: {event['overall_rank']}, Points: {event['points']}")
    
    #Raise exceptions for possible errors
    except KeyError as e:
        print(f"Data format error: missing key {e}. The API response structure may have changed.")
    except TypeError:
        print("Data format error: 'data' is not in the expected format")

    return gameweeks, ranks


def plot_fpl_rank(gameweeks, ranks):

    #Check data present
    if not gameweeks or not ranks:
        print("No data available to plot.")
        return
    
    #Plot the rank per gameweek using Matplotlib
    try:
        plt.plot(gameweeks, ranks, marker='o')
        plt.xlabel('Gameweek')
        plt.ylabel('Overall Rank')
        plt.title('Overall Rank per Gameweek')
        plt.gca().invert_yaxis()                #Invert y-axis to show lower rank at the top
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"An error occured while plotting: {e}")


def main():

    while True:
        try:

            #Input account ID to retrieve account info
            account_id = input("Please enter your FPL account ID: ")

            #Validate account ID
            if not account_id.isdigit() or int(account_id) <=0:
                raise ValueError("Account ID must be a postive integer.")
            break

        except ValueError as e:
            print(f"Invalid input: {e} Please try again.")

    #Fetch data & process
    data = fetch_fpl_data(account_id)
    gameweeks, ranks = process_fpl_data(data)

    #Plot rank per gameweek
    plot_fpl_rank(gameweeks, ranks)

if __name__ == "__main__":
    main()