from gui import PASGui
import json
import sys

#sys.path.append('./game_sim')
from game_sim.simulation import Simulation



class App:
    def __init__(self):
        self.gui = PASGui()
        self.algo_list = dict()
        self.sim_list = dict()
        
        self.sim = None
        
        
    
    def fetch_algo(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as openfile:
            # Reading from json file
                self.algo_list = json.load(openfile)
        except Exception as e:
            print(f"Failed to load algorithms from {filename}: {e}")
            return False
        
    def fetch_sims(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as openfile:
            # Reading from json file
                self.sim_list = json.load(openfile)
        except Exception as e:
            print(f"Failed to load simulations from {filename}: {e}")
            return False
    
    def run_sim(self, episodes: int):
        # get sim ->  PriceGame
        # get players ->  dict(PriceAlgo)
        # make simulation obj
        # 
        
        
        pass
    
    
        