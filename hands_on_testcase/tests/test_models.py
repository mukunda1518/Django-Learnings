# import pytest
# import datetime
# from freezegun import freeze_time
#
from hands_on_testcase.models import RideRequest
#
#
# @pytest.mark.django_db
# @freeze_time("2020-06-15 05:30")
# def test_ride_request_created(populate_ride_requests):
#     # Arrange
#     no_of_records = 1
#
#     # Act
#     actual_records = RideRequest.objects.all()
#
#     # Assert
#     assert no_of_records == actual_records
#
from django.test import TestCase
from django.utils import timezone


class RideRequestTest(TestCase):

    def create_ride_request(self, source="Kurnool", destination="Hyderabad", travel_date_time=timezone.now(), luggage_quantity=6):
        return RideRequest.objects.create(source=source, destination=destination, travel_date_time=travel_date_time, luggage_quantity=luggage_quantity)

    def test_ride_request_creation(self):
        r = self.create_ride_request()
        self.assertTrue(isinstance(r, RideRequest))
