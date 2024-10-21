
class Node:
    '''
    Represents the Node in a tree of a Normal Form Game
     - player (int): p in [1-inf) if normal player, -1 if player is nature, 0 for leaf
     - options (func(choice) => bool): function that returns True when choice is a valid choice
    '''
    
    def __init__(self, player = None, options = None):
        self.player = player
        self.options = options
        self.children = dict()
        
    def set_player(self, player: int) -> None:
        self.player = player
        
    def get_player(self) -> int:
        return self.player
    
    def is_leaf(self) -> bool:
        return self.player == 0
    
    def set_options(self,options: function) -> None:
        self.options = options
        
    def check_option(self,choice) -> bool:
        return self.options(choice)
    
    def add_child(self,choice, child):
        self.children.update({choice:child})