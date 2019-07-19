import pykatchu

p1 = pykatchu.Pikatchu()
p2 = pykatchu.Aipom()
p3 = pykatchu.Bulbasaur()
p4 = pykatchu.Ditto()
p5 = pykatchu.Mewtwo()
pokemon = [p1,p2,p3,p4,p5]
gameOn = True

while gameOn:
    print(p1.getAttackNoise())
    print(p1.getName() + (" hit!" if p1.attack(p2) else " miss!"))
    if not p2.isDead():
        print(p2.getAttackNoise())
        print(p2.getName() + (" hit!" if p2.attack(p1) else " miss!"))
    if p1.isDead() or p2.isDead():
        gameOn = False
print("game is over... ")
if p1.isDead():
    print(p2.getName() + " won")
else:
    print(p1.getName() + " won")
