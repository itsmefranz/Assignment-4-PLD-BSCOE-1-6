def getMoneynApple():
    amountM= float(input("How much money do you have? "))
    appleprice= float(input("What is the price of an apple per piece? "))
    return amountM, appleprice

def getApple(money, price):
    maxnoApl= int(money // price)
    return maxnoApl
    
def getChange():
    change = float(money % appleP)
    return change

moneyamount, priceapple= getMoneynApple()
max_apple= getApple()
getChange()