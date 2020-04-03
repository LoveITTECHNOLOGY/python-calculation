from pyphysicssandbox import *
from random import randint



def obver_func(keys):
    """key是按键，加计数器每一秒运行一次函数，"""
    rgb=Color(randint(0,255),randint(0,255),randint(0,255))
    p=ColoredParticle(rgb)
    p.hit()
class Particle:
    def __init__(self):
        self.ball=ball((200+randint(-1,1),200+randint(-1,1)),20)
        self.direction=randint(-2000,2000),randint(-3000,3000)
    def hit(self):
        self.ball.hit(self.direction,(0,0))
class ColoredParticle(Particle):
    def __init__(self,c):
        super().__init__()
        self.color=c
        self.ball.color=self.color

window("python window",400,400)
c=cosmetic_box((0,0,0),400,400)
c.color=(0,0,0)

obver_func(add_observer)
run()