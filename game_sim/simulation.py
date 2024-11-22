from price_game import PriceGame
from price_algo import PriceAlgo
import numpy as np
import matplotlib.pyplot as plt




class Simulation:
    
    def __init__(self,game: PriceGame, players: dict):
        self.game = game
        self.players = players
        
    def run_episode(self) -> tuple:
        for id in self.players.keys():
            player = self.players[id]
            self.game.choose(id, player.action(self.game.action_space))
        rewards = self.game.profit()
        actions = self.game.actions
        
        return actions, rewards
    
    
    def run_sim(self, rounds: int):
        rewards = np.array((rounds, len(self.players.keys())))
        actions = np.array((rounds, len(self.players.keys())))
        for r in range(rounds):
            actions_round, rewards_round = self.run_episode()
            rewards[r]=rewards_round
            actions[r] = actions_round
            
            round_entry = dict()
            for id in self.players.keys():
                round_entry.update({id:{'action': actions_round[id],
                                        'reward': rewards_round[id]}})
                
            for id in self.players.keys():
                self.players[id].update(round_entry)
        
        return actions, rewards
            
            
            
        

