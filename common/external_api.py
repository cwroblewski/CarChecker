import json
from rest_framework import status
import requests


class ExternalApiConnector:

    def __init__(self, make, vehicle_model):
        self._url = 'https://vpic.nhtsa.dot.gov/api/'
        self._make = make
        self._vehicle_model = vehicle_model

    def check_model_for_make(self):
        try:
            response = requests.get(f'{self._url}vehicles/GetModelsForMake/{self._make}?format=json', timeout=5)
            if not response.ok:
                return status.HTTP_503_SERVICE_UNAVAILABLE
        except requests.exceptions.ConnectionError:
            return status.HTTP_503_SERVICE_UNAVAILABLE
        except requests.exceptions.ReadTimeout:
            return status.HTTP_503_SERVICE_UNAVAILABLE

        else:
            try:
                return status.HTTP_200_OK if response.json()['Results'] and \
                               self._vehicle_model in \
                               [result['Model_Name'].lower() for result in response.json()['Results']] else status.HTTP_404_NOT_FOUND

            except json.decoder.JSONDecodeError:
                return status.HTTP_404_NOT_FOUND
