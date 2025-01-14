import json
import requests
from bs4 import BeautifulSoup

# from netflix.exceptions import NetflixItemTypeError
from exceptions import NetflixItemTypeError


class Movie:
    def __init__(self, netflix_id, fetch_instantly=True):
        self.netflix_id = netflix_id

        self.name = None
        self.description = None
        self.genre = None
        self.image_url = None
        self.metadata = None

        if fetch_instantly:
            self.fetch()
            self.is_fetched = True
        else:
            self.is_fetched = False

    def __str__(self):
        return self.name if self.name else self.netflix_id

    def __repr__(self):
        return "<Netflix Movie: {name}>".format(name=self.__str__())

    def fetch(self):
        url = "https://www.netflix.com/watch/{netflix_id}".format(netflix_id=self.netflix_id)
        response = requests.get(url)
        # print(response.content)
        # print(type(response.content))
        # print(dir(response.content), '\n\n')
        # How to get from her to parsint data?

        soup = BeautifulSoup(response.content, "html.parser")
        print(soup.text, '\n')
        # print(type(soup.text), '\n')
        # print(dir(soup), '\n\n')
        # soup = soup.text
        ## data = soup.select("[type='application/ld+json']")[1]
        ## oJson = json.loads(data.text)["itemListElement"]
        ## numProducts = len(oJson)
        ## results = []
        ## print(results)

        metadata_script_tag = soup.find("script", type="application/ld+json")
        # print(metadata_script_tag)
        # print(type(metadata_script_tag))
        # print(dir(metadata_script_tag), '\n\n')
        metadata = json.loads(metadata_script_tag.string)

        # Be sure about content
        if not metadata["@type"] == "Movie":
            raise NetflixItemTypeError()

        self.name = metadata["name"]
        self.description = metadata["description"]
        self.genre = metadata["genre"]
        self.image_url = metadata["image"]

        self.metadata = metadata


class TVShow:

    def __init__(self, netflix_id, fetch_instantly=True):
        self.netflix_id = netflix_id

        self.name = None
        self.description = None
        self.genre = None
        self.image_url = None
        self.metadata = None

        if fetch_instantly:
            self.fetch()
            self.is_fetched = True
        else:
            self.is_fetched = False

    def __str__(self):
        return self.name if self.name else self.netflix_id

    def __repr__(self):
        return "<Netflix TVShow: {name}>".format(name=self.__str__())

    def fetch(self):
        url = "https://www.netflix.com/watch/{netflix_id}".format(netflix_id=self.netflix_id)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        metadata_script_tag = soup.find("script", type="application/ld+json")
        metadata = json.loads(metadata_script_tag.text)

        # Be sure about content
        if not metadata["@type"] == "TVSeries":
            raise NetflixItemTypeError()

        self.name = metadata["name"]
        self.description = metadata["description"]
        self.genre = metadata["genre"]
        self.image_url = metadata["image"]

        self.metadata = metadata
