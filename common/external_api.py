import requests


class ExternalApiConnector:

    def __init__(self, make, model):
        self._url = 'https://vpic.nhtsa.dot.gov/api/'
        self.make = make
        self.model = model

    def check_in_api_db(self):
        """Metoda tworzy workspace w GeoServerze."""

        response = requests.get(f'{self._url}vehicles/GetModelsForMake/{self.make}?format=json')

        boolean = False

        if not response.ok:
            raise ValueError('Error: {response}'.format(response=response.text))
        else:
            if self.model.lower() in [result['Model_Name'].lower() for result in response.json()['Results']]:
                boolean = True

            return boolean
