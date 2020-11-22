import json
import requests


class ExternalApiConnector:

    def __init__(self, make, vehicle_model):
        self._url = 'https://vpic.nhtsa.dot.gov/api/'
        self._make = make
        self._vehicle_model = vehicle_model

    def check_model_for_make(self):
        response = requests.get(f'{self._url}vehicles/GetModelsForMake/{self._make}?format=json')

        is_ok = False

        if not response.ok:
            return is_ok
        else:
            try:
                if response.json()['Results'] and self._vehicle_model in [result['Model_Name'].lower() for result in response.json()['Results']]:
                    is_ok = True
                return is_ok

            except json.decoder.JSONDecodeError:
                return is_ok
