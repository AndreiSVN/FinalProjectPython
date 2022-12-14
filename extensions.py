# ==========================================      Классы для работы бота "Конвертер валют"        ====================================

import requests
import json
from configuration import keys


class ConvertException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def currency_convert(origin_cur=str, target_cur=str, amount=int):
        if origin_cur == target_cur:
            raise ConvertException(f'Ну и как Вы себе представляете конвертацию {origin_cur} в {target_cur}?!')
        try:
            origin_cur == keys[origin_cur]
        except KeyError:
            raise ConvertException('Эту валюту мы пока не можем конвертировать, но мы над этим работаем!')
        try:
            target_cur == keys[target_cur]
        except KeyError:
            raise ConvertException('Эту валюту мы пока не можем конвертировать, но мы над этим работаем!')
        try:
            amount == int(amount)
        except ValueError:
            raise ConvertException('Сумму необходимо ввести цифрами! Кстати, мелочь не принимаем, вводите целое число!')

        r = requests.get(
                    f'https://min-api.cryptocompare.com/data/price?fsym={keys[origin_cur]}&tsyms={keys[target_cur]}')
        currency_rate = json.loads(r.content)[keys[target_cur]]

        return currency_rate
