def getAppleOrange():
    _apple= input("Please indicate how many apples you want to purchase: ")
    _orange= input("Please indicate how many apples you want to purchase: ")
    return _apple, _orange

apple, orange= getAppleOrange()

totalprice= getPrice(apple, orange)
