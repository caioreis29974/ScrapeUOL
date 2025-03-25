from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
} #If you prefer, change it to your User

url = 'https://noticias.uol.com.br'
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find_all('h3', class_="thumb-title title-xsmall title-lg-small")
text = [elemento.text for elemento in content]
main_titles = [
    *[h2.text.strip() for a in [soup.find('a', class_='title-box')] if (h2 := a.find('h2'))],
    *[h3.text.strip() for h3 in soup.find_all('h3', class_="thumb-title title-xsmall title-lg-small")],
    *[h3.text.strip() for h3 in soup.find_all('h3', class_="thumb-title title-xsmall title-lg-small title-xs-medium")]
]
main_new = list({title for title in main_titles if title.strip()}) or ["Main title not found"]

pd.set_option('display.max_colwidth', 100)
news = pd.DataFrame({'NEWS': text})
main = pd.DataFrame({'MAIN_NEW': main_new})

all_news = pd.DataFrame({
    'NEWS': main['MAIN_NEW'].tolist() + news['NEWS'].tolist()
})

print("Loading News...", end='\r')
sleep(1)
print(f"\n\n{news}\n\n{main}") 

resp = input("Do you want to save this news? [Y/N] ").upper()
if resp == 'Y':
    with open('news.txt', 'w', encoding='utf-8') as f:
        f.write("NEWS\n")
        f.write("\n".join(news['NEWS'].tolist()))
        f.write("\n\n")
        f.write("MAIN NEWS\n")
        f.write("\n".join(main['MAIN_NEW'].tolist()))
    
    print("File 'news.txt' created successfully!")
else:
    print("Unsaved news. The program will be terminated.")
