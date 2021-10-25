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

logo1 = (colored("""  ___  _   ___   ____  __""", "red"))

logo2 = (colored(""" / _ \| \ | \ \ / /\ \/ /""", "blue"))

logo3 = (colored("""| | | |  \| |\ V /  \  /""", "yellow"))

logo4 = (colored("""| |_| | |\  | | |   /  \ """, "green"))

logo5 = (colored(""" \___/|_| \_| |_|  /_/\_\ """, "magenta"))
print("")
print(logo1)
print(logo2, " [", colored("OK", "green"), "]", textes["start"])
print(logo3, "  [", colored("INFO", "blue"), "]", textes["helpstart"])
print(logo4, " [", colored("INFO", "blue"), "]", textes["infoconfig"])
print(logo5, "[", colored("INFO", "blue"), "]", textes["awoydev"])

while True:
    print(" ")
    name = os.environ["USER"]
    command = input(f"onyx@${name}~$ ")

    if command == "help":
        os.system("clear")
        print(" ")
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
        os.system("clear")
        nameapp = input("Choissisez le nom de l'application\nSi l'application que vous voulez ouvrir contient des espaces met le nom de l'application dans des \"\" \n")
        os.system(f"open -a {nameapp}")
        print(f"L'application {nameapp} s'est ouverte avec succès !\n")
    
    elif command == "bitcoin":
        os.system("clear")
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        resp = requests.get(url)
        json = resp.json()
        print(json["bpi"][settings["bitcoin"]]["rate"])

    elif command == "questionnaire":
        os.system("clear")
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
        os.system("clear")
        message = input("Veuillez spécifier un message\n")
        print(pyfiglet.figlet_format(message))


    else:
        print("[", colored("ERR", "red"), f"] {command} : ", textes["error"])
