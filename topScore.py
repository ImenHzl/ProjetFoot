import requests

def topScore(metV1, leagId, apiKey):
    url = f"https://apiv2.allsportsapi.com/football/?met={metV1}&leagueId={leagId}&APIkey={apiKey}"
    response=requests.get(url)
    try:
        if response.status_code == 200:
            print("La requête a réussi (200 OK)")
            # Traitez la réponse ici
            data = response.json()
            for player in data['result']:  # Parcourez la liste des joueurs
                player_name = player.get('player_name', 'N/A')
                team_name = player.get('team_name', 'N/A')
                print("Joueur:", player_name, " | Equipe:", team_name)
        else:
            print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)


metV1="Topscorers"
leagId="207"
apiKey="e4cbdfdb4ff3150de154c810d2f379eb96327fca07378933d56d3e67df8a7db6"
reponse= topScore(metV1, leagId, apiKey)
print(reponse)