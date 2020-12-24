import cryptocompare
import time
from sms import sendsms

lastPrice = 0

while True:
    priceString = str(cryptocompare.get_price('BTC', curr = 'USD'))
    priceStringAltered = priceString.translate({ord('}'): None})
    priceArray = priceStringAltered.split(": ")
    priceString = priceArray[2]
    priceFloat = int(float(priceString))

    #if price is within bounds and the last price that was 
    #sent wasnt within those bounds send price and reassign last price

    if priceFloat in range(22400, 22500):
        pass
    elif priceFloat in range(23400, 23500):
        if lastPrice in range(23400, 23500):
            pass

    #waits 120 seconds or 2 minutes until script runs again as to not spam phone
    time.sleep(120)


