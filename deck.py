
def getNewDeck():
    deck = []
    for suit in ["spades","diamonds","hearts","clubs"]:
        for rank in ["ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king"]:
            deck.append(rank + " of " + suit)
    return deck
