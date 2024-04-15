import requests
from bs4 import BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Test_de_performance"
response = requests.get(url)

contenu = response.content  # "contenu" est plus clair que "content" en français
soupe = BeautifulSoup(contenu, 'html.parser')

# Extraire tous les éléments "span" avec la classe "mw-headline"
titres = soupe.find_all("span", class_="mw-headline")  # "titres" est plus précis que "typeTest"

# une liste pour stocker les données du tableau
donnees_tableau = []

# Parcourir chaque élément "span" et extraire le texte et l'identifiant
for element in titres:
    texte = element.text.strip()  # "texte" est plus clair que "text"
    identifiant = element['id']  # "identifiant" est plus explicite que "id"
    donnees_tableau.append([texte, identifiant])


# Afficher les données du tableau
print("=====================================================================")
print("| Titre                                              | Identifiant       |")
print("=====================================================================")
for ligne in donnees_tableau:
    print(f"| {ligne[0]:50} | {ligne[1]:15} |")
print("=====================================================================")

