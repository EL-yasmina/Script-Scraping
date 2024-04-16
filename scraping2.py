import requests                                     # import la bibliothèque requests (des requêtes HTTP de différents types : GET, POST, PUT...)
from bs4 import BeautifulSoup                       # import la bibliothèque bs4  pour parser de code html  (trier)

def get_soup():                                    #j'ai defini une fonction qui récupere le contenu d'un article (java) wikipedia par son url.
    url = "https://fr.wikipedia.org/wiki/Java"
    response = requests.get(url)                   # Envoyer une requête HTTP GET à l'URL et récupérer le contenu de la page
    content = response.content                     # Récupérer le contenu
    soup = BeautifulSoup(content, 'html.parser')     #html.parser : C'est l'analyseur intégré de BeautifulSoup pour analyser le HTML.
    return soup

def get_title(soup):                                  
    titre_elem = soup.find('h1', id='firstHeading') #j'ai utilise la méthode find() de BeautifulSoup pour trouver le h1 avec son id
    if titre_elem:          #si l'élement est trouvé elle extrait son texte et le retourne
        titre = titre_elem.text
        return titre
    else:
        return "Titre non trouvé"

def get_first_paragraph(soup):
    paragraphe_elem = soup.find('div', class_='mw-parser-output').find('p')
    if paragraphe_elem:
        paragraphe = paragraphe_elem.text
        return paragraphe
    else:
        return "Paragraphe non trouvé"

def get_sections(soup):
    sections = soup.find_all('span', class_='mw-headline')
    section_titles = []                     #j'ai cree liste vide
    for section in sections:                    #j'ai bouclé sur les sections
        section_titles.append(section.text.strip())    #ajouter le texte de section dans la liste à afficher
    return section_titles




soup = get_soup()              #j'ai appellé la fonction get soup()
titre = get_title(soup)        
paragraphe = get_first_paragraph(soup)
sections = get_sections(soup)


print(f"Titre de l'article : {titre}")
print(f"\nPremier paragraphe : {paragraphe}")

if sections:        #verifier si on a des sections avant d'afficher les sections
    print("\nSections principales :")
    for section in sections:
        print(f"- {section}")
    

