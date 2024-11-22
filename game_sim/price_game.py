import random

class PriceGame:
    '''
    Wrapper class for Price Game
    
    For PriceGame object pg:
    
    pg.players:
        - int number of players in game
    
    pg.action_space:
        - tuple of upper lower bound for price choices ( (price_min, price_max) )
    
    pg.actions:
        - list of price actions from players
        - pg.actions[p] = int choice from player p
    
    pg.reward
        - function that returns reward for a player
        - Takes 2 parameters: player, pg.actions
    
    pg.choose(player, choice)
    
    
    '''
    # init new PriceGame object
    def __init__(self, players: int, action_space: tuple, reward: function):
        self.players = players
        self.action_space = action_space        
        self.actions = [None for i in range(players)]
        
        # Test if valid reward function
        try:
            p = reward(player = 0, actions = [random.randint(action_space[0], action_space[1]) for i in range (self.players)])
            if type(p) != float:
                raise Exception(f"reward() return type error (reward -> {type(p)})")
            self.reward = reward
        except:
            raise Exception("reward() parameter error")
            
    # Store action from player 
    def choose(self,player: int, action: int) -> None:
        if self.action_space[0] <= action <= self.action_space[1]:
            self.actions[player-1] = action
        else:
            raise Exception(f"Choice {action} out of bounds for player {player}")
            
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
            profits[p]= self.profit(player = p, choices = self.actions)
            
        return profits
   
    # Resets Game for next episode
    def reset(self) -> None:
        self.actions = [None for i in range(self.players)]