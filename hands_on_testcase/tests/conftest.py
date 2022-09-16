import pytest
from unittest.mock import create_autospec, patch
from freezegun import freeze_time
# from hands_on_testcase.models import RideRequest
import datetime


@pytest.fixture
def order():
    return []


@pytest.fixture
def outer(order, inner):
    order.append("outer")


# @pytest.fixture
# @freeze_time("2020-06-15 05:30")
# def populate_ride_requests():
#     RideRequest.objects.create(
#         source="Kurnool",
#         destination="Hyderabad",
#         travel_date_time=datetime.datetime.now(),
#         luggage_quantity=6
#     )

