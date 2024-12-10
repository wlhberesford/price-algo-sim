'''
Cournot Competition
    pi_i = (p_i-c)D(p_i, p_j)
        - a: max price
        - c: marginal cost
        - D: demand function
'''
# Hyper Parameters
A = 100          
C = 0

# Action Space
BOUNDS = (0, 100)

def reward(player: int, actions: list):
    min_price = min(actions)
    min_count = actions.count(min_price)
    
    if actions[player] != min_price:
        return 0
    elif min_count == 2:
        return (min_price-C)*demand(min_price)/2.0
    else:
        return (min_price-C)*demand(min_price) * 1.0
        
    
def demand(price: int):
    return A - price

