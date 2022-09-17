import factory
from datetime import datetime, timedelta


class RideRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "hands_on_testcase.RideRequest"
    source = factory.Sequence(lambda n: "source%d" % n)
    destination = factory.Sequence(lambda n: "destination%d" %n)

    @factory.lazy_attribute
    def travel_date_time(self):
        return datetime.now() + timedelta(10)