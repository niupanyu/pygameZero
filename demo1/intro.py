import pgzrun
from pgzero.actor import Actor

alien = Actor('alien')
alien.pos = 100, 56
alien.width = 200
alien.height = 200


WIDTH = 500
HEIGHT = alien.height + 20


def draw():
    screen.fill((128, 0, 0))
    # screen.clear()
    alien.draw()


pgzrun.go()
