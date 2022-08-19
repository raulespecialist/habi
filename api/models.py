from django.db import models

class Property(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=32)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Status(models.Model):
    name = models.CharField(unique=True, max_length=32)
    label = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'status'


class StatusHistory(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status_history'
