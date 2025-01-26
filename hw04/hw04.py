from ucb import trace

@trace
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    # if len(lst1) == 0 or len(lst2) == 0:
    #     assert lst1 + lst2 != [], "we get 2 []s"
    #     # print(f"DEBUG: lst1 + lst2 = {lst1 + lst2}")
    #     return lst1 + lst2
    # if lst1[0] < lst2[0]:
    #     # print(f"DEBUG: merge {lst1[1:]} and {lst2}")
    #     result = merge(lst1[1:], lst2)
    #     result.insert(0, lst1[0])
    # else:
    #     # print(f"DEBUG: merge {lst1} and {lst2[1:]}")
    #     result = merge(lst1, lst2[1:])
    #     result.insert(0, lst2[0])
    # return result
    if len(lst1) == 0 or len(lst2) == 0:
        return lst1 + lst2
    if lst1[0] < lst2[0]:
        return merge(lst1[1:], lst2).insert(0, lst1[0])
    else:
        return merge(lst1, lst2[1:]).insert(0, lst2[0])


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def update(self):
        self.year = self.present_year

    def __init__(self):
        self.update()

    def create(self, coin):
        assert issubclass(coin, Coin), "coin must be of subclass of Coin"
        return coin(self.year)


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        print(f"DEBUG year = {self.year}")
        extra = max(Mint.present_year - self.year, 50) - 50
        print(f"DEBUG extra = {extra}")
        return self.cents + extra

class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.quantity = 0 
        self.balance = 0
    def vend(self):
        if self.quantity == 0:
            print(f"'Nothing left to vend. Please restock.'")
            return
        margin = self.price - self.balance
        if margin > 0:
            print(f"'You must add ${margin} more funds.'")
        else:
            self.balance = 0
            self.quantity -= 1
            if margin == 0:
                print(f"'Here is your {self.product}.'")
            else:
                print(f"'Here is your {self.product} and ${-margin} change.'")

    def add_funds(self, funds):
        if self.quantity == 0:
            print(f"'Nothing left to vend. Please restock. Here is your ${funds}.'")
            return
        self.balance += funds
        print(f"'Current balance: ${self.balance}'")

    def restock(self, new_quantity):
        self.quantity += new_quantity
        print(f"'Current {self.product} stock: {self.quantity}'")