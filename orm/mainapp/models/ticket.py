import uuid
from django.db import models
from django_extensions.db.fields import UUIDField

class UUIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36
        kwargs['unique'] = True
        kwargs['default'] = uuid.uuid4
        super().__init__(*args, **kwargs)

class Ticket(models.Model):

    class Categories(models.TextChoices):
        CATEGORIE_SILVER = "Silver"
        CATEGORIE_GOLD = "Gold"
        CATEGORIE_PLATINUM = "Platinum"

    class Currencies(models.TextChoices):
        EURO = "EUR"
        JAPAN_YEN = "JPY"
        NEW_ZEALAND_DOLLAR = "NZD"

    id = UUIDField(primary_key=True)
    #id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    event = models.ForeignKey("Event", on_delete=models.PROTECT)
    category = models.CharField(max_length=10, choices=Categories.choices)
    seat = models.TextField()
    # Pour ce projet "factice, on représente le prix de façon simple en tant que nombre entier
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=Currencies.choices)

