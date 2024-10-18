import random
type=['♠','♥','♦','♣']
a=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck=[]
for i in type:
    for j in a:
        deck.append(i+j)
random.shuffle(deck)
print(deck)
