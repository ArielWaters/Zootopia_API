import requests

API_KEY = 'pDM0vml8I5BGyCCIMRyx6g==1JAYO00gw92VLbVJ'
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name='
HEADERS = {'X-Api-Key': API_KEY}


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = REQUEST_URL + animal_name
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        animals_data = response.json()
        return animals_data
    else:
        return []


def get_animal_info(animal_data):
    """
    Extracts the type and diet information from the animal data and returns an outcome string.
    """
    animal_type = animal_data['taxonomy']['class']
    animal_diet = animal_data['characteristics']['diet']
