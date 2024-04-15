import requests
from bs4 import BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Python_(langage)"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

# Trouver l'élément qui contient le titre de l'article
titre_elem = soup.find('h1', id='firstHeading')
#trouver la paragraphe
paragraphe_elem = soup.find('div', class_='mw-parser-output').find('p')

# Trouver et afficher les titres des sections principales
sections = soup.find_all('span', class_='mw-headline')

# Extraire et afficher le titre de l'article
if titre_elem:
    titre = titre_elem.text.strip()
    print(f"Titre de l'article : {titre}")
else:
    print("Titre non trouvé")

# Extraire et afficher le premier paragraphe du contenu principal
if paragraphe_elem:
    paragraphe = paragraphe_elem.text.strip()
    print(f"\nPremier paragraphe : {paragraphe}")

# Extraire et afficher les titres des sections principales
if sections:
    print("\nSections principales :")
    for section in sections:
        titre_section = section.text.strip()
        print(f"- {titre_section}")