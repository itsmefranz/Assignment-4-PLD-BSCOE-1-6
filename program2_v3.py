def getAppleOrange():
    _apple= int(input("Please indicate how many apples you want to purchase: "))
    _orange= int(input("Please indicate how many apples you want to purchase: "))
    return _apple, _orange

def getPrice(aplamount, orgamount):
    apple_price= aplamount * 20
    orange_price= orgamount *25
    total= apple_price + orange_price
    return total 

apple, orange= getAppleOrange()

totalprice= getPrice(apple, orange)

print(f"The total amount is {totalprice} pesos.")