import os
from termcolor import colored
import pyfiglet
import requests
import json

settings = json.load(open("config.json"))
lang = settings["lang"]
textes = json.load(open("textes.json"))[lang]

#################################
# Made by AwoyDev
#################################

print(colored("""
  ___  _   ___   ____  __
 / _ \| \ | \ \ / /\ \/ /
| | | |  \| |\ V /  \  / 
| |_| | |\  | | |   /  \ 
 \___/|_| \_| |_|  /_/\_\ """, "yellow"))
print("")
print("[", colored("OK", "green"), "]", textes["start"])
print("[", colored("INFO", "blue"), "]", textes["helpstart"])
print("[", colored("INFO", "blue"), "]", textes["infoconfig"])

while True:
    command = input(settings["prefix"])

    if command == "help":
        print("")
        print(textes["titlehelp"])
        print(colored("clear", "green"), textes["clearhelp"])
        print(colored("stop", "green"), textes["stophelp"])
        print(colored("openapp", "green"), textes["openapphelp"])
        print(colored("questionnaire", "green"), textes["questionnairehelp"])
        print(colored("ascii", "green"), textes["asciihelp"])
        print(colored("bitcoin", "green"), textes["bitcoinhelp"])
        

    elif command == "clear":
        os.system("clear")
        print("[", colored("CLEAR", "green"), "]", textes["messageclear"])

    elif command == "stop":
        print("[", colored("STOP", "red"), "]", textes["stopmessage"])
        break

    elif command == "openapp":
        nameapp = input("Choissisez le nom de l'application\nSi l'application que vous voulez ouvrir contient des espaces met le nom de l'application dans des \"\" \n")
        os.system(f"open -a {nameapp}")
        print(f"L'application {nameapp} s'est ouverte avec succès !\n")
    
    elif command == "bitcoin":
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        resp = requests.get(url)
        json = resp.json()
        print(json["bpi"][settings["bitcoin"]]["rate"])

    elif command == "questionnaire":
        print("Bien ! Commençons le questionnaire :\n")
        nom = input("Quelle est votre nom ? :\n")
        print(f"Tu as enregistré : {nom}")
        age =  input("Quel est vôtre âge ? :\n")
        print(f"Tu as enregistré : {age}")
        passion = input("Quelle est votre passion ? :\n")
        print(f"Tu as enregistré : {passion}")

        print(colored(f"\n\nVoici la questionnaire fini :\
        \nNom : {nom}\
        \nAge : {age}\
        \nPassion : {passion}", "blue"))

    elif command == "ascii":
        message = input("Veuillez spécifier un message\n")
        print(pyfiglet.figlet_format(message))


    else:
        print("[", colored("ERR", "red"), f"] {command} : ", textes["error"])
