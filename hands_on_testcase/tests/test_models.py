# import pytest
# import datetime
# from freezegun import freeze_time
#
# from hands_on_testcase.models import RideRequest
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
