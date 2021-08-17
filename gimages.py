# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

# Once you've created them, save your API and CX / make an .env file in this format :
# export DEVELOPER_KEY=QIzaSyD9G993bcg2049OxR0d9KOZNkjo8AdkMJc
# export CX=9e25cccedd0ad4433

# load the API key and CX code from .env file
if os.path.exists(".env"):
  load_dotenv()
else:
  print(".env file missing, please create one with your API and CX")

# create an 'ims' sub directory if it doesn't already exists
if not os.path.exists('images/'):
  os.mkdir('images/')
spath = 'images/'

# Get env variables
DK = os.environ.get('DEVELOPER_KEY')
CX = os.environ.get('CX')

# custom progressbar function
def my_progressbar(url, progress):
    print(url + " " + progress + "%")

# create google images search - object
gis = GoogleImagesSearch(DK, CX, progressbar_fn=my_progressbar)

def fetch_images(searchfor):
  # using contextual mode (Curses)
  with GoogleImagesSearch(DK, CX) as gis:
    # define search params:
    _search_params = {"q": searchfor, 
        "num": 15, 
        "safe": "high", 
        "fileType": "jpg",
        "imgType": "photo",
        "rights": "cc_publicdomain" 
        #  free for use by anyone for any purpose without restriction under copyright law
        }
    gis.search(search_params=_search_params, path_to_dir=spath)

  print("Finished!")
