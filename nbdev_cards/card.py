# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 4
suits = ["♣️", "♦️", "❤️", "♠️"]
ranks = [None, "A"] + [str(x) for x in range(2,11)]  + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 5
class Card:
    "Represents a standard playing card."
    def __init__(self, suit=0, rank=2):
        self.suit,self.rank = suit, rank
        self.suit_nm,self.rank_nm = suits[self.suit],ranks[self.rank]

    def __eq__(self, other): return (self.suit, self.rank) == (other.suit, other.rank)
    def __lt__(self, other): return (self.suit, self.rank) < (other.suit, other.rank)
    def __str__(self): return f'{self.rank_nm}{self.suit_nm}'
    __repr__ = __str__
