def getAppleOrange():
    _apple= input("Please indicate how many apples you want to purchase: ")
    _orange= input("Please indicate how many apples you want to purchase: ")
    return _apple, _orange

def getPrice(aplamount, orgamount):
    apple_price= aplamount * 20
    orange_price= orgamount *25

apple, orange= getAppleOrange()

totalprice= getPrice(apple, orange)
