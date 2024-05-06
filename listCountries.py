import requests
import json
from dotenv import load_dotenv
import os

class Pays:
    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()
    @staticmethod
    def listCountries(metV1, apiKey):
        """cette fonction permet d'afficher la liste des pays pour le league
            params: 
                    metv1: prend comme parametre Countries
                    apiKey: prend apiKey crée
            return une liste de pays et enregistrer dans un fichier json 
        """
        listPays=[]
        url = f"https://apiv2.allsportsapi.com/football/?met={metV1}&APIkey={apiKey}"
        response=requests.get(url)
        try:
            if response.status_code == 200:
                print("La requête a réussi (200 OK)")
                # Traitez la réponse ici
                data = response.json()
                for pays in data['result']:  # Parcourez la liste des pays
                    #pays_name = pays.get('country_name', 'N/A')
                    listPays.append(pays)
                jsonString = json.dumps(listPays)
                # Affichez la chaîne JSON
                print(jsonString)
                # Enregistrez la chaîne JSON dans un fichier
                with open("dataPays.json", "w") as jsonFile:
                    json.dump(listPays, jsonFile, indent=4) 
            else:
                print(f"La requête a échoué avec le code d'erreur : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Une erreur s'est produite lors de la requête à l'API :", e)
        except ValueError as e:
            print("Une erreur s'est produite lors de la conversion de la réponse en JSON :", e)
        return listPays

    @staticmethod
    def PaysSpec(lettre):
        """
        cette fonction permet d'appeler la fonction qui liste tous les pays et recupere 
        une liste speciale de pays qui commence par une lettre donné
        Params: 
            lettre: parametre donné
        returns: 
            une liste des pays qui commence avec la lettre donner
        """
        mondic={}
        info = Pays.listCountries("Countries","e4cbdfdb4ff3150de154c810d2f379eb96327fca07378933d56d3e67df8a7db6")
        for  cle, valeur in info.items():
            if valeur.startswith(lettre):
                mondic[cle]=valeur
        jsonString = json.dumps(mondic)
        # Affichez la chaîne JSON
        print(jsonString)
        # Enregistrez la chaîne JSON dans un fichier
        with open("dataPaysSpec.json", "w") as jsonFile:
            json.dump(mondic, jsonFile, indent=4) 
        return mondic
        
        
        


metV1="Countries"
lettre="A"
# Accéder aux variables d'environnement chargées
apiKey = os.getenv("MY_API")
reponse= Pays.listCountries(metV1,apiKey)
#reponse2= Pays.PaysSpec(lettre)
print(f"list de pays commence par T: {reponse}")


