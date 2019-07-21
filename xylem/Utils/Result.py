import json

class Result:
    def __init__(self, ticker, orders, starting_balance, ending_balance):
        self.ticker = ticker
        self.orders = orders
        self.starting_balance = starting_balance
        self.ending_balance = ending_balance

    def json(self):
        data = {}
        data['ticker'] = self.ticker
        data['orders'] = self.orders
        data['starting_balance'] = self.starting_balance
        data['ending_balance'] = self.ending_balance
        
        return json.dumps(data)
    
    def __str__(self):
        return self.json()

    def printResult(self):
        print("=======================================")
        print("Summary Statistics ({}):".format(self.ticker))
        print("=======================================")
        print("Starting Balance: {:.2f}".format(self.starting_balance))
        print("Ending Balance: {:.2f}".format(self.ending_balance))
        print("=======================================")
