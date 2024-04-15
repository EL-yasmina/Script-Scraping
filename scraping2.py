import requests
from bs4 import BeautifulSoup

def get_title(soup):
    titre_elem = soup.find('h1', id='firstHeading')
    if titre_elem:
        titre = titre_elem.text.strip()
        return titre
    else:
        return "Titre non trouvé"

def get_first_paragraph(soup):
    paragraphe_elem = soup.find('div', class_='mw-parser-output').find('p')
    if paragraphe_elem:
        paragraphe = paragraphe_elem.text.strip()
        return paragraphe
    else:
        return "Paragraphe non trouvé"

def get_main_sections(soup):
    sections = soup.find_all('span', class_='mw-headline')
    if sections:
        section_titles = [section.text.strip() for section in sections]
        return section_titles
    else:
        return []

def main():
    url = "https://fr.wikipedia.org/wiki/Python_(langage)"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    
    titre = get_title(soup)
    paragraphe = get_first_paragraph(soup)
    sections = get_main_sections(soup)


    print(f"Titre de l'article : {titre}")
    print(f"\nPremier paragraphe : {paragraphe}")
    
    if sections:
        print("\nSections principales :")
        for section in sections:
            print(f"- {section}")
    


if __name__ == "__main__":
    main()
