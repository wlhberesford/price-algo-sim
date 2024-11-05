from price_game import PriceGame 


class PriceAlgo:
    '''
    Wrapper class for Price Algorithm
    
    For PriceAlgo object pa:
    
    pa.policy: 
        - Function to return price during a price game
        - Takes 3 parameters: player id (pa.id), game history (pa.history), bounds tuple ( (price_min, price,max) )
        - returns int price value
        
    pa.id:
        - int for pa's id in simulation
        
    pa.history:
        - list of dictionaries to represent previous games 
        - pa.history[t][i] = {price: int, reward: float} for player_i at time t


    pa.action((min,max))
        - returns int price value p: min <= p <= max
        - Raises TypeError exception if pg.policy !-> int
        
    pa.update(episode_results)
        - updates pa.history
        - episode_results[i] = {action: int, reward: float}
    
    pa.reset()
        - clears pa.history
    '''
    
    # init new PriceAlgo object
    def __init__(self, pi: function, game: PriceGame, player: int):
        self.history = list()           # History of prev rounds
        self.id = player                # Algos player number in Price game
        self.policy = pi                # Policy for prices
        
    # returns new price action based on previouse observations
    def action(self, bounds: tuple) -> int:
        a = self.policy(self.id, self.history, bounds)
        if type(a) == int:
            return a
        raise Exception(f"Policy Type Error: policy returns {type(a)} not int")
    
    # Updates history with episode_results
    def update(self, episode_results):
        iteration = episode_results
        self.history.append(iteration)
        
    # Clears self.history
    def reset(self):
        self.history = list()
    
    