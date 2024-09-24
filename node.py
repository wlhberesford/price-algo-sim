class Node:
    
    def __init__(self, id: int, choices: dict) -> None:
        self.id=id
        self.choices=choices
        
    def id(self):
        return self.id
    
    def choices(self):
        return self.choice.keys()
    
    def action(self, choice):
        return self.choices[choice]
    
    
class Leaf(Node):
    