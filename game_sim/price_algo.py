from price_game import PriceGame 


class PriceAlgo:
    
    def __init__(self, pi: function, game: PriceGame, player: int):
        self.history = list()           # History of prev rounds
        self.id = player                # Algos player number in Price game
        self.env = game             
        self.pi = pi                    # Policy for prices
    
    