'''====================================================
|
| Author      : Adam Valdez
| Title       : Coin Marketcap Ledger/Exchange Tracker
| Description : Reads prices from Coin Marketcap,
|               Displays them in the terminal.
|               Percentage gained, USD gained,
|               total gained and more.
| Date        : 12/19/2017
|
===================================================='''

from coinmarketcap import Market
from termcolor import colored


def coinmarket_cap():
    # Enter your crypto into what you have stored in the ledger
    ledger = {'Ethereum': 1.00, 'Ripple': 1.00}
    # Enter your crypto into what you have stored in the binance
    exchange = {'TRON': 1.00, 'Verge': 1.00, 'TNT': 1.00, 'IOTA': 1.00, 'Bitcoin': 1.00,
                   'FUN': 1.00, 'Cardano': 1.00, 'Stellar': 1.00, 'Quantstamp': 1.00, 'Litecoin': 1.00}
    total = {}
    # How much you have invested into cyrpto in total
    total_inv = 1000
    # Wallet value, if known
    walletValue = 10.00
    coinmarketcap = Market()
    # Lower limit means less coins, however faster result
    # Always start with BTC to star from top of list (assuming BTC is still #1)
    ticker = coinmarketcap.ticker(start='BTC', limit=100, convert='USD')
    i = 0
    # Loop count should be equal to limit count
    while 100 > i:
        name = ticker[i]['name']
        # Add every coin in your exchange in here
        if name == 'IOTA' or name == 'Bitcoin' or name == 'TRON' or name == 'Verge' or  name == 'TNT' or\
                        name == 'Quantstamp' or name == 'Cardano' or name == 'Stellar' or name == 'Litecoin':
            print ("----- " + ticker[i]['name'] + " -----")
            usd = float(ticker[i]['price_usd'])
            print ("Price: $ " + str(round(usd, 2)))
            percent = ticker[i]['percent_change_1h'] + "%"
            if percent[0] == '-':
                print (colored(percent, "red"))
            else:
                print(colored(percent, "green"))
            value = float(exchange[name]) * float(usd)
            walletValue = walletValue + round(value, 2)
            print("Wallet Value: $" + str(round(value, 2)))
        # Add every coin in your ledger here
        elif name == 'Ripple' or name == 'Ethereum':
            print ("----- " + ticker[i]['name'] + " -----")
            usd = float(ticker[i]['price_usd'])
            print ("Price: $ " + str(round(usd, 2)))
            percent = ticker[i]['percent_change_1h'] + "%"
            if percent[0] == '-':
                print (colored(percent, "red"))
            else:
                print(colored(percent, "green"))
            print("Wallet Value: $" + str(round(value, 2)))
            price = float(ticker[i]['price_usd'])
            total[name] = price * ledger[name]

        i += 1
    print("============ LEDGER VALUE =============")
    # Add coins from your ledger in here as well
    print("Ripple: $" + str(round(total['Ripple'], 2)))
    print("Ethereum: $" + str(round(total['Ethereum'], 2)))
    LedgerValue = float(total['Ripple']) + float(total['Ethereum'])
    print("Total Chain Value: $" + str(round(LedgerValue, 2)))

    print("============ TOTAL VALUE =============")
    totalValue = walletValue + LedgerValue
    print("Total: $" + str(round(totalValue, 2)))
    print("Invested: $" + str(total_inv))
    gains = round(totalValue - total_inv, 2)
    percent = '{:.1%}'.format(gains/total_inv)
    if gains > 0:
        print ("Total Gain: " + colored(gains, "green"))
        print (colored(percent, "green"))
    else:
        print ("Total Gain: " + colored(gains, "red"))
        print (colored(percent, "red"))


def main():
        coinmarket_cap()


if __name__ == "__main__":
    main()
