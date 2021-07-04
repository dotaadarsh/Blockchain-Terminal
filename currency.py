# Getting Bitcoin value for a particular amount and currency
from blockchain import exchangerates
btc = exchangerates.to_btc('INR', 50000)
print("\n50000 INR in Bitcoin: %s " % btc)
