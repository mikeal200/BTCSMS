import cryptocompare

priceString = str(cryptocompare.get_price('BTC', curr = 'USD'))
priceStringAltered = priceString.translate({ord('}'): None})
priceArray = priceStringAltered.split(": ")
price = priceArray[2]

print(price)


