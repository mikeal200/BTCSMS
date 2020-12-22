import cryptocompare
from sms import sendsms

priceString = str(cryptocompare.get_price('BTC', curr = 'USD'))
priceStringAltered = priceString.translate({ord('}'): None})
priceArray = priceStringAltered.split(": ")
price = priceArray[2]

if int(float(price)) <= 25000:
    sendsms(price)


