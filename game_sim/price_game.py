import random

class PriceGame:
    def __init__(self, players: int, choice_bound: tuple, profit: function):
        self.players = players
        self.choice_bound = choice_bound        
        self.choices = [None for i in range(players)]
        
        # Test if valid profit function
        try:
            p = profit(player = 0, choices = [random.randint(choice_bound[0], choice_bound[1]) for i in range (self.players)])
            if type(p) != float or type(p) != int:
                raise Exception(f"profit() return type error (profit -> {type(p)})")
            self.profit = profit
        except:
            raise Exception("profit() parameter error")
            
    # Store choice q from player 
    def choose(self,player: int, choice: int) -> None:
        if self.choice_bound[0] <= choice <= self.choice_bound[1]:
            self.choices[player-1] = choice
        else:
            raise Exception(f"Choice {choice} out of bounds for player {player}")
            
    # Return True if all choices have been made (for all c in self.choices: c != None) -> (return True)
    def verifyChoices(self) -> bool:
        flag = False
        for c in self.choices:
            if c is None:
                flag = True
        return not flag
    
    # Returns list of profits profit[i] = reward for player i
    def profit(self) -> list:
        profits = [0 for c in range(self.players)]
        
        for p in range(self.players):
            profits[p]= self.profit(player = p, choices = self.choices)
            
        return profits
   