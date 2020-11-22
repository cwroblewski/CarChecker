import json

import requests


class ExternalApiConnector:

    def __init__(self, make, vehicle_model):
        self._url = 'https://vpic.nhtsa.dot.gov/api/'
        self._make = make
        self._vehicle_model = vehicle_model

    def check_model_for_make(self):
        response = requests.get(f'{self._url}vehicles/GetModelsForMake/{self._make}?format=json')

        if not response.ok:
            return response.status_code

        else:
            try:
                return True if response.json()['Results'] and \
                               self._vehicle_model in \
                               [result['Model_Name'].lower() for result in response.json()['Results']] else False

            except json.decoder.JSONDecodeError:
                return False
