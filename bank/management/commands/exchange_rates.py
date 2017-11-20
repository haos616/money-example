from django.core.management.base import BaseCommand
from django.conf import settings

import requests

from bank.models import Currency, ExchangeRate


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = settings.BANK_EXCHANGE_RATES_URL
        response = requests.get(url)
        if response.status_code == 200:
            exchange_rates = response.json()
            for exchange_rate in exchange_rates:
                currency = Currency.get_currency(exchange_rate['ccy'])
                base_currency = Currency.get_currency(exchange_rate['base_ccy'])
                er = ExchangeRate.objects.create(
                    ccy=currency,
                    base_ccy=base_currency,
                    buy=exchange_rate['buy'],
                    sale=exchange_rate['sale'],
                )
                print(er.id)
        else:
            print('Error:', response.status_code)
