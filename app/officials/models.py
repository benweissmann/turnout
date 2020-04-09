import datetime

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from common.utils.models import TimestampModel, UUIDModel
from common.validators import zip_validator
from election.models import State

class ElectionRegion(UUIDModel, TimestampModel):
    external_id = models.IntField()
    name = models.CharField()
    municipality = models.CharField()
    county = models.CharField()
    state = models.ForeignKey("election.State")

    def __str__(self):
        return self.name

class ElectionOffice(UUIDModel, TimestampModel):
    external_id = models.IntField()
    external_updated = models.DateTimeField()

    region = models.ForeignKey("officials.ElectionRegion")
    mailing_address1 = models.CharField()
    mailing_address2 = models.CharField()
    mailing_address3 = models.CharField()
    mailing_city = models.CharField()
    mailing_state = models.ForeignKey("election.State")
    mailing_zipcode = models.TextField(null=True, validators=[zip_validator])

    website = models.URLField()
    email = models.EmailField(max_length=150)
    phone = PhoneNumberField()
    fax = PhoneNumberField()

    processes_registration = models.BooleanField(default=False)
    absentee_request = models.BooleanField(default=False)
    absentee_return = models.BooleanField(default=False)
    overseas_request = models.BooleanField(default=False)
    overseas_return = models.BooleanField(default=False)

    class Meta(object):
        ordering = ["code"]

    def __str__(self):
        return self.name
