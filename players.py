import requests
import json
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()
apiKey = os.getenv("MY_API")

#cette fonction permet d'enregistrer les donnees dans un fichier json
def enregistrerJson(infoplay):
    # Enregistrez la chaîne JSON dans un fichier
                with open("dataPlayer.json", "w") as jsonFile:
                    json.dump(infoplay, jsonFile, indent=4) 

def infoPlayers(met,playerId):
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
                infoplay={
                    "nom du joueur": player_name,
                    "numero du joeur":player_number,
                    "age du joueur":player_age,
                    "nombre de but":player_goals
                }
                jsonString = json.dumps(infoplay)
                # Affichez la chaîne JSON
                print(jsonString)
                enregistrerJson(infoplay)
                print(f"Les infos du joueur démandé sont: Nom: {player_name}| Numéro: {player_number} | Age: {player_age} | Goals: {player_goals}")   
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)

metV1="Players"
playerId="103051168"
reponse= infoPlayers(metV1, playerId)
print(reponse)