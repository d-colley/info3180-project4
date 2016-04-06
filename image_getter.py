import requests
from bs4 import BeautifulSoup
import urlparse

url = "http://s5.photobucket.com/"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
# og_image = (soup.find('meta', property='og:image') or
#                     soup.find('meta', attrs={'name': 'og:image'}))
# if og_image and og_image['content']:
#     print og_image['content']

# thumbnail_spec = soup.find('link', rel='image_src')
# if thumbnail_spec and thumbnail_spec['href']:
#     print thumbnail_spec['href']

def image_dem():
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
       if "sprite" not in img["src"]:
           #print image % urlparse.urljoin(url, img["src"])
           print urlparse.urljoin(url, img["src"])

image_dem()