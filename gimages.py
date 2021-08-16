# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# |r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

# load the API key and CX code from .env file
load_dotenv()
# create an 'ims' sub directory
pathz = 'ims/'
print(pathz)

DK = os.environ.get('DEVELOPER_KEY')
CX = os.environ.get('CX')

# custom progressbar function
def my_progressbar(url, progress):
    print(url + " " + progress + "%")

# create google images search - object
gis = GoogleImagesSearch(DK, CX, progressbar_fn=my_progressbar)

# using contextual mode (Curses)
with GoogleImagesSearch(DK, CX) as gis:
    # define search params:
    _search_params = {"q": "tree", 
        "num": 3, 
        "safe": "off", 
        "fileType": "png"
        }
    gis.search(search_params=_search_params, path_to_dir=pathz)

print("\nDone\n")
