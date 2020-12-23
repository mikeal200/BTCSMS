import cryptocompare
import time
from sms import sendsms

priceString = str(cryptocompare.get_price('BTC', curr = 'USD'))
priceStringAltered = priceString.translate({ord('}'): None})
priceArray = priceStringAltered.split(": ")
price = priceArray[2]

while True:
    priceString = str(cryptocompare.get_price('BTC', curr = 'USD'))
    priceStringAltered = priceString.translate({ord('}'): None})
    priceArray = priceStringAltered.split(": ")
    priceString = priceArray[2]
    priceFloat = int(float(priceString))

    #if price is within bounds and the last price that was 
    #sent wasnt within those bounds send price and reassign last price

    if priceFloat in range(22400, 22500):
        if lastPrice in range(22400, 22500):
            #dont want to spam phone so if the user has
            #already recieved update within range dont do anything
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(22800, 22900):
        if lastPrice in range(22800, 22900):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(22900, 23000):
        if lastPrice in range(22900, 23000):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23000, 23100):
        if lastPrice in range(23000, 23100):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23100, 23200):
        if lastPrice in range(23100, 23200):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23200, 23300):
        if lastPrice in range(23200, 23300):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23300, 23400):
        if lastPrice in range(23300, 23400):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23400, 23500):
        if lastPrice in range(23400, 23500):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23500, 23600):
        if lastPrice in range(23500, 23600):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23600, 23700):
        if lastPrice in range(23600, 23700):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23700, 23800):
        if lastPrice in range(23700, 23800):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23800, 23900):
        if lastPrice in range(23800, 23900):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat
    elif priceFloat in range(23900, 24000):
        if lastPrice in range(23900, 24000):
            pass
        else:
            sendsms(priceString)
            lastPrice = priceFloat

    #waits 120 seconds or 2 minutes until script runs again as to not spam phone
    time.sleep(120)


