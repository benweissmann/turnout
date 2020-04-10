from django.db import models

from common.utils.models import TimestampModel


class USVFModel(TimestampModel):
    external_id = models.IntegerField(primary_key=True)
    external_updated = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Region(USVFModel):
    name = models.TextField(null=True)
    municipality = models.TextField(null=True, db_index=True)
    municipality_type = models.TextField(null=True)
    county = models.TextField(null=True, db_index=True)
    state = models.ForeignKey("election.State", null=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ["external_id"]

    def __str__(self):
        return self.name


class Office(USVFModel):
    hours = models.TextField(null=True)

    class Meta:
        ordering = ["external_id"]


class Address(USVFModel):
    office = models.ForeignKey(Office, null=True, on_delete=models.CASCADE)
    city = models.TextField(null=True)

    class Meta:
        ordering = ["external_id"]


class Official(USVFModel):
    office = models.ForeignKey(Office, null=True, on_delete=models.CASCADE)
    title = models.TextField(null=True)

    class Meta:
        ordering = ["external_id"]
