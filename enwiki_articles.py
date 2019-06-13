
import requests
from bs4 import BeautifulSoup
from timeit import default_timer as timer
from keras.utils import get_file

base_url = 'https://dumps.wikimedia.org/enwiki/'
index = requests.get(base_url).text
soup_index = BeautifulSoup(index, 'html.parser')

# Find the links that are dates of dumps
dumps = [a['href'] for a in soup_index.find_all('a') if
         a.text == '20190501/']

dumps_url = base_url + dumps[0]

# Retrieve the html
dump_html = requests.get(dumps_url).text

# Convert to a soup
soup_dump = BeautifulSoup(dump_html, 'html.parser')

files = []
for file in soup_dump.find_all('li', {'class': 'file'}):
    text = file.text
    if 'pages-articles' in text:
        files.append((text.split()[0], text.split()[1:]))

files_to_download = [file[0] for file in files if '.xml-p' in file[0]]

# pages-articles.xml.bz2 and pages-articles-multistream.xml.bz2 both contain the same .xml file.
# Get rid of multistream pages
excluding_multistream=[]
for i in files_to_download:
    if "multistream" in i:
        continue
    else:
        excluding_multistream.append(i)
files_to_download=excluding_multistream
print(f'There are {len(files_to_download)} files to download.')
data_paths = []
start = timer()
for file in files_to_download:
    data_paths.append(get_file(file, dumps_url + file))
    print(data_paths)
end = timer()
print(f'{round(end - start)} total seconds elapsed.')
