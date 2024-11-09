from gui import PASGui
import json

class App:
    def __init__(self):
        self.gui = PASGui()
        self.algorithms = dict()
        self.simulations = dict()
        
    
    def fetch_algo(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as openfile:
            # Reading from json file
                self.algorithms = json.load(openfile)
        except Exception as e:
            print(f"Failed to load algorithms from {filename}: {e}")
            return False
        
    def fetch_sims(self, filename: str) -> bool:
        try:
            with open(filename, 'r') as openfile:
            # Reading from json file
                self.simulations = json.load(openfile)
        except Exception as e:
            print(f"Failed to load simulations from {filename}: {e}")
            return False
    
    
        