from pyphysicssandbox import *
from random import randint

def obver_func(keys):
    rgb=Color(randint(0,255),randint(0,255),randint(0,255))
    p=ColoredParticle(rgb)
    p.hit()
class Particle:
    def __init__(self):
        self.ball=ball((200+randint(-1,1),200+randint(-1,1)),20)
        self.direction=randint(-2000,2000),randint(-4000,4000)
    def hit(self):
        self.ball.hit(self.direction,(0,0))
class ColoredParticle(Particle):
    def __init__(self,c):
        super().__init__()
        self.color=c
        self.ball.color=self.color

window("fire",400,400)
c=cosmetic_box((0,0,0),400,400)
c.color=(0,0,0)
add_observer(obver_func)
run()
