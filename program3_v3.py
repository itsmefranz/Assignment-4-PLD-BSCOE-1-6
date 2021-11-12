def getMoneynApple():
    amountM= float(input("How much money do you have? "))
    appleprice= float(input("What is the price of an apple per piece? "))
    return amountM, appleprice

def getApple(money, price):
    maxnoApl= int(money // price)
    return maxnoApl
    
def getChange(moneyamount, priceapple):
    change = float(moneyamount % priceapple)
    return change

moneyamount, priceapple= getMoneynApple()
max_apple= getApple(moneyamount, priceapple)
final_change= getChange(moneyamount, priceapple)

print(f"You can buy {max_apple} apples and your change is {final_change: .2f} pesos.")