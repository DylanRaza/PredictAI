import requests
import pandas as pd

def fetch_upcoming_matches(league_id, season):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    querystring = {"league": league_id, "season": season, "status": "NS"}  # NS stands for Not Started
    headers = {
        "X-RapidAPI-Key": "c726a5debcmsh7031fb1931dce90p14b1efjsnb7c7aa85b88e",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()['response']
        if data:
            return pd.DataFrame({
                'fixture_id': [match['fixture']['id'] for match in data],
                'date': [match['fixture']['date'] for match in data],
                'home_team': [match['teams']['home']['name'] for match in data],
                'away_team': [match['teams']['away']['name'] for match in data]
            })
        else:
            print("No upcoming matches found.")
            return pd.DataFrame()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return pd.DataFrame()

def display_upcoming_matches(league_id, year):
    # Ici, assurez-vous que la fonction ne retourne jamais None
    try:
        # Votre logique pour récupérer les matchs
        data = {
            'fixture_id' : [1,2],
            'date': ['2024-05-12', '2024-05-12'],
            'home_team': ['Chelsea', 'Manchester City'],
            'away_team': ['Liverpool', 'Arsenal']
        }
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Failed to retrieve matches: {e}")
        # Retourner un DataFrame vide en cas d'erreur
        return pd.DataFrame()
    

