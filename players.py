import requests

def infoPlayers(met,apiKey,playerId):
    url=f"https://apiv2.allsportsapi.com/football/?met={met}&APIkey={apiKey}&playerId={playerId}"
    response=requests.get(url)
    try:
        if response.status_code==200:
            print("La requête est réussi (OK 200)") 
            data=response.json()
            for elt in data['result']:
                player_name=elt.get('player_name', 'N/A')
                player_number=elt.get('player_number', 'N/A')
                player_age=elt.get('player_age', 'N/A')
                player_goals=elt.get('player_goals', 'N/A')
                print(f"Les infos du joueur démandé sont: Nom: {player_name}| Numéro: {player_number} | Age: {player_age} | Goals: {player_goals}")   
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)

metV1="Players"
apiKey="e4cbdfdb4ff3150de154c810d2f379eb96327fca07378933d56d3e67df8a7db6"
playerId="103051168"
reponse= infoPlayers(metV1, apiKey, playerId)
print(reponse)