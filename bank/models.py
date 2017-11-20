from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return '{}: {}'.format(self.name, self.id)

    @classmethod
    def get_currency(cls, name):
        try:
            currency = cls.objects.get(name=name)
        except cls.DoesNotExist:
            currency = cls.objects.create(name=name)
        return currency


class ExchangeRate(models.Model):
    ccy = models.ForeignKey(Currency, related_name='exchange_rates')
    base_ccy = models.ForeignKey(Currency, related_name='base_exchange_rates')
    buy = models.DecimalField(max_digits=100000, decimal_places=4)
    sale = models.DecimalField(max_digits=100000, decimal_places=4)

