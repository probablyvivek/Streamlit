#scrape all the icons from https://img.pokemondb.net/sprites/sword-shield/icon/
import os
import requests
from bs4 import BeautifulSoup

def download_file(url, file_name):
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return file_name


# get all the pokemon
url = 'https://pokemondb.net/pokedex/all'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('a', class_='ent-name')

for result in results:
    link = result['href']
    pokemon = result.text
    url = 'https://img.pokemondb.net/artwork/' + pokemon.lower() + '.png'
    file_name = pokemon.lower() + '.png'
    if not os.path.isfile(file_name):
        print('Downloading ' + pokemon + '...')
        download_file(url, file_name)