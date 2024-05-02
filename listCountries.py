import requests

def listCountries(metV1, apiKey):
    url = f"https://apiv2.allsportsapi.com/football/?met={metV1}&APIkey={apiKey}"
    response=requests.get(url)
    try:
        if response.status_code == 200:
            print("La requête a réussi (200 OK)")
            # Traitez la réponse ici
            data = response.json()
            for pays in data['result']:  # Parcourez la liste des pays
                pays_name = pays.get('country_name', 'N/A')
                print("Pays:", pays_name)
        else:
            print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête à l'API :", e)
    except ValueError as e:
        print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)


metV1="Countries"
apiKey="e4cbdfdb4ff3150de154c810d2f379eb96327fca07378933d56d3e67df8a7db6"
reponse= listCountries(metV1, apiKey)
print(reponse)