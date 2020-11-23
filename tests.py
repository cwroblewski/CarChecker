from django.urls import reverse
from rest_framework import status
from rest_framework.test import (
    APITestCase,
)

from cars.models import Car
from rate.models import Rate


class CarCheckApiTests(APITestCase):

    def setUp(self):

        car_data = [
            {'make': 'honda', 'model': 'civic'},
            {'make': 'honda', 'model': 'prelude'},
            {'make': 'fiat', 'model': 'spider 2000'},
        ]

        rate_data = [
            {'car': 1, 'rate': 2},
            {'car': 1, 'rate': 3},
            {'car': 1, 'rate': 5},
            {'car': 2, 'rate': 3},
            {'car': 2, 'rate': 5},
            {'car': 3, 'rate': 5},
            {'car': 3, 'rate': 1},
            {'car': 3, 'rate': 2},
            {'car': 3, 'rate': 3},
        ]

        invalid_car_data = [
            {'make': 'Django', 'model': 'Reinhardt'},
            {'make': '1234', 'model': '8658'},
            {'make': True, 'model': False},
        ]

        self.car_url = reverse('car-list')
        self.rate_url = reverse('rate-list')
        self.popular_url = reverse('popular_list')
        self.all_cars = Car.objects.all()
        self.all_rates = Rate.objects.all()
        self.car_data = car_data
        self.rate_data = rate_data
        self.invalid_car_data = invalid_car_data

    def create_cars(self):
        for car in self.car_data:
            Car.objects.create(make=car['make'], model=car['model'])

    def create_rates(self):
        self.create_cars()
        iterator = 1
        for car in self.all_cars:
            for rate_obj in self.rate_data:
                if rate_obj['car'] == iterator:
                    Rate.objects.create(car=car, rate=rate_obj['rate'])
            iterator += 1

    def test_create_car(self):
        """
        Ensure we can create a new car object.
        """

        for car in self.car_data:
            try:
                response = self.client.post(self.car_url, car)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

                new_car = Car.objects.get(make=car['make'], model=car['model'])
                self.assertEqual(new_car.make, car['make'])
                self.assertEqual(new_car.model, car['model'])

            except TypeError:
                self.assertRaises(TypeError, msg='External Api Error')

        self.assertEqual(Car.objects.count(), 3)

    def test_list_cars(self):
        """
        Ensure we can list car objects.
        """
        self.create_cars()

        response = self.client.get(self.car_url)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_model_for_make(self):
        """
        Test check_model_for_make method.
        """

        for data in self.invalid_car_data:
            try:
                response = self.client.post(self.car_url, data)
                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            except TypeError:
                self.assertRaises(TypeError, msg='External Api Error')

    def test_create_rate(self):
        """
        Ensure we can create a new rate object.
        """

        self.create_cars()

        iterator = 1
        for car in self.all_cars:
            for rate_obj in self.rate_data:
                if rate_obj['car'] == iterator:

                    response = self.client.post(self.rate_url, {'car': car.id, 'rate': rate_obj['rate']})

                    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

                    new_rate = Rate.objects.get(car=car.id, rate=rate_obj['rate'])
                    self.assertEqual(new_rate.car_id, car.id)
                    self.assertEqual(new_rate.rate, rate_obj['rate'])

            iterator += 1

        self.assertEqual(Rate.objects.count(), 9)

    def test_list_rates(self):
        """
        Ensure we can list car objects.
        """
        self.create_rates()

        response = self.client.get(self.rate_url)
        self.assertEqual(len(response.json()), 9)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_popular_order(self):
        """
        Check order in /popular.
        """
        self.create_rates()

        response = self.client.get(self.popular_url)
        self.assertEqual([rates_no['rates_no'] for rates_no in response.json()], [4, 3, 2])
