from yahoo_fin.stock_info import get_live_price

class Stocks:
    def __init__(self, symbol, qty = 0, cost = 0, price = 0, worth = 0):
        self.symbol = symbol
        self.qty = qty
        self.cost = cost
        self.price = price
        self.worth = worth


    """def __str__(self):
        return self.price, self.qty"""

    # This only updates one stock... not many
    # remember that cash updates too.
    def update(self):
        while True:
            print(
                "\n'Qty' is to change qty",
                "\n'C' is to change cost",
                "\n'ESC' is to exit")
            x = input()
            if x == "Qty":
                q = float(input("what is the new quanty: "))
                self.qty = q
            if x == "C":
                c = float(input("What is the new cost: "))
                print("0 : SGOL", "1 : VGLT", "2 : VGSH", "3 : VOO")
                c = int(input("enter the number to update the stock's cost: "))
                if c == 0:
                    
                    # add in a confirmation?
                self.cost = c
            if x == "ESC":
                break
        return "update completed\n"
    
    #this is price
    def find_price(self, symbol):
        ticker = self.symbol
        price = []
        for i in range(len(ticker)):
            l = round(get_live_price(ticker[i]), 3)
            price.append(l)
        self.price = price
        return price

    # this is to find market value
    def find_worth(self):
        worth = []
        self.worth = worth
        # sol = 0 + 1797.42
        for i in range(len(self.price)):
            s = round(self.price[i] * self.qty[i], 2)
            worth.append(s)
            # sol += s
        return worth, # sol


    def final_output(self):
        return f"price: {self.price}, market value: {self.worth}, cost: {self.cost}"



def main():
    symbol = ["SGOL", "VGLT", "VGSH", "VOO"]
    qty = [40.000, 7.165, 16.237, 4.018]
    cost = [600, 600, 1005, 1100]
    # cost = []
    S = Stocks(symbol, qty, cost)
    while True:
        x = input("UPDATES -- Y or N\n")
        if x == "Y":
            (S.update())
        else:
            break
    (S.find_price(symbol))
    (S.find_worth())
    print(S.final_output())
    

main()
